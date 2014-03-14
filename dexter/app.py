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

# setup templates and haml
from flask.ext.mako import MakoTemplates, _lookup
import haml
MakoTemplates(app)
app.config['MAKO_PREPROCESSOR'] = haml.preprocessor
app.config['MAKO_TRANSLATE_EXCEPTIONS'] = False
app.config['MAKO_DEFAULT_FILTERS'] = ['decode.utf8']

from flask_wtf.csrf import CsrfProtect, generate_csrf
CsrfProtect(app)

@app.context_processor
def csrf_token():
    return dict(csrf_token=generate_csrf)


# user authentication
from flask.ext.login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user_login'

from dexter.authn import AnonymousUser
login_manager.anonymous_user = AnonymousUser

@login_manager.user_loader
def load_user(userid):
    from .models import User

    user = User.query.get(userid)

    # don't allow disabled users
    if user and user.disabled:
        user = None

    return user

# attach the user id to logs
from flask import request_started, session
from logs import UserIdFilter

def log_attach_user_id(sender, **extra):
    UserIdFilter.set_userid(session.get('user_id', '-'))
request_started.connect(log_attach_user_id, app)
