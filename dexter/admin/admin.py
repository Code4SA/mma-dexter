from dexter.models import db, Document, Entity, Utterance, Medium
from dexter.models.document import DocumentForm
from flask.ext.admin import Admin, expose, AdminIndexView
from flask import render_template, url_for
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.model.template import macro
from wtforms.fields import SelectField, TextAreaField
import flask_wtf

class MyModelView(ModelView):
    form_base_class = flask_wtf.Form


class MyIndexView(AdminIndexView):

    def __init__(self):
        super(MyIndexView, self).__init__(url="/")

    @expose('/')
    def index(self):
        document_count = Document.query.count()
        date_from = Document.query.order_by(Document.published_at).first().published_at
        date_to = Document.query.order_by(Document.published_at.desc()).first().published_at

        self._template_args['document_count'] = document_count
        self._template_args['date_from'] = date_from
        self._template_args['date_to'] = date_to
        return super(MyIndexView, self).index()


class DocumentView(MyModelView):

    list_template = 'admin/custom_list.html'
    create_template = 'admin/add_document_template.html'
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
    column_sortable_list = (
        'published_at',
        ('medium', Medium.name),
        'title',
        'blurb',
        'updated_at'
    )
    column_formatters = dict(
        medium=macro('render_medium'),
        published_at=macro('render_date'),
        title=macro('render_document_title'),
        updated_at=macro('render_date')
    )
    form_overrides = dict(
        blurb=TextAreaField,
        text=TextAreaField,
    )
    column_searchable_list = (
        'title',
        'blurb',
    )
    page_size = 50


    @expose('/new/', methods=('GET', 'POST'))
    def create_view(self):
        """
            Create model view
        """


        return self.render('admin/add_document.html', return_url=url_for('.index_view'))


class EntityView(MyModelView):

    can_create = False
    list_template = 'admin/custom_list.html'
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


class UtteranceView(MyModelView):

    can_create = False
    list_template = 'admin/custom_list.html'
    column_list = (
        'entity',
        'quote',
        'document',
        'created_at',
        'updated_at'
    )
    column_labels = dict(
        created_at='Date Created',
        updated_at='Last Updated',
    )
    column_formatters = dict(
        entity=macro('render_entity'),
        document=macro('render_document'),
        created_at=macro('render_date'),
        updated_at=macro('render_date')
    )
    column_sortable_list = (
        'created_at',
        ('entity', Entity.name),
        ('document', Document.title),
        'quote',
        'updated_at'
    )
    column_searchable_list = (
        'quote',
    )
    page_size = 50


admin_instance = Admin(url='/', base_template='admin/custom_master.html', name="Dexter", index_view=MyIndexView())
admin_instance.add_view(DocumentView(Document, db.session))
admin_instance.add_view(EntityView(Entity, db.session))
admin_instance.add_view(UtteranceView(Utterance, db.session))
admin_instance.add_view(MyModelView(Medium, db.session))