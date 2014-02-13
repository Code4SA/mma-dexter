import logging
log = logging.getLogger(__name__)

from flask import request, url_for, redirect, jsonify

from .app import app
from .models import db, Author

@app.route('/api/authors')
def api_authors():
    authors = Author.query.order_by(Author.name).all()
    return jsonify({'authors': [a.json() for a in authors]})
