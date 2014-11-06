from itertools import groupby
from datetime import datetime, timedelta
from collections import Counter

from dexter.app import app
from flask import request, url_for, flash, redirect, make_response, jsonify, abort
from flask.ext.mako import render_template
from flask.ext.login import login_required, current_user
from sqlalchemy.sql import func, distinct, or_
from sqlalchemy.orm import joinedload

from dexter.models import *
from dexter.models.document import DocumentAnalysisProblem
from dexter.models.user import default_analysis_nature_id, default_country_id

from wtforms import validators, HiddenField, TextField, SelectMultipleField, BooleanField
from wtforms.fields.html5 import DateField
from .forms import Form, SelectField, MultiCheckboxField, RadioField
from .processing.xlsx import XLSXBuilder
from .analysis import SourceAnalyser, TopicAnalyser

from utils import paginate

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


    # setup pagination for doc ids
    query = db.session.query(Document.id).order_by(Document.created_at.desc())
    query = form.filter_query(query)
    pagination = paginate(query, page, per_page)

    doc_ids = [t.id for t in pagination.items]

    # get documents
    docs = Document.query\
                .options(
                    joinedload(Document.created_by),
                    joinedload(Document.medium),
                    joinedload(Document.topic),
                    joinedload(Document.origin),
                    joinedload(Document.fairness),
                    joinedload(Document.sources).lazyload('*')
                )\
                .filter(Document.id.in_(doc_ids))\
                .order_by(Document.created_at.desc())\
                .all()

    # group by date added
    doc_groups = []
    for date, group in groupby(docs, lambda d: d.created_at.date()):
        doc_groups.append([date, list(group)])

    return render_template('dashboard/activity.haml',
                           form=form,
                           pagination=pagination,
                           doc_groups=doc_groups)

@app.route('/activity/map')
@login_required
def activity_map():
    form = ActivityForm(request.args)

    if form.format.data == 'places-json':
        # places in json format
        query = Document.query\
                  .options(joinedload('places').joinedload('place'))
        query = form.filter_query(query)

        return jsonify(DocumentPlace.summary_for_docs(query.all()))

    return render_template('dashboard/map.haml',
                           form=form)


@app.route('/activity/sources')
@login_required
def activity_sources():
    form = ActivityForm(request.args)

    sa = SourceAnalyser(doc_ids=form.document_ids())
    sa.analyse()
    sa.load_utterances()


    # problem sources
    problem_people = sa.find_problem_people()
    problem_people.sort(key=lambda p: -sa.analysed_people[p.id].source_counts_total)

    return render_template('dashboard/sources.haml',
                           form=form,
                           problem_people=problem_people,
                           source_analyser=sa)


@app.route('/activity/mentions')
@login_required
def activity_mentions():
    form = ActivityForm(request.args)

    ta = TopicAnalyser(doc_ids=form.document_ids())
    ta.find_top_people()

    return render_template('dashboard/mentions.haml',
                           form=form,
                           topic_analyser=ta)


@app.route('/activity/topics')
@login_required
def activity_topics():
    # topics take a while to build, so this
    # just returns a shell view which calls back for
    # the actual HTML via ajax, served by activity_topics_detail
    form = ActivityForm(request.args)

    return render_template('dashboard/topics.haml',
                           form=form)


@app.route('/activity/topics/detail')
@login_required
def activity_topics_detail():
    form = ActivityForm(request.args)

    ta = TopicAnalyser(doc_ids=form.document_ids())
    ta.find_topics()
    ta.save()
    db.session.commit()

    return render_template('dashboard/topics_detail.haml',
                           topic_analyser=ta)


