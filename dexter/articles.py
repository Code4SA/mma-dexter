import logging
log = logging.getLogger(__name__)

from flask import request, url_for, flash, redirect
from flask.ext.mako import render_template

from .app import app
from .models import db, Document
from .models.document import DocumentForm

from .processing import DocumentProcessor, ProcessingError

@app.route('/articles/<id>')
def show_article(id):
    document = Document.query.get_or_404(id)
    return render_template('articles/show.haml',
            document=document)


@app.route('/articles/<id>/edit')
def edit_article(id):
    doc = Document.query.get_or_404(id)
    form = DocumentForm()
    return render_template('articles/edit.haml',
            doc=doc,
            form=form)
