from itertools import groupby
import logging
log = logging.getLogger(__name__)

from flask import request, url_for, flash, redirect, make_response
from flask.ext.mako import render_template
from flask.ext.login import login_required, current_user
from sqlalchemy.orm import subqueryload
from sqlalchemy import distinct

from datetime import datetime, timedelta

from .app import app
from .models import db, Document, Entity, Utterance, DocumentEntity, DocumentSource, Person
from .models.person import PersonForm
from .utils import paginate
from .analysis import SourceAnalyser

import urllib


@app.route('/entities/<string:group>/<string:name>/')
@login_required
def show_entity(group, name):

    entity = Entity.query.filter(Entity.group==group, Entity.name==name).first()

    if not entity:
        return make_response("The specified entity could not be found.", 404)

    if entity.person:
        return redirect(url_for('show_person', id=entity.person.id))

    query = db.session.query(distinct(Document.id))\
              .join(DocumentEntity)\
              .filter(DocumentEntity.entity_id == entity.id)\
              .order_by(Document.published_at.desc())
    pagination = paginate(query, int(request.args.get('page', 1)), 50)
    doc_ids = [r[0] for r in pagination.items]

    docs = Document.query\
        .options(subqueryload(Document.utterances))\
        .filter(Document.id.in_(doc_ids))\
        .order_by(Document.published_at.desc())\
        .all()

    return render_template('entities/show.haml', entity=entity, docs=docs, pagination=pagination)


@app.route('/people/<int:id>/', methods=['GET', 'POST'])
@login_required
def show_person(id):
    person = Person.query.get(id)
    if not person:
        return make_response("The specified entity could not be found.", 404)

    form = PersonForm(obj=person)
    form.alias_entity_ids.choices = sorted(
            [[str(e.id), '%s (%s, %d)' % (e.name, e.group, e.id)] for e in person.entities],
            key=lambda t: t[1])

    if request.method == 'POST' and current_user.admin:
        if form.validate():
            form.populate_obj(person)

            if person.gender_id == '':
                person.gender_id = None
            if person.race_id == '':
                person.race_id = None

            flash('Saved.')
            db.session.commit()
            return redirect(url_for('show_person', id=id))

    # docs where this person is a source
    query = db.session.query(distinct(Document.id))\
              .join(DocumentSource)\
              .filter(DocumentSource.person == person)\
              .order_by(Document.published_at.desc())
    pagination = paginate(query, int(request.args.get('page', 1)), 50)
    doc_ids = [r[0] for r in pagination.items]

    docs = Document.query\
        .options(subqueryload(Document.utterances))\
        .filter(Document.id.in_(doc_ids))\
        .order_by(Document.published_at.desc())\
        .all()

    # group docs by date
    grouped_docs = []
    for date, group in groupby(docs, lambda d: d.published_at.date()):
        grouped_docs.append([date, list(group)])

    # source frequency
    today = datetime.utcnow().date() - timedelta(days=1)
    sa = SourceAnalyser(start_date=(today - timedelta(days=14)), end_date=today)
    sa.analyse()
    source_analysis = sa.analysed_people.get(person.id)

    return render_template('person/show.haml',
        person=person,
        form=form,
        source_analysis=source_analysis,
        grouped_docs=grouped_docs,
        pagination=pagination)

@app.route('/people/<int:id>/merge', methods=['POST'])
@login_required
def merge_person(id):
    if current_user.admin:
        person = Person.query.get(id)
        if not person:
            return make_response("The specified entity could not be found.", 404)

        if 'mergein' in request.args:
            # merge someone into this person
            dup = Person.query.get(request.args['mergein'])
            if dup:
                dup.merge_into(person)
                flash('Merged %s into %s.' % (dup.name, person.name))
                db.session.commit()

    return redirect(url_for('show_person', id=id))

@app.route('/people/new', methods=['POST'])
@login_required
def new_person():
    name = request.form.get('name', '')
    entity_id = request.form.get('entity_id')

    if name:
        if entity_id:
            entity = Entity.query.filter(Entity.name == name).first()
        else:
            entity = None

        person = Person.get_or_create(name)
        if entity:
            person.entities.append(entity)

        id = person.id
        db.session.commit()
        return redirect(url_for('show_person', id=id))

    return redirect_to('/')
