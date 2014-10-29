from math import sqrt
from datetime import datetime

from dexter.models import db, Document, Person

from sqlalchemy.sql import func
from sqlalchemy.orm import joinedload


class BaseAnalyser(object):
    """
    Base for analyser objects that handles a collection of
    documents to analyse, based on either document ids
    or start and end dates.
    """

    TREND_UP = 0.5
    TREND_DOWN = -0.5

    def __init__(self, doc_ids=None, start_date=None, end_date=None):
        self.doc_ids = doc_ids
        self.start_date = start_date
        self.end_date = end_date

        # we need either a date range or document ids, fill in
        # whichever is missing
        self._calculate_date_range()
        self._fetch_doc_ids()

        self.n_documents = len(self.doc_ids)

    def _calculate_date_range(self):
        """
        The date range is the range of publication dates for the given
        documents.
        """
        if not self.start_date or not self.end_date:
            if self.doc_ids is None:
                raise ValueError("Need either doc_ids, or both start_date and end_date")

            row = db.session.query(
                func.min(Document.published_at),
                func.max(Document.published_at))\
                .filter(Document.id.in_(self.doc_ids))\
                .first()

            if row and row[0]:
                self.start_date = row[0].date()
                self.end_date = row[1].date()
            else:
                self.start_date = self.end_date = datetime.utcnow()

        self.days = max((self.end_date - self.start_date).days, 1)

    def _fetch_doc_ids(self):
        if self.doc_ids is None:
            rows = db.session.query(Document.id)\
                .filter(Document.published_at >= self.start_date.strftime('%Y-%m-%d 00:00:00'))\
                .filter(Document.published_at <= self.end_date.strftime('%Y-%m-%d 23:59:59'))\
                .all()
            self.doc_ids = [r[0] for r in rows]

    def _lookup_people(self, ids):
        query = Person.query \
            .options(joinedload(Person.affiliation)) \
            .filter(Person.id.in_(ids))

        return dict([p.id, p] for p in query.all())


def moving_weighted_avg_zscore(obs, decay=0.8):
    """
    Calculate a moving-weighted average z-score, based on +obs+,
    a list of observations, and +decay+, the rate at which
    observations decay.

    See http://stackoverflow.com/questions/787496/what-is-the-best-way-to-compute-trending-topics-or-tags
    See http://pandas.pydata.org/pandas-docs/stable/generated/pandas.ewma.html#pandas.ewma
    """
    avg = 0.0
    sq_avg = 0.0

    last = len(obs)-1

    for i, x in enumerate(obs):
        if i == 0:
            # first item
            avg = float(x)
            sq_avg = float(x ** 2)

        elif i == last:
            # basic std deviation
            std = sqrt(sq_avg - avg ** 2)
            if std == 0:
                return x - avg
            else:
                return (x - avg) / std
        else:
            # fold it in
            avg = avg * decay + (1.0-decay) * x
            sq_avg = sq_avg * decay + (1.0-decay) * (x ** 2)