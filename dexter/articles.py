import logging
log = logging.getLogger(__name__)

from flask import request, url_for, flash, redirect
from flask.ext.mako import render_template

from .app import app
from .models import db, Document, DocumentIssue, Issue
from .models.document import DocumentForm, DocumentAnalysisForm
from .models.author import AuthorForm

from .processing import DocumentProcessor, ProcessingError

@app.route('/articles/<id>')
def show_article(id):
    document = Document.query.get_or_404(id)
    return render_template('articles/show.haml',
            document=document)
 

@app.route('/articles/new', methods=['GET', 'POST'])
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
            db.session.add(doc)
            db.session.flush()
            id = doc.id
            db.session.commit()
            flash('Article added.')
            return redirect(url_for('edit_article_analysis', id=id))
        
    return render_template('articles/new.haml',
            url=url,
            form=form,
            author_form=author_form)


@app.route('/articles/<id>/edit', methods=['GET', 'POST'])
def edit_article(id):
    doc = Document.query.get_or_404(id)
    form = DocumentForm(obj=doc)

    author_form = AuthorForm(prefix='author', csrf_enabled=False, obj=doc.author)

    if request.method == 'POST':
        if author_form.validate():
            # link author
            form.author_id.data = author_form.get_or_create_author().id
            if form.validate():
                form.populate_obj(doc)
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
def edit_article_analysis(id):
    document = Document.query.get_or_404(id)
    form = DocumentAnalysisForm(obj=document)

    if request.method == 'POST':
        if form.validate():

            # convert issue id's to DocumentIssue objects
            tmp = []
            for issue_id in form.issues.data:
                # doc_issue = DocumentIssue(issue_id=issue_id, doc_id=id)
                issue = Issue.query.get_or_404(issue_id)
                doc_issue = DocumentIssue(issue=issue, document=document)
                tmp.append(doc_issue)
            form.issues.data = tmp

            form.populate_obj(document)

            # TODO: convert from empty values back into None
            if not document.topic_id:
                document.topic_id = None
            if not document.origin_location_id:
                document.origin_location_id = None

            db.session.commit()
            flash('Analysis updated.')
            return redirect(url_for('show_article', id=id))
        else:
            flash('Validation error.')
    else:
        # TODO: wtforms turns None values into None, which sucks
        if form.topic_id.data == 'None':
            form.topic_id.data = ''
        if form.origin_location_id.data == 'None':
            form.origin_location_id.data = ''

    return render_template('articles/edit_analysis.haml',
            form=form,
            document=document)
