from __future__ import division

import re
import datetime

from wtforms import StringField, TextAreaField, validators, DateTimeField, HiddenField
from wtforms.fields.html5 import URLField

from ..forms import Form, MultiCheckboxField, IntegerField, SelectField

from sqlalchemy import (
    Table,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Float,
    Text,
    func,
    Index
    )
from sqlalchemy.orm import relationship, backref
from .support import db

import logging


universal_newline_re = re.compile(R"\r\n|\n|\r")  # All types of newline.
newlines_re = re.compile(R"\n+")

class Document(db.Model):
    """
    A published document, possibly from online on entered manually.
    """
    __tablename__ = "documents"
    log = logging.getLogger(__name__)

    id        = Column(Integer, primary_key=True)
    url       = Column(String(200), index=True, nullable=True)

    title     = Column(String(1024))
    summary   = Column(String(1024))
    text      = Column(Text)
    section   = Column(String(100), index=True)
    item_num  = Column(Integer)

    author_id         = Column(Integer, ForeignKey('authors.id'), index=True)
    medium_id         = Column(Integer, ForeignKey('mediums.id'), index=True)
    topic_id          = Column(Integer, ForeignKey('topics.id'), index=True)
    document_type_id  = Column(Integer, ForeignKey('document_types.id'), index=True)
    origin_location_id = Column(Integer, ForeignKey('locations.id'), index=True)

    created_by_user_id = Column(Integer, ForeignKey('users.id'), index=True)
    checked_by_user_id = Column(Integer, ForeignKey('users.id'), index=True)

    published_at = Column(DateTime(timezone=True), index=True, unique=False, nullable=False)
    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # Associations
    author      = relationship("Author")
    entities    = relationship("DocumentEntity", backref=backref('document'), cascade='all, delete-orphan', passive_deletes=True, order_by="desc(DocumentEntity.relevance)")
    utterances  = relationship("Utterance", backref=backref('document'), cascade='all', passive_deletes=True)
    keywords    = relationship("DocumentKeyword", backref=backref('document'), cascade='all', passive_deletes=True, order_by="desc(DocumentKeyword.relevance)")
    sources     = relationship("DocumentSource", backref=backref('document'), cascade='all, delete-orphan', passive_deletes=True)
    fairness    = relationship("DocumentFairness", backref=backref('document'), cascade='all, delete-orphan', passive_deletes=True)
    places      = relationship("DocumentPlace", backref=backref('document'), cascade='all, delete-orphan', passive_deletes=True)
    issues      = relationship("Issue", secondary='document_issues', passive_deletes=True)
    medium      = relationship("Medium")
    topic       = relationship("Topic")
    document_type = relationship("DocumentType")
    origin      = relationship("Location")
    created_by  = relationship("User", backref=backref('created_documents'), foreign_keys=[created_by_user_id])
    checked_by  = relationship("User", backref=backref('checked_documents'), foreign_keys=[checked_by_user_id])


    PLACE_ENTITY_GROUPS = set(['city', 'province_or_state', 'region'])

    def people(self):
        return [e for e in self.entities if e.entity.group == 'person']


    def organisations(self):
        return [e for e in self.entities if e.entity.group == 'organization']


    def place_entities(self):
        return [e for e in self.entities if e.entity.group in Document.PLACE_ENTITY_GROUPS]


    def mentioned_entity(self, entity):
        """ Get the DocumentEntity for this entity, if any. """
        for de in self.entities:
            if de.entity == entity:
                return de
        return None


    def add_entity(self, doc_entity):
        """ Add a new DocumentEntity to this document, but only
        if the entity and the specific offsets don't already exist on it. """
        for de in self.entities:
            if de.entity == doc_entity.entity:
                return de.add_offsets(doc_entity.offsets())

        self.entities.append(doc_entity)
        return True

    def add_utterance(self, utterance):
        """ Add a new Utterance, but only if the same one doesn't already
        exist. """
        for u in self.utterances:
            if u == utterance:
                if utterance.offset is not None and u.offset is None:
                    u.offset = utterance.offset
                    u.length = utterance.length
                    return True
                else:
                    return False

        self.utterances.append(utterance)
        return True

    def add_keyword(self, keyword):
        """ Add a new keyword, but only if it's not already there. """
        for k in self.keywords:
            if k.keyword.lower() == keyword.keyword.lower():
                return k.add_offsets(keyword.offsets())
                
        self.keywords.append(keyword)
        return True

    def add_source(self, source):
        """ Add a new source, but only if it's not already there. """
        for s in self.sources:
            if s.person == source.person:
                return False
                
        self.sources.append(source)
        return True


    def add_place(self, doc_place):
        """ Add a new DocumentPlace to this document, but only
        if it doesn't already exist."""
        for dp in self.places:
            if dp.place == doc_place.place:
                return False

        self.places.append(doc_place)
        return True


    def normalise_text(self):
        """ Run some normalisations on the document. """
        if self.text:
            # normalise newlines
            # first ensure they're all \n
            self.text = universal_newline_re.sub("\n", self.text)
            # now ensure all \n's are double
            self.text = newlines_re.sub("\n\n", self.text)


    def can_user_edit(self, user):
        return user.admin or self.created_by is None or self.created_by == user


    def relearn_source_affiliations(self):
        """ Update the default affiilations for people sources linked to this
        document.
        """
        people = set()
        for source in (s for s in self.sources if s.person):
            if source.affiliation is not None and source.affiliation != source.person.affiliation:
                people.add(source.person)

        self.log.debug("Relearning source affiliations for %s", people)

        for person in people:
            person.relearn_affiliation()


    def analysis_problems(self):
        """ A list of problems (possibly empty) for critical things
        missing from this document. """
        return DocumentAnalysisProblem.for_document(self)


    def is_fair(self):
        return not self.fairness or (len(self.fairness) == 1 and self.fairness[0].fairness.name == 'Fair')

    
    def get_places(self, relevant=True):
        """
        Get a list of DocumentPlace instances for this document. If relevant is
        true, only fetch those that are relevant.
        """
        return [dp for dp in self.places if not relevant or dp.relevant]


    def places_relevance_threshold(self):
        # calculate threshold as average of all non-None relevances
        count = 0
        sum = 0
        for dp in self.places:
            if dp.relevance is not None:
                count += 1
                sum += dp.relevance
        return sum/count if count > 0 else 0


    def __repr__(self):
        return "<Document id=%s, url=%s>" % (self.id, self.url)


