from pyramid.response import Response
from pyramid.exceptions import NotFound
from pyramid.view import view_config

import logging
log = logging.getLogger(__name__)

from .models import (
    DBSession,
    Document,
    )

@view_config(route_name='show_article', renderer='articles/show.haml')
def show_article(request):
    document = DBSession.query(Document).get(request.matchdict['id'])
    if not document:
        raise NotFound()
    return {"document": document}
