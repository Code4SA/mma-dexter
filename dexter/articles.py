from pyramid.response import Response
from pyramid.exceptions import NotFound
from pyramid.httpexceptions import HTTPSeeOther, HTTPMovedPermanently
from pyramid.view import view_config
import transaction

import logging
log = logging.getLogger(__name__)

from .models import (
    DBSession,
    Document,
    )
from .models.document import DocumentForm

from .processing import DocumentProcessor

@view_config(route_name='show_article', renderer='articles/show.haml')
def show_article(request):
    document = DBSession.query(Document).get(request.matchdict['id'])
    if not document:
        raise NotFound()
    return {"document": document}
 

@view_config(route_name='new_article', renderer='articles/new.haml')
def new_article(request):
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
                doc = DBSession.query(Document).filter(Document.url == url).first()

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
                DBSession.add(doc)
                DBSession.flush()
                id = doc.id
                transaction.commit()
            else:
                id = doc.id

            raise HTTPMovedPermanently(request.route_url('edit_article', id=id))
        
    return {'url': url, 'form': form}


@view_config(route_name='edit_article', renderer='articles/edit.haml')
def edit_article(request):
    doc = DBSession.query(Document).get(request.matchdict['id'])
    if not doc:
        raise NotFound()

    form = DocumentForm(request.params)
    return {'doc': doc, 'form': form}
