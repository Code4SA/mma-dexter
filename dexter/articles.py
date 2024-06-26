import logging

from flask import request, url_for, flash, redirect, make_response, jsonify, abort, session
from flask.ext.mako import render_template
from flask.ext.security import roles_accepted, current_user, login_required

from wand.exceptions import WandError

from .app import app
from .models import db, Document, Issue, DocumentPlace, DocumentAttachment, DocumentTag, Investment, Phases, Sectors, \
    InvestmentOrigins, InvestmentType, Currencies, Industries, Involvements1, Involvements2, Involvements3, \
    ValueUnits, Provinces
from .models.document import DocumentForm
from .models.fairness import DocumentFairnessForm
from .models.analysis_nature import AnalysisNature
from .models.author import AuthorForm
from .analysis.forms import DocumentSourceForm, FDIAnalysisForm

from sqlalchemy.orm.util import has_identity

from .processing import DocumentProcessor, ProcessingError
from .processing.extractors.calais import CalaisExtractor

log = logging.getLogger(__name__)


@app.route('/articles/<id>')
@app.route('/articles/<id>/<fdi_id>')
@login_required
@roles_accepted('monitor', 'fdi')
def show_article(id, fdi_id=None):
    document = Document.query.get_or_404(id)
    if request.args.get('format') == 'places-json':
        return jsonify(DocumentPlace.summary_for_docs([document]))

    try:
        URL = session[str(current_user.id)]['search']
    except:
        URL = url_for('activity')

    if current_user.has_role('fdi'):

        exists = Investment.query.filter_by(doc_id=id).first() is not None

        if not exists:
            return render_template('fdi/edit_analysis.haml', create=0, document=document, natures=AnalysisNature.all(),
                                   URL=URL)
        elif exists and fdi_id:
            investment = Investment.query.filter_by(id=fdi_id).first()

            # if Involvements1.query.filter_by(id=investment.involvement_id1).first() is None:
            #     investment.involvement_id1 = 5
            #     db.session.commit()
            # if Involvements2.query.filter_by(id=investment.involvement_id2).first() is None:
            #     investment.involvement_id2 = 73
            #     db.session.commit()
            # if Involvements3.query.filter_by(id=investment.involvement_id3).first() is None:
            #     investment.involvement_id3 = 19
            #     db.session.commit()
            # if Provinces.query.filter_by(id=investment.province_id).first() is None:
            #     investment.province_id = 10
            #     db.session.commit()
            # if Industries.query.filter_by(id=investment.industry_id).first() is None:
            #     investment.industry_id = 12
            #     db.session.commit()

            if ValueUnits.query.filter_by(id=investment.value_unit_id).first() is None:
                investment.value_unit_id = 3
                db.session.commit()

            if ValueUnits.query.filter_by(id=investment.value_unit_id2).first() is None:
                investment.value_unit_id2 = 3
                db.session.commit()

            phase = Phases.query.filter_by(id=investment.phase_id).first()
            sector = ' | '.join([Sectors.query.filter_by(id=ind).first().name for ind in
                                 investment.sector_id.split(';') if ind])
            involvement_tier1 = ' | '.join([Involvements1.query.filter_by(id=inv1_id).first().name for inv1_id in
                                            investment.involvement_id1.split(';') if inv1_id])
            involvement_tier2 = ' | '.join([Involvements2.query.filter_by(id=inv2_id).first().name for inv2_id in
                                            investment.involvement_id2.split(';') if inv2_id])
            involvement_tier3 = ' | '.join([Involvements3.query.filter_by(id=inv3_id).first().name for inv3_id in
                                            investment.involvement_id3.split(';') if inv3_id])
            industry = ' | '.join([Industries.query.filter_by(id=ind).first().name for ind in
                                   investment.industry_id.split(';') if ind])
            inv_origin = ' | '.join([InvestmentOrigins.query.filter_by(id=ind).first().name for ind in
                                     investment.invest_origin_id.split(';') if ind])
            province = ' | '.join([Provinces.query.filter_by(id=ind).first().name for ind in
                                   investment.province_id.split(';') if ind])
            target_market = ' | '.join([c for c in investment.target_market.split(';') if ind])
            inv_type = InvestmentType.query.filter_by(id=investment.invest_type_id).first()
            currency = Currencies.query.filter_by(id=investment.currency_id).first()
            value_unit = ValueUnits.query.filter_by(id=investment.value_unit_id).first()
            value_unit2 = ValueUnits.query.filter_by(id=investment.value_unit_id2).first()

            return render_template('fdi/show.haml', investment=investment, document=document, phase=phase.name,
                                   sector=sector, inv_origin=inv_origin, inv_type=inv_type.name,
                                   currency=currency.name, involvement1=involvement_tier1,
                                   involvement2=involvement_tier2,
                                   involvement3=involvement_tier3, industry=industry,
                                   value_unit=value_unit.name, target_market=target_market,
                                   value_unit2=value_unit2.name, province=province, URL=URL)
        else:
            investments = Investment.query.filter_by(doc_id=id)
            return render_template('fdi/edit_analysis.haml', create=1, document=document, investments=investments,
                                   natures=AnalysisNature.all(), URL=URL)

    return render_template('articles/show.haml', document=document, URL=URL)


