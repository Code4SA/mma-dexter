from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Document,
    )


@view_config(route_name='home', renderer='home.haml')
def my_view(request):
    documents = DBSession.query(Document).order_by(Document.published_at.desc()).limit(100)
    return {'documents': documents}
