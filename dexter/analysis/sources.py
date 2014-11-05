from math import sqrt
from collections import defaultdict
from itertools import groupby, chain
from datetime import datetime
from dateutil.parser import parse

from dexter.analysis.base import BaseAnalyser, moving_weighted_avg_zscore
from dexter.models import db, Document, DocumentSource, Person, Utterance, Entity

from sqlalchemy.sql import func, distinct, or_, desc
from sqlalchemy.orm import joinedload


class AnalysedSource(object):
    pass


class AnalysedUtterance(object):
    pass


class SourceAnalyser(BaseAnalyser):
    """
    Helper that runs analyses on document sources.
    """

    def __init__(self, doc_ids=None, start_date=None, end_date=None):
        super(SourceAnalyser, self).__init__(doc_ids, start_date, end_date)
        self.top_people = None
        self.people_trending_up = None
        self.people_trending_down = None
        self.person_utterances = None

    def analyse(self):
        self._load_people_sources()
        self._analyse_people_sources()


    def load_utterances(self):
        """ Find utterances for the sources we've analysed.
        Sets `person_utterances`, a map from person id to 
        `AnalysedUtterance` instances.
        """
        ids = [src.person.id for src in chain(self.top_people, self.people_trending_up, self.people_trending_down)]

        utterances = Utterance.query\
                      .join(Entity, Entity.id == Utterance.entity_id)\
                      .filter(Entity.person_id.in_(ids))\
                      .filter(Utterance.doc_id.in_(self.doc_ids))\
                      .all()

        self.person_utterances = defaultdict(list)
        for utterance in utterances:
            au = AnalysedUtterance()
            au.quote = utterance.quote
            self.person_utterances[utterance.entity.person_id].append(au)


    def _load_people_sources(self):
        """
        Load all people source data for this period.
        """
        rows = db.session.query(distinct(DocumentSource.person_id))\
                .filter(
                        DocumentSource.doc_id.in_(self.doc_ids),
                        DocumentSource.person_id != None)\
                .group_by(DocumentSource.person_id)\
                .all()
        self.people = self._lookup_people([r[0] for r in rows])


    def _analyse_people_sources(self):
        """
        Do trend analysis on people.
        """
        utterance_count = self.count_utterances(self.people.keys())
        source_counts = self.source_frequencies(self.people.keys())

        self.analysed_people = {}
        for pid, person in self.people.iteritems():
            src = AnalysedSource()
            src.person = person

            src.utterance_count = utterance_count.get(src.person.id, 0)
            src.source_counts = source_counts[src.person.id]
            src.source_counts_total = sum(src.source_counts)

            self.analysed_people[pid] = src

        # normalize by total counts per day
        totals = [0] * (self.days+1)

        # first count per-day totals
        for src in self.analysed_people.itervalues():
            for i, n in enumerate(src.source_counts):
                totals[i] += n

        # normalize
        for src in self.analysed_people.itervalues():
            for i, n in enumerate(src.source_counts):
                if totals[i] == 0:
                    src.source_counts[i] = 0
                else:
                    src.source_counts[i] = 100.0 * n / totals[i]

        # calculate trends
        for src in self.analysed_people.itervalues():
            src.source_counts_trend = moving_weighted_avg_zscore(src.source_counts, 0.8)


        # top 20 sources
        self.top_people = sorted(
                self.analysed_people.itervalues(),
                key=lambda s: s.source_counts_total, reverse=True)[:20]

        # trends
        trending = sorted(
                self.analysed_people.itervalues(),
                key=lambda s: s.source_counts_trend)

        # top 10 trending up, most trending first
        self.people_trending_up = [s for s in trending[-10:] if s.source_counts_trend > self.TREND_UP]
        self.people_trending_up.reverse()

        # top 10 trending down, most trending first
        self.people_trending_down = [s for s in trending[:10] if s.source_counts_trend < self.TREND_DOWN]


    def count_utterances(self, ids):
        """
        Return dict from person ID to number of utterances they had in
        these documents.
        """
        rows = db.session.query(
                Person.id,
                func.count(1).label('count')
                )\
                .join(Entity, Entity.person_id == Person.id)\
                .join(Utterance, Utterance.entity_id == Entity.id)\
                .filter(Utterance.doc_id.in_(self.doc_ids))\
                .filter(Person.id.in_(ids))\
                .group_by(Person.id)\
                .all()

        return dict((p[0], p[1]) for p in rows)


    def source_frequencies(self, ids):
        """
        Return dict from person ID to a list of how frequently each
        source was used per day, over the period.
        """
        rows = db.session.query(
                    DocumentSource.person_id,
                    func.date_format(Document.published_at, '%Y-%m-%d').label('date'),
                    func.count(1).label('count')
                )\
                .join(Document, DocumentSource.doc_id == Document.id)\
                .filter(DocumentSource.person_id.in_(ids))\
                .filter(DocumentSource.doc_id.in_(self.doc_ids))\
                .group_by(DocumentSource.person_id, 'date')\
                .order_by(DocumentSource.person_id, Document.published_at)\
                .all()

        freqs = {}
        for person_id, group in groupby(rows, lambda r: r[0]):
            freqs[person_id] = [0] * (self.days+1)

            # set day buckets based on date
            for row in group:
                d, n = parse(row[1]).date(), row[2]
                day = (d - self.start_date).days
                freqs[person_id][day] = n

        return freqs


    def find_problem_people(self):
        """
        Return a list of Person instances for people sources that lack
        a race, gender or affiliation.
        """
        rows = db.session.query(
                    DocumentSource.person_id,
                    func.count(1).label('count')
                )\
                .join(Person, Person.id == DocumentSource.person_id)\
                .filter(DocumentSource.person_id != None)\
                .filter(DocumentSource.doc_id.in_(self.doc_ids))\
                .filter(or_(
                    Person.race_id == None,
                    Person.gender_id == None,
                    Person.affiliation_id == None))\
                .group_by(DocumentSource.person_id)\
                .order_by(desc('count'))\
                .limit(20)\
                .all()

        return self._lookup_people([r[0] for r in rows]).values()
