from dexter.models import db, Document, Entity, Utterance, Medium
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.model.template import macro
from wtforms.fields import SelectField, TextAreaField
import flask_wtf

class MyModelView(ModelView):
    form_base_class = flask_wtf.Form

class DocumentView(MyModelView):

    can_add = False
    list_template = 'admin/custom_list_template.html'
    column_list = (
        'published_at',
        'medium',
        'title',
        'blurb',
        'updated_at'
    )
    column_labels = dict(
        published_at='Date Published',
        medium='Source',
        updated_at='Last Updated',
    )
    column_sortable_list = [
        'published_at',
        ('medium', Medium.name),
        'title',
        'blurb',
        'updated_at'
    ]
    column_formatters = dict(
        medium=macro('render_medium'),
        published_at=macro('render_date'),
        title=macro('render_title'),
        updated_at=macro('render_date')
    )
    form_overrides = dict(
        blurb=TextAreaField,
        text=TextAreaField,
    )

admin_instance = Admin(base_template='admin/custom_master.html', name="Dexter")
admin_instance.add_view(DocumentView(Document, db.session))
admin_instance.add_view(MyModelView(Entity, db.session))
admin_instance.add_view(MyModelView(Utterance, db.session))
admin_instance.add_view(MyModelView(Medium, db.session))