import logging
import urlparse
from datetime import datetime, timedelta
from dateutil.parser import parse
log = logging.getLogger(__name__)

from flask import request, url_for, redirect, jsonify, abort
from flask.ext.login import login_required
from flask.ext import htauth
from sqlalchemy.orm import joinedload, lazyload
from sqlalchemy.sql import func

from .app import app
from .models import db, Author, Person, Entity, Document, DocumentSource, Medium, Location, Topic, Affiliation, DocumentPlace, Place
from .processing import BiasCalculator

@app.route('/api/authors')
@login_required
def api_authors():
    authors = Author.query.order_by(Author.name).all()
    return jsonify({'authors': [a.json() for a in authors]})

@app.route('/api/people')
@login_required
def api_people():
    q = request.args.get('q', '').strip()

    if q and request.args.get('similar'):
        people = [p for p, _ in Person.similarly_named_to(q, 0.7)]
    else:
        query = Person.query\
            .options(joinedload(Person.affiliation))\
            .order_by(Person.name)
        if q:
            q = '%' + q.replace('%', '%%').replace(' ', '%') + '%'
            query = query.filter(Person.name.like(q))
        people = query.all()

    return jsonify({'people': [p.json() for p in people]})

@app.route('/api/entities')
@login_required
def api_entities():
    query = Entity.query.order_by(Entity.name)
    q = request.args.get('q', '').strip()
    if q:
        q = '%' + q.replace('%', '%%').replace(' ', '%') + '%'
        query = query.filter(Entity.name.like(q))

    entities = query.all()

    return jsonify({'entities': [e.json() for e in entities]})

@app.route('/api/entities/<string:group>')
@login_required
def api_group_entities(group):
    query = Entity.query.filter(Entity.group == group).order_by(Entity.name)
    q = request.args.get('q', '').strip()
    if q:
        q = '%' + q.replace('%', '%%').replace(' ', '%') + '%'
        query = query.filter(Entity.name.like(q))

    entities = query.all()

    return jsonify({'entities': [e.json() for e in entities]})


@app.route('/api/feeds/sources')
@app.route('/api/feeds/sources/<string:group>')
@htauth.authenticated
def api_feed_parties(group=None):
    from dexter.models.views import DocumentSourcesView, DocumentsView, DocumentPlacesView

    if group and not group in ['political-parties']:
        abort(404)

    start_date, end_date = api_date_range(request)

    query = db.session.query(
                func.count(DocumentSourcesView.c.document_id).label("record_count"),
                DocumentSourcesView.c.affiliation.label("affiliation"),
                DocumentSourcesView.c.source_name.label("source_name"),
                DocumentSourcesView.c.gender.label("gender"),
                DocumentSourcesView.c.race.label("race"),
                DocumentsView.c.medium_group.label("medium_group"),
                DocumentsView.c.medium_type.label("medium_type"),
                DocumentPlacesView.c.province_code,
                DocumentPlacesView.c.province_name,
                DocumentPlacesView.c.municipality_code,
                DocumentPlacesView.c.municipality_name,
            )\
            .join(DocumentsView, DocumentSourcesView.c.document_id == DocumentsView.c.document_id)\
            .outerjoin(DocumentPlacesView, DocumentPlacesView.c.document_id == DocumentsView.c.document_id)\
            .group_by(
                DocumentSourcesView.c.affiliation.label("affiliation"),
                DocumentSourcesView.c.source_name.label("source_name"),
                DocumentSourcesView.c.gender.label("gender"),
                DocumentSourcesView.c.race.label("race"),
                DocumentsView.c.medium_group.label("medium_group"),
                DocumentsView.c.medium_type.label("medium_type"),
                DocumentPlacesView.c.province_code,
                DocumentPlacesView.c.province_name,
                DocumentPlacesView.c.municipality_code,
                DocumentPlacesView.c.municipality_name,
            )\
            .filter(DocumentsView.c.published_at >= start_date)\
            .filter(DocumentsView.c.published_at <= end_date)

    if group == 'political-parties':
        query = query.filter(DocumentSourcesView.c.affiliation_code.like('4.%'))


    # {
    #   "date-start":"2014-04-03",
    #   "date-end":"2014-04-05",
    #   "cells": [
    #     {
    #       "affiliation": null,
    #       "record_count": 1,
    #       "source_name": "Narend Singh",
    #       "medium_group": "Beeld"
    #     },
    results = {
        "date-start": start_date,
        "date-end": end_date,
        "cells": [r._asdict() for r in query.all()]
    }

    return jsonify(results)


