import logging
log = logging.getLogger(__name__)

from flask import request, url_for, flash, redirect, make_response
from flask.ext.mako import render_template
from flask.ext.login import login_required, current_user
from sqlalchemy.orm import subqueryload

from .app import app
from .models import db, Document, Entity, Utterance, DocumentEntity, Person
from .models.person import PersonForm

import urllib


@app.route('/entities/<string:group>/<string:name>/')
@login_required
def show_entity(group, name):

    entity = Entity.query.filter(Entity.group==group, Entity.name==name).first()

    if not entity:
        return make_response("The specified entity could not be found.", 404)

    if entity.person:
        return redirect(url_for('show_person', id=entity.person.id))

    documents = Document.query\
        .join(DocumentEntity)\
        .options(subqueryload(Document.utterances))\
        .filter(DocumentEntity.entity_id==entity.id)\
        .order_by(Document.published_at.desc()).all()

    return render_template('entities/show.haml', entity=entity, documents=documents)


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


    documents = Document.query\
        .join(DocumentEntity)\
        .options(subqueryload(Document.utterances))\
        .filter(DocumentEntity.entity_id.in_(person.alias_entity_ids))\
        .order_by(Document.published_at.desc()).all()

    return render_template('person/show.haml',
        person=person,
        form=form,
        documents=documents)

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
