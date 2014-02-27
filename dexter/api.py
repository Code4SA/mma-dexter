import logging
log = logging.getLogger(__name__)

from flask import request, url_for, redirect, jsonify

from .app import app
from .models import db, Author, Person

@app.route('/api/authors')
def api_authors():
    authors = Author.query.order_by(Author.name).all()
    return jsonify({'authors': [a.json() for a in authors]})

@app.route('/api/people')
def api_people():
    people = Person.query.order_by(Person.name).all()
    return jsonify({'people': [p.json() for p in people]})
