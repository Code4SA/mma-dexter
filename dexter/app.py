import logging
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
logging.basicConfig(level=(logging.DEBUG if env == 'development' else logging.INFO),
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
logging.getLogger("requests").setLevel(logging.DEBUG)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

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
