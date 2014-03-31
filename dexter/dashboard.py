from itertools import groupby

from dexter.app import app
from flask import request, url_for, flash, redirect
from flask.ext.mako import render_template
from flask.ext.login import login_required, current_user
from sqlalchemy.sql import func

from dexter.models import db, Document, Entity, Medium

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


@app.route('/activity')
@login_required
def activity():
    per_page = 100

    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

    paged_docs = Document.query.order_by(Document.created_at.desc()).paginate(page, per_page)

    doc_groups = {}
    for date, group in groupby(paged_docs.items, lambda d: d.created_at.date()):
        doc_groups[date] = list(group)

    return render_template('activity.haml',
                           paged_docs=paged_docs,
                           doc_groups=doc_groups)
