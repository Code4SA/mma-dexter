from math import sqrt

from itertools import groupby
from datetime import datetime
from dateutil.parser import parse

from dexter.analysis.base import BaseAnalyser, moving_weighted_avg_zscore
from dexter.models import db, Document, DocumentEntity, Person, Utterance, Entity

from sqlalchemy.sql import func, distinct, or_, desc
from sqlalchemy.orm import joinedload


class AnalysedTopic(object):
    pass


class TopicAnalyser(BaseAnalyser):
    """
    Helper that runs analyses on document topics.
    """

    def __init__(self, doc_ids=None, start_date=None, end_date=None):
        super(TopicAnalyser, self).__init__(doc_ids, start_date, end_date)
        self.top_people = None

    def analyse(self):
        self._load_people_mentions()
        self._analyse_people_mentions()

    def _load_people_mentions(self):
        """
        Load all people mentions data for this period.
        """
        rows = db.session.query(distinct(Entity.person_id))\
                .filter(
                        DocumentEntity.doc_id.in_(self.doc_ids),
                        Entity.person_id != None)\
                .join(DocumentEntity, DocumentEntity.entity_id == Entity.id)\
                .all()
        self.people = self._lookup_people([r[0] for r in rows])

    def _analyse_people_mentions(self):
        """
        Do trend analysis on people mentions.
        """
        mention_counts = self.mention_frequencies(self.people.keys())

        self.analysed_people = {}
        for pid, person in self.people.iteritems():
            topic = AnalysedTopic()
            topic.person = person
            topic.mention_counts = mention_counts[pid]
            topic.mention_counts_total = sum(topic.mention_counts)
            self.analysed_people[pid] = topic

        # normalize by total counts per day
        totals = [0] * (self.days+1)

        # first count per-day totals
        for topic in self.analysed_people.itervalues():
            for i, n in enumerate(topic.mention_counts):
                totals[i] += n

        # normalize
        for topic in self.analysed_people.itervalues():
            for i, n in enumerate(topic.mention_counts):
                if totals[i] == 0:
                    topic.mention_counts[i] = 0
                else:
                    topic.mention_counts[i] = 100.0 * n / totals[i]

        # calculate trends
        for topic in self.analysed_people.itervalues():
            topic.mention_counts_trend = moving_weighted_avg_zscore(topic.mention_counts, 0.8)


        # top 20 sources
        self.top_people = sorted(
                self.analysed_people.itervalues(),
                key=lambda s: s.mention_counts_total, reverse=True)[:20]

        # trends
        trending = sorted(
                self.analysed_people.itervalues(),
                key=lambda s: s.mention_counts_trend)

        # top 10 trending up, most trending first
        self.people_trending_up = [s for s in trending[-10:] if s.mention_counts_trend > self.TREND_UP]
        self.people_trending_up.reverse()

        # top 10 trending down, most trending first
        self.people_trending_down = [s for s in trending[:10] if s.mention_counts_trend < self.TREND_DOWN]

    def mention_frequencies(self, ids):
        """
        Return dict from person ID to a list of how frequently each
        person was mentioned per day, over the period.
        """
        rows = db.session.query(
                    Entity.person_id,
                    func.date_format(Document.published_at, '%Y-%m-%d').label('date'),
                    func.count(distinct(DocumentEntity.doc_id)).label('count')
                ) \
                .join(DocumentEntity, Entity.id == DocumentEntity.entity_id) \
                .join(Document, DocumentEntity.doc_id == Document.id) \
                .filter(Entity.person_id.in_(ids))\
                .filter(DocumentEntity.doc_id.in_(self.doc_ids))\
                .group_by(Entity.person_id, 'date')\
                .order_by(Entity.person_id, Document.published_at)\
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
