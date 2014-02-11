from wtforms import StringField, TextAreaField, validators, SelectField, DateField
from wtforms.fields.html5 import URLField

from ..forms import Form

from sqlalchemy import (
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
log = logging.getLogger(__name__)

class Document(db.Model):
    """
    A published document, possibly from online on entered manually.
    """
    __tablename__ = "documents"

    id        = Column(Integer, primary_key=True)
    url       = Column(String(200), index=True, nullable=True)

    title     = Column(String(1024))
    blurb     = Column(String(1024))
    text      = Column(Text)
    section   = Column(String(100), index=True)
    author_entity_id = Column(Integer, ForeignKey('entities.id'))
    medium_id = Column(Integer, ForeignKey('mediums.id'))
    topic_id  = Column(Integer, ForeignKey('topics.id'), index=True)

    published_at = Column(DateTime(timezone=True), index=True, unique=False, nullable=False)
    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # TODO: location

    # Associations
    author      = relationship("Entity", foreign_keys=[author_entity_id])
    entities    = relationship("DocumentEntity", backref=backref('document'), order_by="desc(DocumentEntity.relevance)")
    utterances  = relationship("Utterance", backref=backref('document'))
    keywords    = relationship("DocumentKeyword", backref=backref('document'), order_by="desc(DocumentKeyword.relevance)")
    sources     = relationship("DocumentSource", backref=backref('document'))
    medium      = relationship("Medium")
    topic       = relationship("Topic")


    PLACE_ENTITY_GROUPS = set(['city', 'province_or_state', 'region'])

    def people(self):
        return [e for e in self.entities if e.entity.group == 'person']


    def organisations(self):
        return [e for e in self.entities if e.entity.group == 'organization']


    def places(self):
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
            if s.entity == source.entity:
                return False
                
        self.sources.append(source)
        return True



    def __repr__(self):
        return "<Document id=%s, url=%s>" % (self.id, self.url)


class DocumentForm(Form):
    url         = URLField('URL', [validators.Length(max=200)])
    title       = StringField('Headline', [validators.Required(), validators.Length(max=1024)])
    published_at = DateField('Published on', [validators.Required()], format='%Y/%m/%d')
    blurb       = StringField('Blurb', [validators.Length(max=1024)])
    text        = TextAreaField('Article content', [validators.Required()])

    medium_id   = SelectField('Medium', [validators.Required()])

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)

        from . import Medium
        self.medium_id.choices = [[str(m.id), m.name] for m in Medium.query.all()]
