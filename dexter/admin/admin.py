from flask.ext.admin import Admin, expose, AdminIndexView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.model.template import macro
from wtforms.fields import SelectField, TextAreaField, TextField, HiddenField
from flask import abort
import flask_wtf
from flask.ext.security import current_user

from sqlalchemy import desc, func

from dexter.models import *
from ..forms import Form

class MyModelView(ModelView):
    form_base_class = Form
    can_create = True
    can_edit = True
    can_delete = False
    page_size = 50

    def is_accessible(self):
        return current_user.is_authenticated() and current_user.admin


class MyIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not (current_user.is_authenticated() and current_user.admin):
            abort(403)
        return super(MyIndexView, self).index()

class DocumentView(MyModelView):
    can_create = False
    can_edit = False
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


class EntityView(MyModelView):
    can_create = False
    can_edit = False
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


class MediumView(MyModelView):
    column_list = (
        'name',
        'domain',
        'medium_type',
        'medium_group',
        'parent_org',
        'country',
    )
    column_labels = dict(
        medium_type='Publication Type',
        )
    column_searchable_list = (
        'name',
        'parent_org'
    )
    column_default_sort = 'name'
    column_formatters = dict(
        medium_type=macro('render_medium_type'),
    )
    column_sortable_list = (
        ('name', Medium.name),
        'domain',
        'medium_type',
        'medium_group',
        ('country', Country.name),
    )
    column_filters = ['country.name']

    choices = []
    for choice in ["online", "print - daily", "print - weekly", "radio", "television", "other"]:
        choices.append((choice, choice.title()))

    form_overrides = dict(medium_type=SelectField)
    form_args = dict(
        # Pass the choices to the `SelectField`
        medium_type=dict(
            choices=choices
        ),
        domain=dict(filters=[lambda x: x or None])
      )

class AffiliationView(MyModelView):
    column_list = (
        'code',
        'name',
        'country',
    )
    column_searchable_list = (
        'code',
        'name',
    )
    column_sortable_list = (
        ('code', Affiliation.code),
        ('name', Affiliation.name),
        ('country', Country.name),
    )
    column_filters = ['country.name']
    column_default_sort = ('code', False)
    page_size = 100

    def _order_by(self, query, joins, sort_joins, sort_field, sort_desc):
        query, joins = super(AffiliationView, self)._order_by(query, joins, sort_joins, sort_field, sort_desc)

        if sort_field.name == 'code':
            # sort by the code field, which has entries like:
            # 1
            # 1.1
            # 1.2
            # 1.10
            # 1.11
            # 10.1
            #
            # these are hard to sort, because they don't sort correctly
            # numerically or lexicographically. Instead, we treat them
            # as parts of dotted-quad IP addresses and use mysql's inet_aton
            # to sort them.

            sort_field = func.inet_aton(
                    func.if_(func.instr(sort_field, '.') > 0,
                        func.concat(sort_field, '.0.0'),     # eg. 10.2
                        func.concat(sort_field, '.0.0.0')))  # eg. 10

            if sort_desc:
                sort_field = desc(sort_field)
            query = query.order_by(None).order_by(sort_field)

        return query, joins


class IssueView(MyModelView):
    column_list = (
        'name',
        'description',
    )
    column_searchable_list = (
        'name',
    )
    page_size = 100
    form_create_rules = ('name', 'description')
    form_edit_rules = ('name', 'description')

class TopicView(MyModelView):
    column_searchable_list = ('name', 'group')
    column_sortable_list = (
        'name',
        'group',
        ('analysis_nature', AnalysisNature.name),
        )
    column_filters = ['analysis_nature.name']


class LocationView(MyModelView):
    column_list = ('name', 'group', 'country')
    column_sortable_list = (
        ('name', Location.name),
        ('group', Location.group),
        ('country', Country.name),
    )
    column_filters = ['country.name']


class SourceRoleView(MyModelView):
    column_sortable_list = (
        ('name', SourceRole.name),
        'indication',
        ('analysis_nature', AnalysisNature.name),
    )
    column_filters = ['analysis_nature.name']


class CountryView(MyModelView):
    def scaffold_form(self):
        form_class = super(MyModelView, self).scaffold_form()
        del form_class.mediums
        return form_class

class UserView(MyModelView):
    column_list = (
        'first_name',
        'last_name',
        'email',
        'country',
        'disabled',
        'admin',
    )
    column_searchable_list = ('first_name', 'last_name', 'email')
    column_filters = ['country.name']

    form_columns = [
        'email',
        'first_name',
        'last_name',
        'country',
        'disabled',
        'roles',
        'admin',
        'default_analysis_nature',
    ]


admin_instance = Admin(url='/admin', base_template='admin/custom_master.html', name="Dexter Admin", index_view=MyIndexView(), template_mode='bootstrap3')
admin_instance.add_view(UserView(User, db.session, name="Users", endpoint='user'))
admin_instance.add_view(CountryView(Country, db.session, name="Countries", endpoint='country'))

admin_instance.add_view(MediumView(Medium, db.session, name="Media", endpoint="medium", category='Article Information'))
admin_instance.add_view(MyModelView(DocumentType, db.session, name="Types", endpoint="type", category='Article Information'))
admin_instance.add_view(TopicView(Topic, db.session, name="Topics", endpoint="topic", category='Article Information'))
admin_instance.add_view(LocationView(Location, db.session, name="Origins", endpoint="origins", category='Article Information'))
admin_instance.add_view(EntityView(Entity, db.session, name="Entities", endpoint='entity', category='Article Information'))
admin_instance.add_view(IssueView(Issue, db.session, name="Issues", endpoint="issues", category='Article Information'))
admin_instance.add_view(MyModelView(Fairness, db.session, name="Bias", endpoint="bias", category='Article Information'))
admin_instance.add_view(MyModelView(Principle, db.session, name="Principles", endpoint="principles", category='Article Information'))

admin_instance.add_view(MyModelView(SourceFunction, db.session, name="Functions", endpoint='functions', category='Source Information'))
admin_instance.add_view(AffiliationView(Affiliation, db.session, name="Affiliations", endpoint="affiliations", category='Source Information'))
admin_instance.add_view(MyModelView(AuthorType, db.session, name="Authors", endpoint="authortypes", category='Source Information'))
admin_instance.add_view(MyModelView(SourceAge, db.session, name="Ages", endpoint="ages", category='Source Information'))
admin_instance.add_view(SourceRoleView(SourceRole, db.session, name="Roles", endpoint="roles", category='Source Information'))
