import logging
log = logging.getLogger(__name__)

from flask import request, url_for, render_template

from .app import app
from .models import db, Document
from .models.document import DocumentForm

from .processing import DocumentProcessor

@app.route('/articles/<id>')
def show_article(id):
    document = db.query(Document).get_or_404(id)
    return render_template('articles/show.haml',
            document=document)
 

@app.route('/articles/new')
def new_article():
    form = DocumentForm(request.params)
    url = form.url.data

    if request.method == 'POST':
        doc = None

        if url:
            # new document from url
            proc = DocumentProcessor()

            if not proc.valid_url(url):
                request.session.flash("The URL isn't valid or we don't know how to process it.", 'error')
            else:
                url = proc.canonicalise_url(url)
                doc = db.query(Document).filter(Document.url == url).first()

                if doc:
                    # already exists
                    request.session.flash("We already have that article.")
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
                db.add(doc)
                db.flush()
                id = doc.id
                transaction.commit()
            else:
                id = doc.id

            raise HTTPMovedPermanently(request.route_url('edit_article', id=id))
        
    return render_template('articles/show.haml',
            url=url,
            form=form)


@app.route('/articles/<id>/edit')
def edit_article(id):
    doc = db.query(Document).get_or_404(id)
    form = DocumentForm(request.params)
    return render_template('articles/edit.haml',
            doc=doc,
            form=form)
