import logging
log = logging.getLogger(__name__)

from flask import request, url_for, flash, redirect
from flask.ext.mako import render_template

from .app import app
from .models import db, Document
from .models.document import DocumentForm

from .processing import DocumentProcessor

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

        if url:
            # new document from url
            proc = DocumentProcessor()

            if not proc.valid_url(url):
                flash("The URL isn't valid or we don't know how to process it.", 'error')
            else:
                url = proc.canonicalise_url(url)
                doc = Document.query.filter(Document.url == url).first()

                if doc:
                    # already exists
                    flash("We already have that article.")
                else:
                    # create and process the document
                    # TODO: error handling
                    doc = DocumentProcessor().process(url)

        else:
            # new document from article text
            if form.validate():
                doc = Document()
                form.populate_obj(doc)

        if doc:
            if not doc.id:
                db.session.add(doc)
                db.session.flush()
                id = doc.id
                db.session.commit()
            else:
                id = doc.id

            return redirect(url_for('edit_article', id=id))
        
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