@app.route('/articles/<id>/delete', methods=['POST'])
@login_required
@roles_accepted('monitor')
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
@roles_accepted('monitor')
def new_article():
    form = DocumentForm()
    author_form = AuthorForm(prefix='author', csrf_enabled=False)

    form.url.data = form.url.data or request.args.get('url')
    url = form.url.data

    if request.method == 'POST':
        doc = None
        proc = DocumentProcessor()

        if url and 'manual' not in request.form:
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
                        log.error("Error processing raw document: %s" % (e,), exc_info=e)
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
@roles_accepted('monitor', 'fdi')
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


@app.route('/articles/<id>/fdi_create')
@login_required
@roles_accepted('monitor', 'fdi')
def fdi_create(id):
    investment = Investment()
    investment.name = ''
    investment.target_market = ''
    investment.value = 0
    investment.value2 = 0
    investment.temp_opps = 0
    investment.perm_opps = 0
    investment.government = ''
    investment.company = ''
    investment.additional_place = ''
    investment.gov_programs = ''
    investment.soc_programs = ''
    investment.mot_investment = ''
    investment.currency_id = 165
    investment.invest_type_id = 6
    investment.phase_id = 6
    investment.invest_origin_id = ''
    investment.invest_origin_city = ''
    investment.province_id = ''
    investment.sector_id = ''
    investment.industry_id = ''
    investment.involvement_id1 = ''
    investment.involvement_id2 = ''
    investment.involvement_id3 = ''
    investment.doc_id = id
    investment.value_unit_id = 3
    investment.value_unit_id2 = 3
    investment.constraints_barriers = ''
    investment.credibility_grading = ''
    investment.grading_notes = ''
    db.session.add(investment)
    db.session.commit()

    return redirect(url_for('edit_article_analysis', id=id, fdi_id=investment.id))


