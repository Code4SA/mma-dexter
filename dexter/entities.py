import logging
log = logging.getLogger(__name__)

from flask import request, url_for, flash, redirect, make_response
from flask.ext.mako import render_template

from .app import app
from .models import db, Document, Entity, Utterance, DocumentEntity
import urllib


@app.route('/<string:group>/<string:name>/')
def show_entity(group, name):

    entity = Entity.query.filter(Entity.group==group, Entity.name==name).first()

    if not entity:
        return make_response("The specified entity could not be found.", 404)

    documents = Document.query.join(DocumentEntity)\
        .filter(DocumentEntity.entity_id==entity.id)\
        .order_by(Document.published_at.desc()).all()

    return render_template('entities/show.haml', entity=entity, documents=documents)
