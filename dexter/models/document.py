from wtforms import Form, StringField, TextAreaField, validators
from wtforms.fields.html5 import URLField

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

from .support import Base

import logging
log = logging.getLogger(__name__)

class Document(Base):
    """
    A published document, possibly from online on entered manually.
    """
    __tablename__ = "documents"

    id        = Column(Integer, primary_key=True)
    url       = Column(String(200), index=True, unique=True, nullable=False)

    title     = Column(String(1024))
    blurb     = Column(String(1024))
    text      = Column(Text)
    section   = Column(String(100), index=True)

    published_at = Column(DateTime(timezone=True), index=True, unique=False, nullable=False)
    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # TODO: name of publication, eg. M&G
    # TODO: location
    # TODO: author

    # Associations
    entities    = relationship("DocumentEntity", backref=backref('document'), order_by="desc(DocumentEntity.relevance)")
    utterances  = relationship("Utterance", backref=backref('document'))
    keywords    = relationship("DocumentKeyword", backref=backref('document'), order_by="desc(DocumentKeyword.relevance)")


    PLACE_ENTITY_GROUPS = set(['city', 'province_or_state', 'region'])

    def people(self):
        return [e for e in self.entities if e.entity.group == 'person']


    def organisations(self):
        return [e for e in self.entities if e.entity.group == 'organization']


    def places(self):
        return [e for e in self.entities if e.entity.group in Document.PLACE_ENTITY_GROUPS]


    def add_entity(self, doc_entity):
        """ Add a new DocumentEntity to this document, but only
        if the entity doesn't already exist on it."""
        if any(de.entity == doc_entity.entity for de in self.entities):
            return False

        self.entities.append(doc_entity)
        return True

    def add_utterance(self, utterance):
        """ Add a new Utterance, but only if the same one doesn't already
        exist. """
        if any(u == utterance for u in self.utterances):
            return False

        self.utterances.append(utterance)
        return True

    def add_keyword(self, keyword):
        """ Add a new keyword, but only if it's not already there. """
        if any(k.keyword == keyword.keyword for k in self.keywords):
            return False

        self.keywords.append(keyword)
        return True


    def __str__(self):
        return "<Document url=%s>" % (self.url)


class DocumentForm(Form):
    url     = URLField('URL', [validators.Required()])
    title   = StringField('Headline')
    blurb   = StringField('Blurb')
    text    = TextAreaField('Article content')
