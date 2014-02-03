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
 

@app.route('/articles/new', methods=['GET', 'POST'])
def new_article():
    form = DocumentForm()
    url = form.url.data

    if request.method == 'POST':
        doc = None
        proc = DocumentProcessor()

        if url and not 'manual' in request.form:
            # new document from url
            if not proc.valid_url(url):
                flash("The URL isn't valid or we don't know how to process it.", 'error')
            else:
                url = proc.canonicalise_url(url)
                doc = Document.query.filter(Document.url == url).first()

                if doc:
                    # already exists
                    flash("We already have that article.")
                    return redirect(url_for('show_article', id=doc.id))

                try:
                    doc = proc.process_url(url)
                except ProcessingError as e:
                    log.error("Error processing %s: %s" % (url, e), exc_info=e)
                    flash("Something went wrong processing the document: %s" % (e,), 'error')
                    doc = None

        else:
            # new document from article text
            if form.validate():
                doc = Document()
                form.populate_obj(doc)

                try:
                    proc.process_document(doc)
                except ProcessingError as e:
                    log.error("Error processing raw document: %s" % (e, ), exc_info=e)
                    flash("Something went wrong processing the document: %s" % (e,), 'error')
                    doc = None

        if doc:
            db.session.add(doc)
            db.session.flush()
            id = doc.id
            db.session.commit()
            flash('Article added.')
            return redirect(url_for('show_article', id=id))
        
    return render_template('articles/new.haml',
            url=url,
            form=form)


@app.route('/articles/<id>/edit')
def edit_article(id):
    doc = Document.query.get_or_404(id)
    form = DocumentForm()
    return render_template('articles/edit.haml',
            doc=doc,
            form=form)
