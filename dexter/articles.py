import logging
import os

from flask import request, url_for, flash, redirect, make_response, jsonify
from flask.ext.mako import render_template
from flask.ext.login import login_required, current_user

from werkzeug.exceptions import Forbidden, NotAcceptable
from wand.exceptions import WandError

from .app import app
from .models import db, Document, Issue, Person, DocumentPlace, DocumentAttachment
from .models.document import DocumentForm
from .models.source import DocumentSource, DocumentSourceForm
from .models.fairness import DocumentFairness, DocumentFairnessForm
from .models.analysis_nature import AnalysisNature
from .models.author import AuthorForm

from .processing import DocumentProcessor, ProcessingError

log = logging.getLogger(__name__)

@app.route('/articles/<id>')
@login_required
def show_article(id):
    document = Document.query.get_or_404(id)

    if request.args.get('format') == 'places-json':
        return jsonify(DocumentPlace.summary_for_docs([document]))

    return render_template('articles/show.haml',
            document=document)

@app.route('/articles/<id>/delete', methods=['POST'])
@login_required
def delete_article(id):
    document = Document.query.get_or_404(id)

    if not document.can_user_edit(current_user):
        flash("You're not allowed to delete this article.", 'error')
        return redirect(url_for('show_article', id=id))

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
                        doc.analysis_nature_id = form.analysis_nature_id.data
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
                    form.populate_obj(doc, request.form.getlist('attachments'))

                    db.session.add(doc)
                    db.session.flush()

                    try:
                        proc.process_document(doc)
                    except ProcessingError as e:
                        log.error("Error processing raw document: %s" % (e, ), exc_info=e)
                        flash("Something went wrong processing the document: %s" % (e,), 'error')
                        doc = None

        if doc:
            if current_user.is_authenticated():
                doc.created_by = current_user
                # change analysis default for this user
                current_user.default_analysis_nature_id = doc.analysis_nature_id

                # enforce a country
                if doc.country is None:
                    doc.country = current_user.country

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
                form.populate_obj(doc, request.form.getlist('attachments'))
                doc.normalise_text()

                db.session.commit()
                flash('Article updated.')
                return redirect(url_for('show_article', id=id))

    else:
        author_form.person_race_id.data = doc.author.person.race.id if doc.author.person and doc.author.person.race else None
        author_form.person_gender_id.data = doc.author.person.gender.id if doc.author.person and doc.author.person.gender else None

    return render_template('articles/edit.haml',
            document=doc,
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

    if request.args.get('format') == 'places-json':
        return jsonify(DocumentPlace.summary_for_docs([document]))

    status = 200
    form = document.make_analysis_form()
    nature = document.analysis_nature

    # forms for existing sources
    source_forms = []
    for source in document.sources:
        f = DocumentSourceForm(prefix='source[%d]' % source.id, obj=source)
        source_forms.append(f)
    source_forms.sort(key=lambda f: f.source.sort_key())

    # in the page, the fields for all new sources will be transformed into
    # 'source-new[0]-name'. This form is used as a template for these
    # new source forms.
    new_sources = []
    new_source_form = DocumentSourceForm(prefix='source-new', csrf_enabled=False, nature=nature, country=document.country)

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
            src_form = DocumentSourceForm(prefix=key, nature=nature, country=document.country)
            # skip new sources that have an empty name but aren't anonymous
            if not src_form.named.data or src_form.name.data:
                new_sources.append(src_form)

        # new fairness
        for key in sorted(set('-'.join(key.split('-', 3)[0:2]) for key in request.form.keys() if key.startswith('fairness-new['))):
            frm = DocumentFairnessForm(prefix=key)
            # skip new fairness that have an empty bias
            if frm.fairness_id.data != '':
                fairness_forms.append(frm)

        forms = [form] + new_sources + source_forms + fairness_forms
        if all(f.validate() for f in forms):
            if nature != AnalysisNature.SIMPLE:
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

            # XXX - the document analysis forms only update the *_id attributes,
            # no the association attribute, but we need that updated for the functionality
            # below. So, run it after the commit. It sucks that we don't do this all
            # in one transaction. We should use a different form mechanism
            # that updates everything
            document.relearn_source_affiliations()
            db.session.commit()

            flash('Analysis updated.')

            # if it's an ajax request, we're just going to return a 200
            if not request.is_xhr:
                return redirect(url_for('edit_article_analysis', id=id))

            status = 200
        else:
            if request.is_xhr:
                status = 412
            else:
                flash('Please correct the problems below and try again.', 'warning')
    else:
        if nature != AnalysisNature.SIMPLE:
            # wtforms turns None values into None, which sucks
            if form.topic_id.data == 'None':
                form.topic_id.data = ''
            if form.origin_location_id.data == 'None':
                form.origin_location_id.data = ''
            # ensure that checkboxes can be pre-populated
            form.issues.data = [str(i.id) for i in document.issues]

    # only render if it's not an ajax request
    if not request.is_xhr:
        resp = make_response(render_template('articles/edit_analysis.haml',
            form=form,
            source_forms=source_forms,
            new_source_form=new_source_form,
            new_sources=new_sources,
            new_fairness_form=new_fairness_form,
            fairness_forms=fairness_forms,
            document=document,
            natures=AnalysisNature.all()))
    else:
        resp = ''

    return (resp, status,
            # ensure the browser refreshes the page when Back is pressed
            {'Cache-Control': 'no-cache, no-store, must-revalidate'})

@app.route('/articles/<id>/analysis/nature', methods=['POST'])
@login_required
def edit_article_analysis_nature(id):
    document = Document.query.get_or_404(id)

    # can this user do this?
    if not document.can_user_edit(current_user):
        flash("You're not allowed to edit this article.", 'error')
        return redirect(url_for('show_article', id=id))

    nature = AnalysisNature.lookup(request.args.get('nature', ''))
    if nature:
        document.analysis_nature = nature

        # change default for this user
        if current_user.is_authenticated():
            current_user.default_analysis_nature = nature

        db.session.commit()

    return redirect(url_for('edit_article_analysis', id=id))


@app.route('/articles/attachments', methods=['POST'])
@login_required
def create_article_attachment():
    try:
        if 'file' in request.files:
            upload = request.files['file']

            if not DocumentAttachment.is_acceptable(upload):
                raise ValueError('Only image and PDF attachments are supported')

            try:
                attachment = DocumentAttachment.from_upload(upload, current_user)
            except WandError as e:
                log.warn("Couldn't process attachment: %s, %s: %s" % (upload.mimetype, upload.filename, e.message), exc_info=e)
                raise ValueError('Only image and PDF attachments are supported')

            db.session.add(attachment)
            db.session.commit()

            return jsonify({'attachment': attachment.to_json()})

        raise ValueError("Need a file attachment")
    except ValueError as e:
        return (make_response(e.message), 400, [])
