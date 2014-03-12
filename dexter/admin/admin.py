from dexter.models import db, Document, Entity, Medium, DocumentType, Topic, Fairness, Individual, User
from flask.ext.admin import Admin, expose, AdminIndexView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.model.template import macro
from wtforms.fields import SelectField, TextAreaField, TextField, HiddenField
import flask_wtf

from ..forms import Form

class MyModelView(ModelView):
    form_base_class = Form
    can_create = True
    can_edit = True
    can_delete = False
    page_size = 50


class MyIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        document_count = Document.query.count()
        self._template_args['document_count'] = document_count

        earliest = Document.query.order_by(Document.published_at).first()
        if earliest:
            self._template_args['date_from'] = earliest.published_at
        latest = Document.query.order_by(Document.published_at.desc()).first()
        if latest:
            self._template_args['date_to'] = latest.published_at

        group_counts = {}
        tmp = db.session.query(db.func.count(Entity.id), Entity.group).group_by(Entity.group).all()
        if tmp:
            for row in tmp:
                group_counts[str(row[1])] = int(row[0])
            self._template_args['group_counts'] = group_counts

        source_count = []
        tmp = db.session.query(db.func.count(Document.id), Medium.name) \
            .join(Medium) \
            .group_by(Document.medium_id) \
            .order_by(db.func.count(Document.id)) \
            .limit(5)
        for row in tmp:
            source_count.append([str(row[1]), int(row[0])])
        self._template_args['source_count'] = source_count
        return super(MyIndexView, self).index()

class DocumentView(MyModelView):

    can_create = False
    can_edit = False
    can_delete = False
    list_template = 'admin/custom_list_template.html'
    column_list = (
        'published_at',
        'medium',
        'title',
        'summary',
        'updated_at'
    )
    column_labels = dict(
        published_at='Date Published',
        medium='Source',
        updated_at='Last Updated',
        )
    column_sortable_list = (
        'published_at',
        ('medium', Medium.name),
        'title',
        'summary',
        'updated_at'
    )
    column_formatters = dict(
        medium=macro('render_medium'),
        published_at=macro('render_date'),
        title=macro('render_document_title'),
        updated_at=macro('render_date')
    )
    form_overrides = dict(
        summary=TextAreaField,
        text=TextAreaField,
        )
    column_searchable_list = (
        'title',
        'summary',
    )
    page_size = 50


class EntityView(MyModelView):

    can_create = False
    can_edit = False
    can_delete = False
    list_template = 'admin/custom_list_template.html'
    column_list = (
        'name',
        'group',
        'created_at',
        'updated_at'
    )
    column_labels = dict(
        created_at='Date Created',
        group='Type',
        updated_at='Last Updated',
        )
    column_formatters = dict(
        name=macro('render_entity_name'),
        )
    column_searchable_list = (
        'name',
        'group'
    )
    page_size = 50


class MediumView(MyModelView):

    list_template = 'admin/custom_list_template.html'
    column_labels = dict(
        medium_type='Publication Type',
        )
    column_formatters = dict(
        medium_type=macro('render_medium_type'),
        )
    choices = []
    for choice in ["PRINT", "ONLINE", "TELEVISION", "RADIO", "OTHER"]:
        choices.append((choice, choice.title()))

    form_overrides = dict(medium_type=SelectField)
    form_args = dict(
        # Pass the choices to the `SelectField`
        medium_type=dict(
            choices=choices
        ))

class IndividualView(MyModelView):

    can_create = True
    can_edit = True
    can_delete = False
    list_template = 'admin/custom_list_template.html'
    column_list = (
        'code',
        'name',
    )
    column_searchable_list = (
        'code',
        'name'
    )
    page_size = 100

class UserView(MyModelView):

    can_create = True
    can_edit = True
    can_delete = False
    list_template = 'admin/custom_list_template.html'
    column_list = (
        'email',
        'admin',
    )
    column_searchable_list = (
        'email',
    )
    page_size = 50

    def scaffold_form(self):
        form_class = super(UserView, self).scaffold_form()
        form_class.password = TextField('Change password')
        del form_class.encrypted_password
        del form_class.created_at
        del form_class.updated_at
        return form_class

admin_instance = Admin(url='/admin', base_template='admin/custom_master.html', name="Dexter Admin", index_view=MyIndexView())
admin_instance.add_view(UserView(User, db.session, name="Users", endpoint='user'))
admin_instance.add_view(DocumentView(Document, db.session, name="Articles", endpoint='document'))
admin_instance.add_view(EntityView(Entity, db.session, name="Entities", endpoint='entity'))
admin_instance.add_view(MyModelView(Topic, db.session, name="Article Topics", endpoint="topic"))
admin_instance.add_view(MyModelView(DocumentType, db.session, name="Article Types", endpoint="type"))
admin_instance.add_view(MediumView(Medium, db.session, name="Mediums", endpoint="medium"))
admin_instance.add_view(MyModelView(Fairness, db.session, name="Fairness", endpoint="fairness"))
admin_instance.add_view(IndividualView(Individual, db.session, name="Individuals", endpoint="individuals"))
