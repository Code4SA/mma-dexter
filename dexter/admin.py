from models import db, Document, Entity, Utterance, Medium
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from .app import app

admin = Admin(app)
admin.add_view(ModelView(Document, db.session))
admin.add_view(ModelView(Entity, db.session))
admin.add_view(ModelView(Utterance, db.session))
admin.add_view(ModelView(Medium, db.session))