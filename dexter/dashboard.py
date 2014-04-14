from itertools import groupby
from datetime import datetime, timedelta

from dexter.app import app
from flask import request, url_for, flash, redirect, make_response
from flask.ext.mako import render_template
from flask.ext.login import login_required, current_user
from sqlalchemy.sql import func

from dexter.models import db, Document, Entity, Medium, User
from dexter.models.document import DocumentsView

from wtforms import validators, HiddenField
from wtforms.fields.html5 import DateField
from .forms import Form, SelectField

@app.route('/dashboard')
@login_required
def dashboard():
    latest_docs = Document.query.order_by(Document.created_at.desc()).limit(30)

    doc_groups = []
    for date, group in groupby(latest_docs, lambda d: d.created_at.date()):
        doc_groups.append([date, list(group)])

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

    return render_template('dashboard/dashboard.haml',
                           doc_groups=doc_groups,
                           document_count=document_count,
                           latest=latest,
                           earliest=earliest,
                           group_counts=group_counts,
                           medium_counts=medium_counts)


@app.route('/monitor-dashboard')
@login_required
def monitor_dashboard():
    docs = Document.query.filter(Document.created_by_user_id == current_user.id).order_by(Document.created_at.desc()).limit(30)

    doc_groups = []
    for date, group in groupby(docs, lambda d: d.created_at.date()):
        doc_groups.append([date, list(group)])

    return render_template('dashboard/monitor.haml',
                           doc_groups=doc_groups)



@app.route('/activity')
@login_required
def activity():
    per_page = 100

    form = ActivityForm(request.args)

    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

    if form.format.data == 'csv':
        # return csv
        query = db.session.query(DocumentsView)\
            .join(Document)
    else:
        query = Document.query


    if form.medium_id.data:
        query = query.filter(Document.medium_id == form.medium_id.data)

    if form.user_id.data:
        query = query.filter(Document.created_by_user_id == form.user_id.data)

    if form.created_from.data:
        query = query.filter(Document.created_at >= form.created_from.data)

    if form.created_to.data:
        query = query.filter(Document.created_at <= form.created_to.data)

    if form.format.data == 'csv':
        # return csv
        body = []
        keys = None
        for row in query.all():
            if not keys:
                keys = row.keys()
                body.append(';'.join(keys))
            body.append(u';'.join('"%s"' % (unicode(x) if x is not None else '',) for x in row))

        response = make_response(u"\r\n".join(body).encode('utf-8'))

        filename = ['activity']
        if form.created_from.data:
            filename.append(form.created_from.data.strftime("%Y-%m-%d"))
        if form.created_to.data:
            filename.append(form.created_to.data.strftime("%Y-%m-%d"))

        response.headers["Content-Disposition"] = "attachment; filename=%s.csv" % '-'.join(filename)

        return response

        
    paged_docs = query.order_by(Document.created_at.desc()).paginate(page, per_page)

    doc_groups = []
    for date, group in groupby(paged_docs.items, lambda d: d.created_at.date()):
        doc_groups.append([date, list(group)])

    return render_template('dashboard/activity.haml',
                           form=form,
                           paged_docs=paged_docs,
                           doc_groups=doc_groups)


class ActivityForm(Form):
    user_id     = SelectField('User', [validators.Optional()], default='')
    medium_id   = SelectField('Medium', [validators.Optional()], default='') 
    created_from   = DateField('Created on or after', [validators.Optional()], default=lambda: datetime.utcnow() - timedelta(days=14))
    created_to     = DateField('Created on or before', [validators.Optional()], default=lambda: datetime.utcnow())
    format         = HiddenField('format', default='html') 

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)

        self.user_id.choices = [['', '(any)']] + [
                [str(u.id), u.short_name()] for u in sorted(User.query.all(), key=lambda u: u.short_name())]

        self.medium_id.choices = [['', '(any)']] + [(str(m.id), m.name) for m in Medium.query.order_by(Medium.name).all()]


    def user(self):
        if self.user_id.data:
            return User.query.get(self.user_id.data)
        return None

    def medium(self):
        if self.medium_id.data:
            return Medium.query.get(self.medium_id.data)
        return None
