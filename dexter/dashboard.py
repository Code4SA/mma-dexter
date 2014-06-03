from itertools import groupby
from datetime import datetime, timedelta
from collections import Counter

from dexter.app import app
from flask import request, url_for, flash, redirect, make_response, jsonify, abort
from flask.ext.mako import render_template
from flask.ext.login import login_required, current_user
from flask.ext.sqlalchemy import Pagination
from sqlalchemy.sql import func, distinct
from sqlalchemy.orm import joinedload, subqueryload

from dexter.models import db, Document, Entity, Medium, User, DocumentSource, DocumentPlace, DocumentFairness, Fairness, Topic, Place
from dexter.models.document import DocumentAnalysisProblem

from wtforms import validators, HiddenField, TextField, SelectMultipleField
from wtforms.fields.html5 import DateField
from .forms import Form, SelectField, MultiCheckboxField
from .processing.xlsx import XLSXBuilder

@app.route('/dashboard')
@login_required
def dashboard():
    latest_docs = [x.id for x in Document.query.order_by(Document.created_at.desc()).limit(30)]

    latest_docs = Document.query\
        .options(
            joinedload('created_by'),
            joinedload('sources'),
            joinedload('topic'),
            joinedload('medium'),
        )\
        .filter(Document.id.in_(latest_docs))\
        .order_by(Document.created_at.desc())

    doc_groups = []
    for date, group in groupby(latest_docs, lambda d: d.created_at.date()):
        doc_groups.append([date, list(group)])

    return render_template('dashboard/dashboard.haml',
                           doc_groups=doc_groups)


@app.route('/monitor-dashboard')
@login_required
def monitor_dashboard():
    docs = [x.id for x in Document.query.filter(Document.created_by_user_id == current_user.id)\
        .order_by(Document.created_at.desc()).limit(30)]

    docs = Document.query\
        .options(
            joinedload('created_by'),
            joinedload('sources'),
            joinedload('topic'),
            joinedload('medium'),
        )\
        .filter(Document.id.in_(docs))\
        .order_by(Document.created_at.desc())

    doc_groups = []
    for date, group in groupby(docs, lambda d: d.created_at.date()):
        doc_groups.append([date, list(group)])

    return render_template('dashboard/monitor.haml',
                           doc_groups=doc_groups)


@app.route('/coverage-map')
def coverage_map():

    form = CoverageForm(request.args)

    if form.format.data == 'places-json':
        # places in json format
        query = Document.query\
                  .options(joinedload('places').joinedload('place'))
        query = form.filter_query(query)

        return jsonify(DocumentPlace.summary_for_coverage(query.all()))

    query = Document.query\
                .options(
                    joinedload(Document.medium),
                    joinedload(Document.topic),
                    joinedload(Document.origin).lazyload('*')
                )
    query = form.filter_query(query)

    # do manual pagination
    query = query.order_by(Document.created_at.desc())
    document_count = form.filter_query(db.session.query(func.count(distinct(Document.id)))).scalar()
    paged_docs = query.all()

    return render_template('dashboard/coverage-map.haml',
                           form=form,
                           document_count=document_count,
                           paged_docs=paged_docs)


class CoverageForm(Form):
    medium_id = SelectMultipleField('Medium', [validators.Optional()], default='')
    published_at = TextField('Published', [validators.Optional()])
    format = HiddenField('format', default='html')
    selected_province = HiddenField('selected_province')
    selected_municipality = HiddenField('selected_municipality')

    def __init__(self, *args, **kwargs):
        super(CoverageForm, self).__init__(*args, **kwargs)

        self.medium_id.choices = [(str(m.id), m.name) for m in Medium.query.order_by(Medium.name).all()]

        # dynamic default
        if not self.published_at.data:
            self.published_at.data = ' - '.join(d.strftime("%Y/%m/%d") for d in [datetime.utcnow() - timedelta(days=14), datetime.utcnow()])

    def media(self):
        if self.medium_id.data:
            return Medium.query.filter(Medium.id.in_(self.medium_id.data))
        else:
            return None

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
        # Note: this filter is not working as expected
        # if self.level.data and self.level.data == "province":
        #     query = query.filter(Place.province_code == self.selected_area.data)

        if self.medium_id.data:
            query = query.filter(Document.medium_id.in_(self.medium_id.data))

        if self.published_from:
            query = query.filter(Document.published_at >= self.published_from)

        if self.published_to:
            query = query.filter(Document.published_at <= self.published_to)
        return query

    def as_dict(self):
        return dict((f.name, f.data) for f in self if f.name != 'csrf_token')


