from datetime import datetime, timedelta
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
from dexter.analysis import SourceAnalyser, TopicAnalyser
from dexter.utils import client_cache_for


@app.route('/mine/')
@roles_accepted('monitor', 'miner')
@client_cache_for(minutes=10)
def mine_home():
    form = MineForm(request.args)

    sa = SourceAnalyser(doc_ids=form.document_ids())
    sa.analyse()
    sa.load_utterances()

    expires = datetime.now() + timedelta(minutes=10)

    return render_template('mine/index.haml',
            form=form,
            source_analyser=sa),


class MineForm(Form):
    medium_id       = SelectField('Medium', [validators.Optional()], default='')
    published_at    = TextField('Published', [validators.Optional()])
    source_person_id = TextField('With source', [validators.Optional()])

    nature_id = AnalysisNature.ANCHOR

    def __init__(self, *args, **kwargs):
        super(MineForm, self).__init__(*args, **kwargs)

        self.country = current_user.country

        media = Medium.query.filter(Medium.country == self.country).order_by(Medium.name).all()
        self.medium_id.choices = [('', 'All Media')] + [(str(m.id), m.name) for m in media]
        if not self.published_at.data:
            self.published_at.data = ' - '.join(d.strftime("%Y/%m/%d") for d in [datetime.utcnow() - timedelta(days=14), datetime.utcnow()])


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
        query = query.filter(
                Document.analysis_nature_id == self.nature_id,
                Document.country == self.country,
                )

        if self.medium_id.data:
            query = query.filter(Document.medium_id.in_(self.medium_id.data))

        if self.published_from:
            query = query.filter(Document.published_at >= self.published_from)

        if self.published_to:
            query = query.filter(Document.published_at <= self.published_to)

        if self.source_person_id.data:
            query = query\
                .join(DocumentSource)\
                .filter(DocumentSource.person_id == self.source_person_id.data)

        return query