@app.route('/articles/<id>/analysis', methods=['GET', 'POST'])
@app.route('/articles/<id>/<fdi_id>/analysis', methods=['GET', 'POST'])
@login_required
@roles_accepted('monitor', 'fdi')
def edit_article_analysis(id, fdi_id=None):
    document = Document.query.get_or_404(id)

    try:
        URL = session[str(current_user.id)]['search']
    except:
        URL = url_for('activity')

    if current_user.has_role('fdi'):
        investment = Investment.query.filter_by(id=fdi_id).first()

        fdi_form = FDIAnalysisForm(prefix='fdi-new', csrf_enabled=True, obj=investment)

    # can this user do this?
    if not document.can_user_edit(current_user):
        flash("You're not allowed to edit this article.", 'error')
        return redirect(url_for('show_article', id=id, fdi_id=fdi_id))

    if request.args.get('format') == 'places-json':
        return jsonify(DocumentPlace.summary_for_docs([document]))

    status = 200
    form = document.make_analysis_form()

    new_source_form = DocumentSourceForm(prefix='sources-new', csrf_enabled=False, document=document)

    # fairness forms
    new_fairness_form = DocumentFairnessForm(prefix='fairness-new', csrf_enabled=False)
    new_fairness_form.fairness_id.choices = [['', '(none)']] + new_fairness_form.fairness_id.choices

    fairness_forms = []
    for fairness in document.fairness:
        f = DocumentFairnessForm(prefix='fairness[%d]' % fairness.id, obj=fairness)
        f.document_fairness = fairness
        fairness_forms.append(f)

    if request.method == 'POST':

        if current_user.has_role('fdi'):

            forms = [fdi_form]
            if all(f.validate() for f in forms):
                if len(fdi_form.name.data) == 0 and len(fdi_form.name_existing.data) != 0:
                    fdi_form.name.data = fdi_form.name_existing.data
                fdi_form.involvement_id1.data = ';'.join(fdi_form.involvement_id1.data)
                fdi_form.involvement_id2.data = ';'.join(fdi_form.involvement_id2.data)
                fdi_form.involvement_id3.data = ';'.join(fdi_form.involvement_id3.data)
                fdi_form.sector_id.data = ';'.join(fdi_form.sector_id.data)
                fdi_form.industry_id.data = ';'.join(fdi_form.industry_id.data)
                fdi_form.province_id.data = ';'.join(fdi_form.province_id.data)
                fdi_form.invest_origin_id.data = ';'.join(fdi_form.invest_origin_id.data)
                fdi_form.target_market.data = ';'.join(fdi_form.target_market.data)

                with db.session.no_autoflush:
                    fdi_form.populate_obj(investment)

                if current_user.is_authenticated() and not document.checked_by:
                    document.checked_by = current_user

                log.info("Updated analysis by %s for %s" % (current_user, document))
                db.session.commit()

                flash('Analysis updated.')

                if not request.is_xhr:
                    return redirect(url_for('edit_article_analysis', id=id, fdi_id=fdi_id))

                status = 200
            else:
                if request.is_xhr:
                    status = 412
                else:
                    flash('Please correct the problems below and try again.', 'warning')

        else:
            form.sources.entries = [e for e in form.sources.entries
                                    if not e.form.is_deleted() and not e.form.is_empty()]

            # new fairness
            for key in sorted(set('-'.join(key.split('-', 3)[0:2]) for key in request.form.keys() if
                                  key.startswith('fairness-new['))):
                frm = DocumentFairnessForm(prefix=key)
                # skip new fairness that have an empty bias
                if frm.fairness_id.data != '':
                    fairness_forms.append(frm)

            forms = [form] + fairness_forms

            if all(f.validate() for f in forms):
                # convert issue id's to Issue objects
                form.issues.data = [Issue.query.get_or_404(i) for i in form.issues.data]

                # update document -- no_autoflush seems to be required with wtforms alchemy
                with db.session.no_autoflush:
                    form.populate_obj(document)
                    document.dedup_sources()

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
                    return redirect(url_for('edit_article_analysis', id=id, fdi_id=fdi_id))

                status = 200
            else:
                if request.is_xhr:
                    status = 412
                else:
                    flash('Please correct the problems below and try again.', 'warning')
    else:
        if current_user.has_role('fdi'):
            t2_options = {1: range(1, 48) + [73], 2: range(48, 57) + [73], 3: range(57, 65) + [73],
                          4: range(65, 73) + [73],
                          5: [73]}
            t3_options = {9: [1, 19], 33: [2, 19], 48: [3, 19], 49: [4, 19], 50: [5, 6, 7, 19], 51: [8, 9, 19],
                          52: [10, 11, 19], 53: [12, 19], 54: [13, 19],
                          55: [14, 19], 56: [15, 19], 57: [16, 19], 58: [17, 19], 59: [18, 19], 73: [19]}

            # if fdi_form.involvement_id1.data is not None:
            #     if int(fdi_form.involvement_id1.data) in t2_options.keys():
            #         fdi_form.involvement_id2.choices = [[str(c.id), c.name] for c in Involvements2.query.filter(Involvements2.id.in_(t2_options[int(fdi_form.involvement_id1.data)])).all()]
            #     else:
            #         fdi_form.involvement_id2.choices = [["73", "unspecified"]]
            # else:
            #     fdi_form.involvement_id2.choices = [["73", "unspecified"]]
            #
            # if fdi_form.involvement_id2.data is not None:
            #     if int(fdi_form.involvement_id2.data) in t3_options.keys():
            #         fdi_form.involvement_id3.choices = [[str(c.id), c.name] for c in Involvements3.query.filter(Involvements3.id.in_(t3_options[int(fdi_form.involvement_id2.data)])).all()]
            #     else:
            #         fdi_form.involvement_id3.choices = [["19", "unspecified"]]
            # else:
            #     fdi_form.involvement_id3.choices = [["19", "unspecified"]]

        # wtforms turns None values into None, which sucks

        if form.topic_id.data == 'None':
            form.topic_id.data = ''
        if form.origin_location_id.data == 'None':
            form.origin_location_id.data = ''
        # ensure that checkboxes can be pre-populated
        form.issues.data = [str(i.id) for i in document.issues]

    # only render if it's not an ajax request
    if not request.is_xhr:
        if current_user.has_role('fdi'):
            resp = make_response(
                render_template('fdi/edit_analysis.haml',
                                fdi_form=fdi_form,
                                fdi_id=fdi_id,
                                document=document,
                                investment=investment,
                                natures=AnalysisNature.all(),
                                URL=URL))
        else:
            resp = make_response(
                render_template('articles/edit_analysis.haml',
                                form=form,
                                new_source_form=new_source_form,
                                new_fairness_form=new_fairness_form,
                                fairness_forms=fairness_forms,
                                document=document,
                                natures=AnalysisNature.all(),
                                URL=URL))
    else:
        resp = ''

    return (resp, status,
            # ensure the browser refreshes the page when Back is pressed
            {'Cache-Control': 'no-cache, no-store, must-revalidate'})