class ActivityForm(Form):
    cluster_id  = HiddenField('Cluster')
    analysis_nature_id = RadioField('Analysis', default=AnalysisNature.ANCHOR)
    user_id     = SelectField('User', [validators.Optional()], default='')
    medium_id   = SelectMultipleField('Medium', [validators.Optional()], default='') 
    country_id  = SelectField('Country', [validators.Optional()], default=default_country_id)
    created_at  = TextField('Added', [validators.Optional()])
    published_at   = TextField('Published', [validators.Optional()])
    problems       = MultiCheckboxField('Article problems', [validators.Optional()], choices=DocumentAnalysisProblem.for_select())
    flagged        = BooleanField('flagged')
    has_url        = RadioField('hasurl', [validators.Optional()], choices=[('1', 'with URL'), ('0', 'without URL')])
    format         = HiddenField('format', default='html')

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)

        self.user_id.choices = [['', '(any)'], ['-', '(none)']] + [
                [str(u.id), u.short_name()] for u in sorted(User.query.all(), key=lambda u: u.short_name())]

        self.medium_id.choices = [(str(m.id), m.name) for m in Medium.query.order_by(Medium.name).all()]
        self.analysis_nature_id.choices = [[str(n.id), n.name] for n in AnalysisNature.all()]
        self.country_id.choices = [['', '(any)']] + [[str(c.id), c.name] for c in Country.all()]

        # override the analysis nature id if we have a cluster
        if self.cluster_id.data:
            self.analysis_nature_id.data = str(self.cluster().members[0].document.analysis_nature_id)

        # at least one of these must be set
        oneof = [self.created_at, self.published_at, self.user_id, self.medium_id, self.cluster_id]
        if not any(x.data for x in oneof):
            self.published_at.data = ' - '.join(d.strftime("%Y/%m/%d") for d in [datetime.utcnow() - timedelta(days=14), datetime.utcnow()])


    def user(self):
        if self.user_id.data and self.user_id.data != '-':
            return User.query.get(self.user_id.data)
        return None

    def media(self):
        if self.medium_id.data:
            return Medium.query.filter(Medium.id.in_(self.medium_id.data))
        else:
            return None

    def country(self):
        if self.country_id.data:
            return Country.query.get(self.country_id.data)
        return None

    def analysis_nature(self):
        if self.analysis_nature_id.data:
            return AnalysisNature.query.get(self.analysis_nature_id.data)
        return None

    def cluster(self):
        if self.cluster_id.data:
            return Cluster.query.get(self.cluster_id.data)
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


    def document_ids(self):
        return [d[0] for d in self.filter_query(db.session.query(Document.id)).all()]


    def filter_query(self, query):
        query = query.filter(Document.analysis_nature_id == self.analysis_nature_id.data)

        if self.cluster_id.data:
            query = query.join(ClusteredDocument)\
                         .filter(ClusteredDocument.cluster_id == self.cluster_id.data)

        if self.medium_id.data:
            query = query.filter(Document.medium_id.in_(self.medium_id.data))

        if self.user_id.data:
            if self.user_id.data == '-':
                query = query.filter(Document.created_by_user_id == None)
            else:
                query = query.filter(Document.created_by_user_id == self.user_id.data)

        if self.country_id.data:
            query = query.filter(Document.country_id == self.country_id.data)

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

        if self.flagged.data:
            query = query.filter(Document.flagged == True)

        if self.has_url.data == '1':
            query = query.filter(Document.url != None, Document.url != '')
        elif self.has_url.data == '0':
            query = query.filter(or_(Document.url == None, Document.url == ''))

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
                'countries': self.countries_chart(),
                'media': self.media_chart(),
                'problems': self.problems_chart(),
                'fairness': self.fairness_chart(),
                'markers': self.markers_chart(),
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

    def countries_chart(self):
        query = db.session.query(
                  Document.country_id,
                  func.count(Document.id),
                )\
                .group_by(Document.country_id)
        rows = self.filter(query).all()
        countries = dict((c.id, c.name) for c in Country.query.filter(Country.id.in_(r[0] for r in rows)))

        return {
            'values': dict((countries.get(r[0], 'None'), r[1]) for r in rows)
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

    def markers_chart(self):
        counts = {}

        # flagged
        query = self.filter(db.session.query(
                  func.count(Document.id),
                )\
                .filter(Document.flagged == True))
        counts['flagged'] = query.scalar()

        # with URL
        query = self.filter(db.session.query(
                  func.count(Document.id),
                )\
                .filter(Document.url != None, Document.url != ''))
        counts['with-url'] = query.scalar()

        # without URL
        query = self.filter(db.session.query(
                  func.count(Document.id),
                )\
                .filter(or_(Document.url == None, Document.url == '')))
        counts['without-url'] = query.scalar()

        # average people sources per document
        subq = self.filter(db.session\
                .query(func.count(DocumentSource.doc_id).label('count'))\
                .join(Document, DocumentSource.doc_id == Document.id)\
                .group_by(DocumentSource.doc_id))\
                .subquery('cnt')

        n = float(db.session\
                .query(func.avg(subq.c.count))\
                .select_from(subq)\
                .scalar() or 0)
        counts['average-sources-per-document'] = round(n, 2)

        return {
            'values': counts
        }

    def filter(self, query):
        return query.filter(Document.id.in_(self.doc_ids))
