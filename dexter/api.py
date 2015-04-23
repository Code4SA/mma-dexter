import logging
import urlparse
import urllib
from datetime import datetime, timedelta
from dateutil.parser import parse
log = logging.getLogger(__name__)

from flask import request, url_for, redirect, jsonify, abort
from flask.ext.security import roles_accepted, current_user
from flask.ext import htauth
from sqlalchemy.orm import joinedload, lazyload
from sqlalchemy.sql import func

from .app import app
from .models import db, Author, Person, Entity, Document, DocumentSource, Medium, Location, Topic, Affiliation, DocumentPlace, Place, Country
from .analysis import BiasCalculator

@app.route('/api/authors')
@roles_accepted('monitor')
def api_authors():
    q = request.args.get('q', '').strip()
    try:
        limit = max(int(request.args.get('limit', 10)), 0)
    except:
        limit = 10

    query = Author.query
    if q:
        q = '%' + q.replace('%', '%%').replace(' ', '%') + '%'
        query = query.filter(Author.name.like(q))\
                     .order_by(func.length(Author.name))

    authors = query.order_by(Author.name)\
                   .limit(limit)\
                   .all()

    return jsonify({'authors': [a.json() for a in authors]})

@app.route('/api/people')
@roles_accepted('monitor', 'mine')
def api_people():
    q = request.args.get('q', '').strip()
    try:
        limit = max(int(request.args.get('limit', 10)), 0)
    except:
        limit = 10

    if q and request.args.get('similar'):
        people = [p for p, _ in Person.similarly_named_to(q, 0.7)]
    else:
        query = Person.query\
            .options(joinedload(Person.affiliation))
        if q:
            q = '%' + q.replace('%', '%%').replace(' ', '%') + '%'
            query = query.filter(Person.name.like(q))\
                         .order_by(func.length(Person.name))

        people = query.order_by(Person.name)\
                      .limit(limit)\
                      .all()

    return jsonify({'people': [p.json() for p in people]})

# THIS IS A PUBLIC API
@app.route('/api/people/<string:name>/sourced')
def api_people_sourced(name):
    """
    Returns the documents where a person has been sourced.
    """
    from dexter.models.views import DocumentsView

    start_date, end_date = api_date_range(request)
    name = urllib.unquote_plus(name)

    person = Person.query.filter(Person.name == name).first()
    if not person:
        abort(404)

    query = db.session.query(
                DocumentsView.c.article_url,
                DocumentsView.c.title,
                DocumentsView.c.published_date,
                DocumentsView.c.medium,
            )\
            .join(DocumentSource, DocumentSource.doc_id == DocumentsView.c.document_id)\
            .filter(DocumentSource.person_id == person.id)\
            .filter(DocumentsView.c.published_at >= start_date)\
            .filter(DocumentsView.c.published_at <= end_date)\

    query = filter_country(query, DocumentsView.c.country, request.args.get('country'))\
            .order_by(DocumentsView.c.published_at.desc())\
            .limit(50) # only return the most recent 50

    result = {
        "date-start": start_date,
        "date-end": end_date,
        "source": person.json(),
        "sourced_by": [r._asdict() for r in query.all()]
    }

    return jsonify(result)


@app.route('/api/entities')
@roles_accepted('monitor')
def api_entities():
    q = request.args.get('q', '').strip()
    try:
        limit = max(int(request.args.get('limit', 10)), 0)
    except:
        limit = 10

    query = Entity.query
    if q:
        q = '%' + q.replace('%', '%%').replace(' ', '%') + '%'
        query = query.filter(Entity.name.like(q))\
                     .order_by(func.length(Entity.name))

    entities = query.order_by(Entity.name)\
                    .limit(limit)\
                    .all()

    return jsonify({'entities': [e.json() for e in entities]})

@app.route('/api/entities/<string:group>')
@roles_accepted('monitor')
def api_group_entities(group):
    query = Entity.query.filter(Entity.group == group).order_by(Entity.name)
    q = request.args.get('q', '').strip()
    if q:
        q = '%' + q.replace('%', '%%').replace(' ', '%') + '%'
        query = query.filter(Entity.name.like(q))

    entities = query.all()

    return jsonify({'entities': [e.json() for e in entities]})

