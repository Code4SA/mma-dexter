from dexter.models import db, Document, Entity, Utterance, Medium
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
import flask_wtf

class MyModelView(ModelView):
    form_base_class = flask_wtf.Form

admin_instance = Admin(base_template='admin/custom_master.html', name="Dexter")
admin_instance.add_view(MyModelView(Document, db.session))
admin_instance.add_view(MyModelView(Entity, db.session))
admin_instance.add_view(MyModelView(Utterance, db.session))
admin_instance.add_view(MyModelView(Medium, db.session))