import logging
from datetime import datetime, timedelta
from dateutil.parser import parse
log = logging.getLogger(__name__)

from flask import request, url_for, redirect, jsonify
from flask.ext.login import login_required
from flask.ext import htauth
from sqlalchemy.orm import subqueryload
from sqlalchemy.sql import func

from .app import app
from .models import db, Author, Person, Entity

@app.route('/api/authors')
@login_required
def api_authors():
    authors = Author.query.order_by(Author.name).all()
    return jsonify({'authors': [a.json() for a in authors]})

@app.route('/api/people')
@login_required
def api_people():
    people = Person.query\
        .options(subqueryload(Person.affiliation))\
        .order_by(Person.name)\
        .all()
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

@app.route('/api/feeds/sources/political-parties')
@htauth.authenticated
def api_feed_sources():
    from dexter.models.views import DocumentSourcesView, DocumentsView

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

    end_date = end_date.strftime("%Y/%m/%d")
    start_date = start_date.strftime("%Y/%m/%d")

    query = db.session.query(
                func.count(DocumentSourcesView.c.document_id).label("record_count"),
                DocumentSourcesView.c.affiliation.label("affiliation"),
                DocumentSourcesView.c.source_name.label("source_name"),
                DocumentsView.c.medium_group.label("medium_group"),
                DocumentsView.c.medium_type.label("medium_type"),
            )\
            .join(DocumentsView, DocumentSourcesView.c.document_id == DocumentsView.c.document_id)\
            .group_by(
                DocumentSourcesView.c.affiliation.label("affiliation"),
                DocumentSourcesView.c.source_name.label("source_name"),
                DocumentsView.c.medium_group.label("medium_group"),
                DocumentsView.c.medium_type.label("medium_type"),
            )\
            .filter(DocumentSourcesView.c.affiliation_code.like('4.%'))\
            .filter(DocumentsView.c.published_at >= start_date)\
            .filter(DocumentsView.c.published_at <= end_date)

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