@app.route('/activity')
@login_required
def activity():
    per_page = 100

    form = ActivityForm(request.args)

    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

    if form.format.data == 'chart-json':
        # chart data in json format
        return jsonify(ActivityChartHelper(form).chart_data())

    elif form.format.data == 'places-json':
        # places in json format
        query = Document.query\
                  .options(joinedload('places').joinedload('place'))
        query = form.filter_query(query)

        return jsonify(DocumentPlace.summary_for_docs(query.all()))

    elif form.format.data == 'xlsx':
        # excel spreadsheet
        excel = XLSXBuilder(form).build()

        response = make_response(excel)
        response.headers["Content-Disposition"] = "attachment; filename=%s" % form.filename()
        response.headers["Content-Type"] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        return response


    query = Document.query\
                .options(
                    joinedload(Document.created_by),
                    joinedload(Document.medium),
                    joinedload(Document.topic),
                    joinedload(Document.origin),
                    joinedload(Document.fairness),
                    joinedload(Document.sources).lazyload('*')
                )
    query = form.filter_query(query)

    # do manual pagination
    query = query.order_by(Document.created_at.desc())
    items = query.limit(per_page).offset((page - 1) * per_page).all()
    if not items and page != 1:
        abort(404)
    total = form.filter_query(db.session.query(func.count(distinct(Document.id)))).scalar()
    paged_docs = Pagination(query, page, min(per_page, len(items)), total, items)

    # group by date added
    doc_groups = []
    for date, group in groupby(paged_docs.items, lambda d: d.created_at.date()):
        doc_groups.append([date, list(group)])

    return render_template('dashboard/activity.haml',
                           form=form,
                           paged_docs=paged_docs,
                           doc_groups=doc_groups)


class ActivityForm(Form):
    user_id     = SelectField('User', [validators.Optional()], default='')
    medium_id   = SelectMultipleField('Medium', [validators.Optional()], default='') 
    created_at  = TextField('Added', [validators.Optional()])
    published_at   = TextField('Published', [validators.Optional()])
    problems       = MultiCheckboxField('Article problems', [validators.Optional()], choices=DocumentAnalysisProblem.for_select())
    format         = HiddenField('format', default='html') 

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)

        self.user_id.choices = [['', '(any)']] + [
                [str(u.id), u.short_name()] for u in sorted(User.query.all(), key=lambda u: u.short_name())]

        self.medium_id.choices = [(str(m.id), m.name) for m in Medium.query.order_by(Medium.name).all()]

        # dynamic default
        if not self.created_at.data and not self.published_at.data and not self.user_id.data and not self.medium_id.data:
            self.created_at.data = ' - '.join(d.strftime("%Y/%m/%d") for d in [datetime.utcnow() - timedelta(days=14), datetime.utcnow()])


    def user(self):
        if self.user_id.data:
            return User.query.get(self.user_id.data)
        return None

    def media(self):
        if self.medium_id.data:
            return Medium.query.filter(Medium.id.in_(self.medium_id.data))
        else:
            return None


    def get_problems(self):
        return [DocumentAnalysisProblem.lookup(code) for code in self.problems.data]


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
            query = query.filter(Document.medium_id.in_(self.medium_id.data))

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
    def __init__(self, form):
        self.form = form

        # we use these to filter our queries, rather than trying to pull
        # complex filter logic into our view queries
        self.doc_ids = [d[0] for d in form.filter_query(db.session.query(Document.id)).all()]


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
                'documents': len(self.doc_ids)
            }
        }


    def created_chart(self):
        query = db.session.query(
                  func.date_format(Document.created_at, '%Y/%m/%d').label('t'),
                  func.count(Document.id),
                )\
                .group_by('t')

        return {
            'values': dict(self.filter(query).all())
        }

    def published_chart(self):
        query = db.session.query(
                  func.date_format(Document.published_at, '%Y/%m/%d').label('t'),
                  func.count(Document.id),
                )\
                .group_by('t')

        return {
            'values': dict(self.filter(query).all())
        }

    def users_chart(self):
        query = db.session.query(
                  Document.created_by_user_id,
                  func.count(Document.id),
                )\
                .group_by(Document.created_by_user_id)
        rows = self.filter(query).all()
        users = dict((u.id, u.short_name()) for u in User.query.filter(User.id.in_(r[0] for r in rows)))

        return {
            'values': dict((users.get(r[0], 'None'), r[1]) for r in rows)
        }

    def fairness_chart(self):
        query = db.session.query(
                    Fairness.name.label('t'),
                    func.count(distinct(DocumentFairness.doc_id)))\
                .join(DocumentFairness)\
                .join(Document, DocumentFairness.doc_id == Document.id)\
                .group_by('t')

        rows = self.filter(query).all()
        counts = dict(rows)
        counts.setdefault('Fair', 0)

        # missing documents are considered fair
        counts['Fair'] += len(self.doc_ids) - sum(counts.itervalues())

        return {
            'values': counts
        }

    def media_chart(self):
        query = db.session.query(
                    Medium.name,
                    func.count(Document.id))\
                    .join(Document)\
                    .group_by(Medium.name)
        rows = self.filter(query).all()

        return {
            'values': dict(rows),
            'types': dict([m.name, m.medium_type] for m in Medium.query.all())
        }

    def problems_chart(self):
        counts = {}

        for p in DocumentAnalysisProblem.all():
            query = db.session.query(func.count(distinct(Document.id)))
            query = self.filter(p.filter_query(query))
            counts[p.short_desc] = query.scalar()

        return {
            'values': counts
        }

    def filter(self, query):
        return query.filter(Document.id.in_(self.doc_ids))
