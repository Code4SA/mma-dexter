from dexter.models import db, Document, Entity, DocumentEntity, Utterance, Medium
from dexter.models.document import DocumentForm
from dexter.processing import DocumentProcessor, ProcessingError
from flask.ext.admin import Admin, expose, AdminIndexView
from flask import request, render_template, url_for, flash, redirect
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.model.template import macro
from wtforms.fields import SelectField, TextAreaField
import flask_wtf
import logging
log = logging.getLogger(__name__)
from dexter.helpers import format_paragraphs

class MyModelView(ModelView):
    form_base_class = flask_wtf.Form


class MyIndexView(AdminIndexView):

    def __init__(self):
        super(MyIndexView, self).__init__(url="/")

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

        form = DocumentForm()
        url = request.form.get('url')
        log.debug(url)

        if request.method == 'POST':
            doc = None
            proc = DocumentProcessor()

            if url and not 'manual' in request.form:
                # new document from url
                if not proc.valid_url(url):
                    flash("The URL isn't valid or we don't know how to process it.", 'error')
                else:
                    url = proc.canonicalise_url(url)
                    doc = Document.query.filter(Document.url == url).first()

                    if doc:
                        # already exists
                        flash("We already have that article.")
                        return redirect(url_for('show_article', id=doc.id))

                    try:
                        doc = proc.process_url(url)
                    except ProcessingError as e:
                        log.error("Error processing %s: %s" % (url, e), exc_info=e)
                        flash("Something went wrong processing the document: %s" % (e,), 'error')
                        doc = None

            else:
                # new document from article text
                if form.validate():
                    doc = Document()
                    form.populate_obj(doc)

                    try:
                        proc.process_document(doc)
                    except ProcessingError as e:
                        log.error("Error processing raw document: %s" % (e, ), exc_info=e)
                        flash("Something went wrong processing the document: %s" % (e,), 'error')
                        doc = None

            if doc:
                db.session.add(doc)
                db.session.flush()
                id = doc.id
                db.session.commit()
                flash('Article added.')
                return redirect(url_for('show_article', id=id))

        return self.render('admin/add_document.html', return_url=url_for('.index_view'), form=form)

    @expose('/<id>/', methods=('GET',))
    def show_document(self, id):

        document = Document.query.get_or_404(id)
        return self.render('admin/show_document.html', return_url=url_for('.index_view'), document=document, format_paragraphs=format_paragraphs)


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

    @expose('/<string:group>/<string:entity_name>/', methods=('GET',))
    def show_entity(self, group, entity_name):

        entity = Entity.query.filter(Entity.group==group, Entity.name==entity_name).first()

        if not entity:
            return make_response("The specified entity could not be found.", 404)

        documents = Document.query.join(DocumentEntity)\
            .filter(DocumentEntity.entity_id==entity.id)\
            .order_by(Document.published_at.desc()).all()
        return self.render('admin/show_entity.html', return_url=url_for('.index_view'), entity=entity, documents=documents)


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
admin_instance.add_view(DocumentView(Document, db.session, name="Articles", endpoint='document'))
admin_instance.add_view(EntityView(Entity, db.session, name="Entities", endpoint='entity'))
admin_instance.add_view(UtteranceView(Utterance, db.session, name="Quotes", endpoint="utterance"))
admin_instance.add_view(MyModelView(Medium, db.session, name="Sources", endpoint="medium"))