import logging
log = logging.getLogger(__name__)

from flask import request, url_for, flash, redirect
from flask.ext.mako import render_template
from flask.ext.login import login_required, current_user

from .app import app
from .models import db, Document, Issue, Person
from .models.document import DocumentForm, DocumentAnalysisForm
from .models.source import DocumentSource, DocumentSourceForm
from .models.fairness import DocumentFairness, DocumentFairnessForm
from .models.author import AuthorForm

from .processing import DocumentProcessor, ProcessingError

@app.route('/articles/<id>')
@login_required
def show_article(id):
    document = Document.query.get_or_404(id)
    return render_template('articles/show.haml',
            document=document)

@app.route('/articles/<id>/delete', methods=['POST'])
@login_required
def delete_article(id):
    document = Document.query.get_or_404(id)

    if current_user.admin:
        log.info("Document deleted by %s: %s" % (current_user, document))
        db.session.delete(document)
        db.session.commit()
        flash('The document has been deleted.', 'info')

    return redirect(url_for('dashboard'))
 

@app.route('/articles/new', methods=['GET', 'POST'])
@login_required
def new_article():
    form = DocumentForm()
    author_form = AuthorForm(prefix='author', csrf_enabled=False)

    form.url.data = form.url.data or request.args.get('url')
    url = form.url.data

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
                else:
                    try:
                        doc = proc.process_url(url)
                    except ProcessingError as e:
                        log.error("Error processing %s: %s" % (url, e), exc_info=e)
                        flash("Something went wrong processing the document: %s" % (e,), 'error')
        else:
            # new document from article text
            if author_form.validate():
                # link author
                form.author_id.data = author_form.get_or_create_author().id

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
            if current_user.is_authenticated():
                doc.created_by = current_user

            db.session.add(doc)
            db.session.flush()
            id = doc.id
            log.info("Document added by %s: %s" % (current_user, doc))
            db.session.commit()
            flash('Article added.')
            return redirect(url_for('edit_article_analysis', id=id))
        
    return render_template('articles/new.haml',
            url=url,
            form=form,
            author_form=author_form)


@app.route('/articles/<id>/edit', methods=['GET', 'POST'])
@login_required
def edit_article(id):
    doc = Document.query.get_or_404(id)
    if not doc.can_user_edit(current_user):
        flash("You're not allowed to edit this article.", 'error')
        return redirect(url_for('show_article', id=id))

    form = DocumentForm(obj=doc)

    author_form = AuthorForm(prefix='author', csrf_enabled=False, obj=doc.author)

    if request.method == 'POST':
        if author_form.validate():
            # link author
            form.author_id.data = author_form.get_or_create_author().id
            if form.validate():
                form.populate_obj(doc)
                doc.normalise_text()
                db.session.commit()
                flash('Article updated.')
                return redirect(url_for('show_article', id=id))
    else:
        author_form.person_race_id.data = doc.author.person.race.id if doc.author.person and doc.author.person.race else None
        author_form.person_gender_id.data = doc.author.person.gender.id if doc.author.person and doc.author.person.gender else None

    return render_template('articles/edit.haml',
            doc=doc,
            form=form,
            author_form=author_form)

@app.route('/articles/<id>/analysis', methods=['GET', 'POST'])
@login_required
def edit_article_analysis(id):
    document = Document.query.get_or_404(id)

    # can this user do this?
    if not document.can_user_edit(current_user):
        flash("You're not allowed to edit this article.", 'error')
        return redirect(url_for('show_article', id=id))

    form = DocumentAnalysisForm(obj=document)

    # forms for existing sources
    source_forms = []
    for source in document.sources:
        f = DocumentSourceForm(prefix='source[%d]' % source.id, obj=source)
        f.source = source
        source_forms.append(f)
    source_forms.sort(key=lambda f: f.source.sort_key())

    # in the page, the fields for all new sources will be transformed into
    # 'source-new[0]-name'. This form is used as a template for these
    # new source forms.
    new_sources = []
    new_source_form = DocumentSourceForm(prefix='source-new', csrf_enabled=False)

    # fairness forms
    new_fairness_form = DocumentFairnessForm(prefix='fairness-new', csrf_enabled=False)
    new_fairness_form.fairness_id.choices = [['', '(none)']] + new_fairness_form.fairness_id.choices

    fairness_forms = []
    for fairness in document.fairness:
        f = DocumentFairnessForm(prefix='fairness[%d]' % fairness.id, obj=fairness)
        f.document_fairness = fairness
        fairness_forms.append(f)

    if request.method == 'POST':
        # find new sources and build forms for them.
        # the field names are like: source-new[2]-name
        for key in sorted(set('-'.join(key.split('-', 3)[0:2]) for key in request.form.keys() if key.startswith('source-new['))):
            src_form = DocumentSourceForm(prefix=key)
            # skip new sources that have an empty name
            if src_form.source_type.data not in ('person', 'secondary') or src_form.name.data != '':
                new_sources.append(src_form)

        # new fairness
        for key in sorted(set('-'.join(key.split('-', 3)[0:2]) for key in request.form.keys() if key.startswith('fairness-new['))):
            frm = DocumentFairnessForm(prefix=key)
            # skip new fairness that have an empty bias
            if frm.fairness_id.data != '':
                fairness_forms.append(frm)

        forms = [form] + new_sources + source_forms + fairness_forms
        if all(f.validate() for f in forms):
            # convert issue id's to Issue objects
            form.issues.data = [Issue.query.get_or_404(i) for i in form.issues.data]

            # update document
            form.populate_obj(document)

            # update and delete sources
            for f in source_forms + new_sources:
                f.create_or_update(document)

            # update and delete fairness
            for frm in fairness_forms:
                frm.create_or_update(document)

            # link to user
            if current_user.is_authenticated() and not document.checked_by:
                document.checked_by = current_user

            log.info("Updated analysis by %s for %s" % (current_user, document))

            db.session.commit()
            flash('Analysis updated.')
            return redirect(url_for('edit_article_analysis', id=id))
        else:
            flash('Please correct the problems below and try again.')
    else:
        # wtforms turns None values into None, which sucks
        if form.topic_id.data == 'None':
            form.topic_id.data = ''
        if form.origin_location_id.data == 'None':
            form.origin_location_id.data = ''
        # ensure that checkboxes can be pre-populated
        form.issues.data = [str(i.id) for i in document.issues]

    return render_template('articles/edit_analysis.haml',
            form=form,
            source_forms=source_forms,
            new_source_form=new_source_form,
            new_sources=new_sources,
            new_fairness_form=new_fairness_form,
            fairness_forms=fairness_forms,
            document=document)
