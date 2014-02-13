import logging
log = logging.getLogger(__name__)

from flask import request, url_for, flash, redirect, make_response
from flask.ext.mako import render_template

from .app import app
from .models import db, Document, Entity, Utterance, DocumentEntity, Person
import urllib


@app.route('/<string:group>/<string:name>/')
def show_entity(group, name):

    entity = Entity.query.filter(Entity.group==group, Entity.name==name).first()

    if not entity:
        return make_response("The specified entity could not be found.", 404)

    if entity.person:
        return redirect(url_for('show_person', id=entity.person.id))

    documents = Document.query.join(DocumentEntity)\
        .filter(DocumentEntity.entity_id==entity.id)\
        .order_by(Document.published_at.desc()).all()

    return render_template('entities/show.haml', person=None, entities=[entity, ], documents=documents)


@app.route('/person/<int:id>/')
def show_person(id):

    person = Person.query.get(id)

    if not person:
        return make_response("The specified entity could not be found.", 404)

    entities = Entity.query.filter(Entity.person==person).all()
    tmp_ids = []
    for entity in entities:
        tmp_ids.append(entity.id)

    documents = Document.query.join(DocumentEntity)\
        .filter(DocumentEntity.entity_id.in_(tmp_ids))\
        .order_by(Document.published_at.desc()).all()

    return render_template('entities/show.haml', person=person, entities=entities, documents=documents)
