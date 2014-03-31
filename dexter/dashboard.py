from itertools import groupby

from dexter.app import app
from flask import request, url_for, flash, redirect
from flask.ext.mako import render_template
from flask.ext.login import login_required, current_user
from sqlalchemy.sql import func

from dexter.models import db, Document, Entity, Medium, User, DocumentType

from wtforms import validators
from .forms import Form, SelectField

@app.route('/dashboard')
@login_required
def dashboard():
    latest_docs = Document.query.order_by(Document.created_at.desc()).limit(30)

    doc_groups = {}
    for date, group in groupby(latest_docs, lambda d: d.created_at.date()):
        doc_groups[date] = list(group)

    document_count = Document.query.count()
    if document_count is None:
        document_count = 0

    earliest = Document.query.order_by(Document.published_at).first()
    latest = Document.query.order_by(Document.published_at.desc()).first()
    if earliest:
        earliest = earliest.published_at.strftime('%e %B %Y')
    if latest:
        latest = latest.published_at.strftime('%e %B %Y')

    group_counts = {}
    for group_count, group_name in db.session.query(func.count(Entity.id), Entity.group).group_by(Entity.group).all():
        group_counts[group_name] = int(group_count)

    medium_counts = []
    for medium_count, medium_name in db.session.query(func.count(Document.id), Medium.name) \
            .join(Medium) \
            .group_by(Document.medium_id) \
            .order_by(func.count(Document.id).desc()) \
            .limit(5):
        medium_counts.append([medium_name, int(medium_count)])

    return render_template('dashboard.haml',
                           doc_groups=doc_groups,
                           document_count=document_count,
                           latest=latest,
                           earliest=earliest,
                           group_counts=group_counts,
                           medium_counts=medium_counts)


@app.route('/activity', methods=['GET', 'POST'])
@login_required
def activity():
    per_page = 100

    form = ActivityForm()

    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

    query = Document.query

    if form.medium_id.data:
        query = query.filter(Document.medium_id == form.medium_id.data)

    if form.user_id.data:
        query = query.filter(Document.checked_by_user_id == form.user_id.data)

    if form.document_type_id.data:
        query = query.filter(Document.document_type_id == form.document_type_id.data)
    
    paged_docs = query.order_by(Document.created_at.desc()).paginate(page, per_page)

    doc_groups = {}
    for date, group in groupby(paged_docs.items, lambda d: d.created_at.date()):
        doc_groups[date] = list(group)

    return render_template('activity.haml',
                           form=form,
                           paged_docs=paged_docs,
                           doc_groups=doc_groups)


class ActivityForm(Form):
    user_id     = SelectField('User', [validators.Optional()], default='')
    medium_id   = SelectField('Medium', [validators.Optional()], default='')
    document_type_id = SelectField('Document type', [validators.Optional()], default='')

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)

        self.user_id.choices = [['', '(none)']] + [
                [str(u.id), u.short_name()] for u in sorted(User.query.all(), key=lambda u: u.short_name())]

        self.medium_id.choices = [['', '(none)']] + [(str(m.id), m.name) for m in Medium.query.order_by(Medium.name).all()]
        self.document_type_id.choices = [['', '(none)']] + [(str(dt.id), dt.name) for dt in DocumentType.query.order_by(DocumentType.name).all()]