@app.route('/articles/<id>/analysis/nature', methods=['POST'])
@login_required
@roles_accepted('monitor')
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


@app.route('/articles/<id>/analysis/reprocess', methods=['POST'])
@login_required
@roles_accepted('monitor')
def reprocess_article_analysis(id):
    """ Trigger a reprocessing of some aspect of the article's
    analysis, provided as the +aspect+ parameter.
    """
    document = Document.query.get_or_404(id)

    # can this user do this?
    if not document.can_user_edit(current_user):
        flash("You're not allowed to edit this article.", 'error')
        return redirect(url_for('show_article', id=id))

    aspect = request.args.get('aspect')
    if aspect == 'taxonomy':
        document.taxonomies = []
        db.session.flush()

        cx = CalaisExtractor()
        calais = cx.fetch_data(document)
        cx.extract_topics(document, calais)

        db.session.commit()
        flash('Topics updated')
    else:
        abort(400, "Must supply a valid aspect parameter")

    return redirect(url_for('edit_article_analysis', id=id))


@app.route('/articles/attachments', methods=['POST'])
@login_required
@roles_accepted('monitor')
def create_article_attachment():
    try:
        if 'file' in request.files:
            upload = request.files['file']

            if not DocumentAttachment.is_acceptable(upload):
                raise ValueError('Only image and PDF attachments are supported')

            try:
                attachment = DocumentAttachment.from_upload(upload, current_user)
            except WandError as e:
                log.warn("Couldn't process attachment: %s, %s: %s" % (upload.mimetype, upload.filename, e.message),
                         exc_info=e)
                raise ValueError('Only image and PDF attachments are supported')

            db.session.add(attachment)
            db.session.commit()

            return jsonify({'attachment': attachment.to_json()})

        raise ValueError("Need a file attachment")
    except ValueError as e:
        return (make_response(e.message), 400, [])


@app.route('/articles/add-tag', methods=['POST'])
@login_required
@roles_accepted('monitor', 'fdi')
def add_article_tags():
    tags = DocumentTag.split(request.form.get('tag', '').strip())
    doc_ids = DocumentTag.split(request.form.get('doc_ids', ''))
    docs = Document.query.filter(Document.id.in_(doc_ids))

    if tags and tags:
        for doc in docs:
            for tag in tags:
                doc.tags.add(tag)
    db.session.commit()
    return '', 200


@app.route('/articles/remove-tag', methods=['POST'])
@login_required
@roles_accepted('monitor', 'fdi')
def remove_article_tags():
    tags = DocumentTag.split(request.form.get('tag', '').strip())
    doc_ids = DocumentTag.split(request.form.get('doc_ids', ''))
    docs = Document.query.filter(Document.id.in_(doc_ids))

    if tags and tags:
        for doc in docs:
            for tag in tags:
                doc.tags.discard(tag)
    db.session.commit()
    return '', 200
