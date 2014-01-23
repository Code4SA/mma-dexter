from pyramid.config import Configurator
from webassets import Bundle


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    setup_database(settings)

    config = Configurator(settings=settings)

    config.add_mako_renderer('.haml')

    setup_routes(config)

    config.scan()
    return config.make_wsgi_app()


def setup_routes(config):
    setup_assets(config)

    config.add_route('home', '/')

    # articles
    config.add_route('show_article', '/articles/{id}', request_method='GET')


def setup_database(settings):
    from sqlalchemy import engine_from_config
    from .models import DBSession, Base

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

def setup_assets(config):
    css = Bundle('css/app.scss',
            filters='scss',
            output='css/app.%(version)s.css')

    config.add_webasset('css', css)
