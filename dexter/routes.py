from dexter.app import app
from flask.ext.mako import render_template
from flask import render_template as flask_render_template
import logging
log = logging.getLogger(__name__)

from dexter.models import Document, Entity, DocumentEntity

import dexter.articles
import dexter.entities

@app.route('/')
def home():
    documents = Document.query.order_by(Document.published_at.desc()).limit(100)
    return render_template('index.haml',
            documents=documents)