@app.route('/api/feeds/topics')
@htauth.authenticated
def api_feed_topics():
    from dexter.models.views import DocumentSourcesView, DocumentsView, DocumentPlacesView

    start_date, end_date = api_date_range(request)

    query = db.session.query(
                func.count(DocumentsView.c.document_id).label("record_count"),
                DocumentsView.c.topic.label("topic"),
                DocumentsView.c.medium_group.label("medium_group"),
                DocumentsView.c.medium_type.label("medium_type"),
                DocumentPlacesView.c.province_code,
                DocumentPlacesView.c.province_name,
                DocumentPlacesView.c.municipality_code,
                DocumentPlacesView.c.municipality_name,
            )\
            .outerjoin(DocumentPlacesView, DocumentPlacesView.c.document_id == DocumentsView.c.document_id)\
            .group_by(
                DocumentsView.c.topic.label("topic"),
                DocumentsView.c.medium_group.label("medium_group"),
                DocumentsView.c.medium_type.label("medium_type"),
                DocumentPlacesView.c.province_code,
                DocumentPlacesView.c.province_name,
                DocumentPlacesView.c.municipality_code,
                DocumentPlacesView.c.municipality_name,
            )\
            .filter(DocumentsView.c.published_at >= start_date)\
            .filter(DocumentsView.c.published_at <= end_date)

    results = {
        "date-start": start_date,
        "date-end": end_date,
        "cells": [r._asdict() for r in query.all()]
    }

    return jsonify(results)


@app.route('/api/feeds/origins')
@htauth.authenticated
def api_feed_origins():
    from dexter.models.views import DocumentSourcesView, DocumentsView

    start_date, end_date = api_date_range(request)

    query = db.session.query(
                func.count(DocumentsView.c.document_id).label("record_count"),
                DocumentsView.c.origin.label("origin"),
                DocumentsView.c.medium_group.label("medium_group"),
                DocumentsView.c.medium_type.label("medium_type"),
            )\
            .group_by(
                DocumentsView.c.origin.label("origin"),
                DocumentsView.c.medium_group.label("medium_group"),
                DocumentsView.c.medium_type.label("medium_type"),
            )\
            .filter(DocumentsView.c.published_at >= start_date)\
            .filter(DocumentsView.c.published_at <= end_date)

    results = {
        "date-start": start_date,
        "date-end": end_date,
        "cells": [r._asdict() for r in query.all()]
    }

    return jsonify(results)


@app.route('/api/feeds/bias')
@htauth.authenticated
def api_feed_bias():
    start_date, end_date = api_date_range(request)
    calc = BiasCalculator()

    log.info("Loading documents for bias calculation")
    documents = calc.get_query()\
            .filter(Document.published_at >= start_date)\
            .filter(Document.published_at <= end_date).all()
    log.info("Loaded %d docs" % len(documents))

    scores = calc.calculate_bias_scores(documents, key=lambda d: (d.medium.group_name(), d.medium.medium_type))

    cells = []
    for score in scores:
        cell = score.asdict()
        cell['medium_group'] = score.group[0]
        cell['medium_type'] = score.group[1]
        cells.append(cell)

    results = {
        "date-start": start_date,
        "date-end": end_date,
        "cells": cells,
    }

    return jsonify(results)


@app.route('/api/feeds/metadata')
@htauth.authenticated
def api_feed_metadata():
    data = {}

    media = Medium.query.all()
    data['media'] = {
        "bias_feed_url": "%s" % urlparse.urljoin(request.url_root, url_for('api_feed_bias')),
        "names": [m.name for m in media],
        "groups": list(set(m.group_name() for m in media)),
    }

    data['origins'] = {
        "names": [x.name for x in Location.query.all()],
        "feed_url": "%s" % urlparse.urljoin(request.url_root, url_for('api_feed_origins')),
    }

    data['topics'] = {
        "names": [x.name for x in Topic.query.all()],
        "feed_url": "%s" % urlparse.urljoin(request.url_root, url_for('api_feed_topics')),
    }

    data['affiliations'] = {
        "names": [x.name for x in Affiliation.query.all()],
    }

    data['political-parties'] = {
        "names": [x.name for x in Affiliation.query.filter(Affiliation.code.like("4.%")).all()],
        "feed_url": "%s" % urlparse.urljoin(request.url_root, url_for('api_feed_parties')),
    }

    return jsonify({"metadata": data})


def api_date_range(request):
    end_date = datetime.utcnow()
    try:
        end_date = parse(request.args.get('end-date', ''), default=end_date, yearfirst=True)
    except ValueError:
        pass

    start_date = end_date - timedelta(days=7)
    try:
        start_date = parse(request.args.get('start-date', ''), default=start_date, yearfirst=True)
    except ValueError:
        pass

    start_date = start_date.strftime("%Y/%m/%d") + ' 00:00:00'
    end_date = end_date.strftime("%Y/%m/%d") + ' 23:59:59'

    return (start_date, end_date)
