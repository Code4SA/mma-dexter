import logging
import logging.config
import os
import sys

from flask import Flask

app = Flask(
    __name__,
    static_folder='public')

app.secret_key = 'satoheu8fabasof8sahbdai8fa834nts234b8aeuasiub8afil0a8feuohaoteuhbacgla8iufabiu'

# setup configs
env = os.environ.get('FLASK_ENV', 'development')

# nosetest doesn't give us much room to setup a test config
if sys.argv[0].endswith('nosetests'):
    env = 'test'

app.config['ENV'] = env
app.config.from_pyfile('config/%s.cfg' % env)

# setup logging
with open('%s/config/%s-logging.yaml' % (app.root_path, env)) as f:
    import yaml
    logging.config.dictConfig(yaml.load(f))

# attach the user id to logs
from flask import request_started, session
from logs import UserIdFilter

def log_attach_user_id(sender, **extra):
    UserIdFilter.set_userid(session.get('user_id', '-'))
request_started.connect(log_attach_user_id, app)


# setup templates and haml
from flask.ext.mako import MakoTemplates, _lookup, render_template
import haml
MakoTemplates(app)
app.config['MAKO_PREPROCESSOR'] = haml.preprocessor
app.config['MAKO_TRANSLATE_EXCEPTIONS'] = False
app.config['MAKO_DEFAULT_FILTERS'] = ['decode.utf8']

# CSRF protection
from flask_wtf.csrf import CsrfProtect
CsrfProtect(app)

# Database
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)


# Mail
from flask_mail import Mail
mail = Mail(app)


# htpasswd-based basic auth for API access
from flask.ext import htauth
app.config['HTAUTH_HTPASSWD_PATH'] = './resources/nginx/htpasswd'
app.config['HTAUTH_REALM'] = 'Dexter'
htauth.HTAuth(app)


# file attachments
from .attachments import setup_attachments
setup_attachments(app)

# celery tasks
if env == 'production':
    from celery import Celery
    celery_app = Celery('dexter', include=['dexter.tasks', 'dexter.app'])
    celery_app.config_from_object('dexter.config.celeryconfig')
