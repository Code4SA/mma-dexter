from itertools import groupby
from datetime import datetime, timedelta
from collections import Counter

from dexter.app import app
from flask import request, url_for, flash, redirect, make_response, jsonify
from flask.ext.mako import render_template
from flask.ext.login import login_required, current_user
from sqlalchemy.sql import func
from sqlalchemy.orm import joinedload

from dexter.models import db, Document, Entity, Medium, User, DocumentSource
from dexter.models.document import DocumentAnalysisProblem

from wtforms import validators, HiddenField, TextField
from wtforms.fields.html5 import DateField
from .forms import Form, SelectField, MultiCheckboxField
from .processing.xlsx import XLSXBuilder

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

    query = form.make_query()

    if form.format.data == 'chart-json':
        # chart data in json format
        return jsonify(ActivityChartHelper(query.all()).chart_data())

    elif form.format.data == 'xlsx':
        # excel spreadsheet
        excel = XLSXBuilder(form).build()

        response = make_response(excel)
        response.headers["Content-Disposition"] = "attachment; filename=%s" % form.filename()
        response.headers["Content-Type"] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
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
    created_at  = TextField('Added', [validators.Optional()])
    published_at   = TextField('Published', [validators.Optional()])
    problems       = MultiCheckboxField('Article problems', [validators.Optional()], choices=DocumentAnalysisProblem.for_select())
    format         = HiddenField('format', default='html') 

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)

        self.user_id.choices = [['', '(any)']] + [
                [str(u.id), u.short_name()] for u in sorted(User.query.all(), key=lambda u: u.short_name())]

        self.medium_id.choices = [['', '(any)']] + [(str(m.id), m.name) for m in Medium.query.order_by(Medium.name).all()]

        # dynamic default
        if not self.created_at.data and not self.published_at.data and not self.user_id.data and not self.medium_id.data:
            self.created_at.data = ' - '.join(d.strftime("%Y/%m/%d") for d in [datetime.utcnow() - timedelta(days=14), datetime.utcnow()])


    def user(self):
        if self.user_id.data:
            return User.query.get(self.user_id.data)
        return None

    def medium(self):
        if self.medium_id.data:
            return Medium.query.get(self.medium_id.data)
        return None

    def make_query(self):
        query = Document.query\
                    .join(DocumentSource)\
                    .options(
                        joinedload(Document.created_by),
                        joinedload(Document.medium),
                        joinedload(Document.topic),
                        joinedload(Document.origin),
                        joinedload(Document.fairness),
                        joinedload(Document.sources),
                    )

        return self.filter_query(query)

    
    @property
    def created_from(self):
        if self.created_at.data:
            return self.created_at.data.split(' - ')[0].strip()
        else:
            return None

    @property
    def created_to(self):
        if self.created_at.data and ' - ' in self.created_at.data:
            return self.created_at.data.split(' - ')[1].strip() + ' 23:59:59'
        else:
            return self.created_from

    @property
    def published_from(self):
        if self.published_at.data:
            return self.published_at.data.split(' - ')[0].strip()
        else:
            return None

    @property
    def published_to(self):
        if self.published_at.data and ' - ' in self.published_at.data:
            return self.published_at.data.split(' - ')[1].strip() + ' 23:59:59'
        else:
            return self.published_from


    def filter_query(self, query):
        if self.medium_id.data:
            query = query.filter(Document.medium_id == self.medium_id.data)

        if self.user_id.data:
            query = query.filter(Document.created_by_user_id == self.user_id.data)

        if self.created_from:
            query = query.filter(Document.created_at >= self.created_from)

        if self.created_to:
            query = query.filter(Document.created_at <= self.created_to)

        if self.published_from:
            query = query.filter(Document.published_at >= self.published_from)

        if self.published_to:
            query = query.filter(Document.published_at <= self.published_to)

        if self.problems.data:
            for code in self.problems.data:
                query = DocumentAnalysisProblem.lookup(code).filter_query(query)

        return query

    def filename(self):
        filename = ['documents']

        if self.created_at.data:
            filename.append('added')
            filename.append(self.created_at.data.replace(' ', ''))

        if self.published_at.data:
            filename.append('published')
            filename.append(self.published_at.data.replace(' ', ''))

        return "%s.%s" % ('-'.join(filename), self.format.data)

    def as_dict(self):
        return dict((f.name, f.data) for f in self if f.name != 'csrf_token')


class ActivityChartHelper:
    def __init__(self, docs):
        self.docs = docs


    def chart_data(self):
        return {
            'charts': {
                'created': self.created_chart(),
                'published': self.published_chart(),
                'users': self.users_chart(),
                'media': self.media_chart(),
                'problems': self.problems_chart(),
                'fairness': self.fairness_chart(),
            },
            'summary': {
                'documents': len(self.docs)
            }
        }


    def created_chart(self):
        return {
            'values': dict(Counter(d.created_at.strftime('%Y/%m/%d') for d in self.docs))
        }

    def published_chart(self):
        return {
            'values': dict(Counter(d.published_at.strftime('%Y/%m/%d') for d in self.docs))
        }

    def users_chart(self):
        return {
            'values': dict(Counter(d.created_by.short_name() if d.created_by else '' for d in self.docs))
        }

    def fairness_chart(self):
        counts = Counter()
        for d in self.docs:
            if d.is_fair():
                counts.update(['Fair'])
            else:
                counts.update(f.fairness.name for f in d.fairness)
        return {
            'values': dict(counts)
        }

    def media_chart(self):
        return {
            'values': dict(Counter(d.medium.name for d in self.docs)),
            'types': dict([d.medium.name, d.medium.medium_type] for d in self.docs)
        }

    def problems_chart(self):
        counts = Counter()
        for d in self.docs:
            counts.update(w.short_desc for w in d.analysis_warnings())

        return {
            'values': dict(counts)
        }
