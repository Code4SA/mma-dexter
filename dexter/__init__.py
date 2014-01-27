import os
from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from webassets import Bundle


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    setup_database(settings)

    session = UnencryptedCookieSessionFactoryConfig(os.environ.get('PYRAMID_SESSION_SECRET', settings.get('sessions.secret')))
    config = Configurator(settings=settings, session_factory=session)

    config.add_mako_renderer('.haml')

    setup_routes(config)

    config.scan()
    return config.make_wsgi_app()


def setup_routes(config):
    setup_assets(config)

    config.add_route('home', '/')

    # articles
    config.add_route('add_article', 'articles/new', request_method='GET')
    config.add_route('new_article', 'articles/new', request_method='POST')
    config.add_route('show_article', '/articles/{id}', request_method='GET')


def setup_database(settings):
    from sqlalchemy import engine_from_config
    from .models import DBSession, Base

    # load URL from env variable, falling back to the ini setting
    settings['sqlalchemy.url'] = os.environ.get('SQLALCHEMY_URL', settings.get('sqlalchemy.url'))

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

def setup_assets(config):
    env = config.get_webassets_env()
    # force this to be a list
    env.load_path = env.load_path.split()

    config.add_webasset('css', 
            Bundle(
                'css/bootstrap-3.0.3.min.css',
                'css/bootstrap-3.0.3-theme.min.css',
                Bundle(
                    'css/*.scss',
                    filters='pyscss',
                    output='css/app.%(version)s.css'),
                output='css/all.%(version)s.css'))

    config.add_webasset('js', 
            Bundle(
                'js/jquery-1.10.2.min.js',
                'js/bootstrap-3.0.3.min.js',
                output='js/app.%(version)s.js'))
