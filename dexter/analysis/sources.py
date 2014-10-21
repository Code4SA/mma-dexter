from dexter.models import db, Document, DocumentSource, Person, Utterance, Entity

from sqlalchemy.sql import func, distinct, or_, desc
from sqlalchemy.orm import joinedload

class AnalyzedSource(object):
    pass

class SourceAnalyzer(object):
    """
    Helper that runs analyses on document sources.
    """
    def __init__(self, form):
        self.form = form
        self.doc_ids = form.document_ids()

        self.top_people = None

        # max results for most analyses
        self.row_limit = 100


    def analyze(self):
        self._analyze_top_people()


    def _analyze_top_people(self):
        """
        Calculate top people for these documents, storing the results in
        `top_sources`.
        Top people are those people who were sources the most over a period.
        """
        sources = []
        query = db.session.query(
                DocumentSource.person_id,
                func.count(DocumentSource.person_id).label('count')
                )\
                .filter(
                        DocumentSource.doc_id.in_(self.doc_ids),
                        DocumentSource.person_id != None)\
                .group_by(DocumentSource.person_id)\
                .order_by(desc('count'))\
                .limit(self.row_limit)

        rows = query.all()

        people = self._lookup_people([r[0] for r in rows])
        utterance_count = self._count_utterances(people.keys())

        for row in (r._asdict() for r in query.all()):
            src = AnalyzedSource()
            src.person = people[row['person_id']]
            src.count = row['count']
            src.utterance_count = utterance_count.get(src.person.id, 0)
            sources.append(src)

        self.top_people = sources


    def _lookup_people(self, ids):
        query = Person.query\
                .options(joinedload(Person.affiliation))\
                .filter(Person.id.in_(ids))

        return dict([p.id, p] for p in query.all())

    def _count_utterances(self, ids):
        """
        Return dict from person ID to number of utterances they had in
        these documents.
        """
        rows = db.session.query(
                Person.id,
                func.count(Utterance.id).label('count')
                )\
                .join(Entity, Entity.person_id == Person.id)\
                .join(Utterance, Utterance.entity_id == Entity.id)\
                .filter(Utterance.doc_id.in_(self.doc_ids))\
                .filter(Person.id.in_(ids))\
                .all()

        return dict((p.id, p[1]) for p in rows)
