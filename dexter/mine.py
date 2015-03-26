from datetime import datetime, timedelta, date
import time

from wtforms import validators, HiddenField, TextField, SelectMultipleField, BooleanField
from wtforms.fields.html5 import DateField

from flask import request, url_for, flash, redirect, make_response, jsonify, abort
from flask.ext.mako import render_template
from flask.ext.security import roles_accepted, current_user
from wsgiref.handlers import format_date_time

from dexter.app import app
from dexter.models import *
from dexter.forms import Form, SelectField, MultiCheckboxField, RadioField
from dexter.analysis import SourceAnalyser, TopicAnalyser, MediaAnalyser
from dexter.utils import client_cache_for


@app.route('/mine/')
@roles_accepted('monitor', 'miner')
@client_cache_for(minutes=10)
def mine_home():
    form = MineForm(request.args)

    ma = MediaAnalyser(doc_ids=form.document_ids(overview=True))
    ma.analyse()

    sa = SourceAnalyser(doc_ids=form.document_ids())
    sa.analyse()
    sa.load_utterances()

    return render_template('mine/index.haml',
            form=form,
            source_analyser=sa,
            media_analyser=ma)


class MineForm(Form):
    medium_id       = HiddenField('Medium', [validators.Optional()])
    # period to cover, expressed in days since yesterday
    period          = RadioField('Period', [validators.Optional()], choices=[('7', 'last 7 days'), ('30', 'last 30 days'), ('90', 'last 90 days')], default='7')
    source_person_id = TextField('With source', [validators.Optional()])

    nature_id = AnalysisNature.ANCHOR

    def __init__(self, *args, **kwargs):
        super(MineForm, self).__init__(*args, **kwargs)
        self.country = current_user.country
        self.yesterday = date.today() - timedelta(days=1)


    @property
    def published_from(self):
        try:
            days = int(self.period.data)
        except ValueError:
            days = 7

        return (self.yesterday - timedelta(days=days)).strftime('%Y-%m-%d 00:00:00')

    @property
    def published_to(self):
        return (self.yesterday - timedelta(days=1)).strftime('%Y-%m-%d 23:59:59')

    def document_ids(self, overview=False):
        return [d[0] for d in self.filter_query(db.session.query(Document.id), overview=overview).all()]

    @property
    def medium(self):
        if self.medium_id.data:
            return Medium.query.get(self.medium_id.data)

    def filter_query(self, query, overview=False):
        query = query.filter(
                Document.analysis_nature_id == self.nature_id,
                Document.country == self.country,
                )

        if not overview and self.medium:
            query = query.filter(Document.medium == self.medium)

        query = query.filter(
                Document.published_at >= self.published_from,
                Document.published_at <= self.published_to)

        if self.source_person_id.data:
            query = query\
                .join(DocumentSource)\
                .filter(DocumentSource.person_id == self.source_person_id.data)

        return query