class DocumentForm(Form):
    url         = URLField('URL', [validators.Length(max=200)])
    title       = StringField('Headline', [validators.Required(), validators.Length(max=1024)])
    published_at = DateTimeField('Published/broadcast on', [validators.Required()], format='%Y/%m/%d %H:%M')
    summary     = TextAreaField('Summary', [validators.Length(max=1024)])
    text        = TextAreaField('Article content')
    item_num    = IntegerField('Item no', [validators.Optional(), validators.NumberRange(min=1, max=100)])

    medium_id           = SelectField('Medium', [validators.Required()])
    document_type_id    = SelectField('Type', [validators.Required()], default=1)
    author_id           = HiddenField()

    def __init__(self, *args, **kwargs):
        self.published_at.data = datetime.datetime.utcnow()

        super(DocumentForm, self).__init__(*args, **kwargs)

        from . import Medium, DocumentType

        self.medium_id.choices = [['', '(none)']] + [[str(m.id), m.name] for m in Medium.query.order_by(Medium.name).all()]
        self.document_type_id.choices = [[str(t.id), t.name] for t in DocumentType.query.order_by(DocumentType.name).all()]


class DocumentType(db.Model):
    """
    Nature of the document.
    """
    __tablename__ = "document_types"

    id        = Column(Integer, primary_key=True)
    name      = Column(String(100), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<DocumentType name='%s'>" % (self.name.encode('utf-8'),)

    @classmethod
    def create_defaults(self):
        text = """
        News story
        In brief/short
        Cartoon/graphic
        Editorial
        Opinion piece
        Feature/news analysis
        Business
        Sport
        Photograph
        Opinion poll
        Interview
        Panel discussion
        Phone-in programme/talk
        Documentary insert
        Current affairs
        Special elections programme
        Other (Last Resort)
        """

        types = []
        for s in text.strip().split("\n"):
            t = DocumentType()
            t.name = s.strip()
            types.append(t)

        return types


class DocumentAnalysisForm(Form):
    topic_id            = SelectField('Topic')
    issues              = MultiCheckboxField('Issues')
    origin_location_id  = SelectField('Origin')

    def __init__(self, *args, **kwargs):
        super(DocumentAnalysisForm, self).__init__(*args, **kwargs)

        from . import Topic, Location, Issue

        self.topic_id.choices = [['', '(none)']] + [[str(t.id), t.name] for t in Topic.query.order_by(Topic.name).all()]
        self.issues.choices = [(str(issue.id), issue.name) for issue in db.session.query(Issue).order_by('name')]
        self.origin_location_id.choices = [['', '(none)']] + [
                [str(loc.id), loc.name] for loc in Location.query.order_by(Location.name).all()]


class DocumentAnalysisProblem(object):
    """
    A helper class that describes a problem with a document's analysis.
    It has support for filtering SQL queries to find documents with that
    problem, describing the problem, etc.
    """
    _problems = {}

    def check(self, doc):
        raise NotImplementedError()

    def filter_query(self, query):
        raise NotImplementedError()

    @classmethod
    def all(cls):
        if not cls._problems:
            cls._problems = dict((k.code, k()) for k in cls.__subclasses__())
        return sorted(cls._problems.values(), key=lambda k: k.short_desc)

    @classmethod
    def for_document(cls, doc):
        return [p for p in cls.all() if p.check(doc)]

    @classmethod
    def for_select(cls):
        return [[k.code, k.short_desc] for k in cls.all()]

    @classmethod
    def lookup(cls, key):
        return cls._problems[key]


class MissingTopic(DocumentAnalysisProblem):
    code = 'missing-topic'
    short_desc = 'missing a topic'
    long_desc  = 'This document is missing a topic.'

    def check(self, doc):
        return doc.topic is None

    def filter_query(self, query):
        return query.filter(Document.topic == None)


class MissingOrigin(DocumentAnalysisProblem):
    code = 'missing-origin'
    short_desc = 'missing an origin'
    long_desc  = 'This document is missing an origin.'

    def check(self, doc):
        return doc.origin is None

    def filter_query(self, query):
        return query.filter(Document.origin == None)


class SourceWithoutFunction(DocumentAnalysisProblem):
    code = 'source-without-function'
    short_desc = 'source without a function'
    long_desc  = 'This document has a source without a function.'

    def check(self, doc):
        return any(ds.source_function_id is None for ds in doc.sources)

    def filter_query(self, query):
        from . import DocumentSource
        return query\
                .join(DocumentSource)\
                .filter(DocumentSource.function == None)


class SourceWithoutAffiliation(DocumentAnalysisProblem):
    code = 'source-without-affiliation'
    short_desc = 'source without an affiliation'
    long_desc  = 'This document has a source without an affiliation.'

    def check(self, doc):
        return any(ds.affiliation_id is None for ds in doc.sources)

    def filter_query(self, query):
        from . import DocumentSource
        return query\
                .join(DocumentSource)\
                .filter(DocumentSource.affiliation == None)
