from dexter.analysis.base import BaseAnalyser
from dexter.models import db, Document, Medium

from sqlalchemy.sql import func, distinct, or_, desc
from sqlalchemy.orm import joinedload


class AnalysedMedium(object):
    pass


class MediaAnalyser(BaseAnalyser):
    """
    Helper that runs analyses on document mediums.
    """

    def __init__(self, doc_ids=None, start_date=None, end_date=None):
        super(MediaAnalyser, self).__init__(doc_ids, start_date, end_date)
        self.media = None

    def analyse(self):
        self._analyse_media()


    def _analyse_media(self):
        media = {m.id: m for m in Medium.query.all()}

        rows = db.session.query(
                    Medium.id,
                    func.count(Document.id))\
                    .join(Document)\
                    .group_by(Medium.id)\
                    .filter(Document.id.in_(self.doc_ids)).all()

        self.media = []
        for id, count in rows:
            # ignore media with too few articles
            if count < 10:
                continue

            m = AnalysedMedium()
            m.medium = media[id]
            m.count = count
            self.media.append(m)

        if self.media:
            biggest = max(m.count for m in self.media)
            for m in self.media:
                m.normalised_count = m.count * 1.0 / biggest

        self.media.sort(key=lambda m: m.count, reverse=True)