# THIS IS A PUBLIC API!
@app.route('/api/feeds/sources/people')
def api_feed_people():
    start_date, end_date = api_date_range(request)

    # since it's public, keep the list of permitted keys limited
    keys = ['source_name', 'gender', 'race', 'affiliation', 'affiliation_group']

    results = get_sources_feed(start_date, end_date, keys, source_type='person')
    return jsonify(results)

@app.route('/api/feeds/sources')
@app.route('/api/feeds/sources/<string:group>')
@htauth.authenticated
def api_feed_sources(group=None):
    start_date, end_date = api_date_range(request)
    keys = request.args.get('keys', '').strip()
    if keys:
        keys = keys.split(',')

    results = get_sources_feed(start_date, end_date, keys, group)
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

    query = filter_country(query, DocumentsView.c.country, request.args.get('country'))

    results = {
        "date-start": start_date,
        "date-end": end_date,
        "cells": [r._asdict() for r in query.all()]
    }

    return jsonify(results)


@app.route('/api/feeds/origins')
@htauth.authenticated
def api_feed_origins():
    from dexter.models.views import DocumentsView

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

    query = filter_country(query, DocumentsView.c.country, request.args.get('country'))

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
    query = calc.get_query()\
            .join(Country)\
            .filter(Document.published_at >= start_date)\
            .filter(Document.published_at <= end_date)

    query = filter_country(query, Country.name, request.args.get('country'))

    documents = query.all()

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

def get_sources_feed(start_date, end_date, keys=None, group=None, source_type=None):
    """
    Get a rollup of sources over a period, where 'keys' is a list
    of keys to group them by.
    """
    from dexter.models.views import DocumentSourcesView, DocumentsView, DocumentPlacesView

    if group and group not in ['political-parties', 'groups']:
        abort(404)

    # map from the column alias to the column object
    FIELDS = {str(c.name): c for c in [
            DocumentSourcesView.c.affiliation.label("affiliation"),
            DocumentSourcesView.c.affiliation_group.label("affiliation_group"),
            DocumentSourcesView.c.source_name.label("source_name"),
            DocumentSourcesView.c.gender.label("gender"),
            DocumentSourcesView.c.race.label("race"),
            DocumentsView.c.medium_group.label("medium_group"),
            DocumentsView.c.medium_type.label("medium_type"),
            DocumentPlacesView.c.province_code,
            DocumentPlacesView.c.province_name,
            DocumentPlacesView.c.municipality_code,
            DocumentPlacesView.c.municipality_name,
            ]}

    # let the user choose what columns they get back as a comma-separated list
    if not keys:
        keys = FIELDS.keys()
        if group == 'groups':
            # remove the affiliation column
            keys.remove('affiliation')

    cols = [FIELDS[c] for c in FIELDS.viewkeys() & keys]

    query = db.session.query(
                func.count(DocumentSourcesView.c.document_id).label("record_count"),
                *cols
            )\
            .join(DocumentsView, DocumentSourcesView.c.document_id == DocumentsView.c.document_id)\
            .outerjoin(DocumentPlacesView, DocumentPlacesView.c.document_id == DocumentsView.c.document_id)\
            .group_by(*cols)\
            .filter(DocumentsView.c.published_at >= start_date)\
            .filter(DocumentsView.c.published_at <= end_date)

    if source_type is not None:
        query = query.filter(DocumentSourcesView.c.source_type == source_type)

    if group == 'political-parties':
        query = query.filter(DocumentSourcesView.c.affiliation_code.like('4.%'))

    query = filter_country(query, DocumentsView.c.country, request.args.get('country'))

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

    return results

def filter_country(query, col, country=None):
    if not country:
        if current_user and current_user.is_authenticated():
            country = current_user.country
        else:
            country = Country.query.filter(Country.code == 'za').first()
    else:
        country = Country.query.filter(Country.code == country).first()

    if not country:
        abort(400, 'invalid country')

    return query.filter(col == country)

