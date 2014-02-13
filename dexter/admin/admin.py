from dexter.models import db, Document, Entity, Utterance, Medium
from flask.ext.admin import Admin, expose, AdminIndexView
from flask import render_template
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.model.template import macro
from wtforms.fields import SelectField, TextAreaField
import flask_wtf

class MyModelView(ModelView):
    form_base_class = flask_wtf.Form


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
        tmp = db.session.query(db.func.count(Document.id), Medium.name)\
            .join(Medium)\
            .group_by(Document.medium_id)\
            .order_by(db.func.count(Document.id))\
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


class UtteranceView(MyModelView):

    can_create = False
    can_edit = False
    can_delete = False
    list_template = 'admin/custom_list_template.html'
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


class MediumView(MyModelView):

    can_create = False
    can_edit = False
    can_delete = False
    page_size = 50


admin_instance = Admin(url='/admin', base_template='admin/custom_master.html', name="Dexter", index_view=MyIndexView())
admin_instance.add_view(DocumentView(Document, db.session, name="Articles", endpoint='document'))
admin_instance.add_view(EntityView(Entity, db.session, name="Entities", endpoint='entity'))
admin_instance.add_view(UtteranceView(Utterance, db.session, name="Quotes", endpoint="utterance"))
admin_instance.add_view(MediumView(Medium, db.session, name="Sources", endpoint="medium"))
