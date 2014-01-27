from pyramid.response import Response
from pyramid.exceptions import NotFound
from pyramid.httpexceptions import HTTPFound, HTTPNotModified, HTTPSeeOther, HTTPMovedPermanently
from pyramid.view import view_config

import logging
log = logging.getLogger(__name__)

from .models import (
    DBSession,
    Document,
    )

from .processing import DocumentProcessor

@view_config(route_name='show_article', renderer='articles/show.haml')
def show_article(request):
    document = DBSession.query(Document).get(request.matchdict['id'])
    if not document:
        raise NotFound()
    return {"document": document}
 

@view_config(route_name='add_article', renderer='articles/new.haml')
def add_article(request):
    url = request.params.get('url')
    return {"url": url}


@view_config(route_name='new_article', renderer='articles/new.haml')
def new_article(request):
    url = request.params.get('url')
    if url:
        proc = DocumentProcessor()

        if not proc.valid_url(url):
            request.session.flash("The URL isn't valid or we don't know how to process it.", 'error')
            raise HTTPSeeOther(request.route_url('new_article', _query={'url': url}))

        url = proc.canonicalise_url(url)
        doc = DBSession.query(Document).filter(Document.url == url).first()

        if doc:
            # already exists
            raise HTTPNotModified(request.route_url('show_article', id=doc.id))

        # create and process the document
        doc = DocumentProcessor().process(url)
        # TODO: error handling
        raise HTTPMovedPermanently(request.route_url('show_article', id=doc.id))
    else:
        raise HTTPSeeOther(request.route_url('new_article'))
