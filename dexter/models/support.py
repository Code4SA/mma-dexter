# setup the db
from dexter.app import app
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
