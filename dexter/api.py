import logging
log = logging.getLogger(__name__)

from flask import request, url_for, redirect, jsonify
from flask.ext.login import login_required
from sqlalchemy.orm import subqueryload

from .app import app
from .models import db, Author, Person, Entity

@app.route('/api/authors')
@login_required
def api_authors():
    authors = Author.query.order_by(Author.name).all()
    return jsonify({'authors': [a.json() for a in authors]})

@app.route('/api/people')
@login_required
def api_people():
    people = Person.query\
        .options(subqueryload(Person.affiliation))\
        .order_by(Person.name)\
        .all()
    return jsonify({'people': [p.json() for p in people]})

@app.route('/api/entities')
@login_required
def api_entities():
    query = Entity.query.order_by(Entity.name)
    q = request.args.get('q', '').strip()
    if q:
        q = '%' + q.replace('%', '%%').replace(' ', '%') + '%'
        query = query.filter(Entity.name.like(q))

    entities = query.all()

    return jsonify({'entities': [e.json() for e in entities]})

@app.route('/api/entities/<string:group>')
@login_required
def api_group_entities(group):
    query = Entity.query.filter(Entity.group == group).order_by(Entity.name)
    q = request.args.get('q', '').strip()
    if q:
        q = '%' + q.replace('%', '%%').replace(' ', '%') + '%'
        query = query.filter(Entity.name.like(q))

    entities = query.all()

    return jsonify({'entities': [e.json() for e in entities]})
