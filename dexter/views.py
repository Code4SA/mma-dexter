from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    )


@view_config(route_name='home', renderer='home.haml')
def my_view(request):
    return {'one': None, 'project': 'dexter'}
