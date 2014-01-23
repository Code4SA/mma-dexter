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
    url_hash  = Column(String(32), index=True, unique=True, nullable=False)

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
    entities    = relationship("DocumentEntity", backref=backref('document'))
    utterances  = relationship("Utterance", backref=backref('document'))
    keywords    = relationship("DocumentKeyword", backref=backref('document'))

    def __str__(self):
        return "<Document url_hash=%s>" % (self.url_hash)
    

class Entity(Base):
    """
    An entity (person, place etc.) mentioned or quoted in a document.
    """
    __tablename__ = "entities"

    id          = Column(Integer, primary_key=True)
    group       = Column(String(50), index=True, nullable=False)
    name        = Column(String(150), index=True, nullable=False)

    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    def __str__(self):
        return "<Entity group=\"%s\", name=\"%s\">" % (self.group, self.name)

Index('entity_group_name_ix', Entity.group, Entity.name, unique=True)


class DocumentEntity(Base):
    """
    Entities referenced in a document.
    """
    __tablename__ = "document_entities"

    id        = Column(Integer, primary_key=True)
    doc_id    = Column(Integer, ForeignKey('documents.id'), index=True)
    entity_id = Column(Integer, ForeignKey('entities.id'), index=True)
    relevance = Column(Float, index=True, nullable=False)
    count     = Column(Integer, index=True, nullable=False, default=1)

    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # Document Offsets

    # Associations
    entity    = relationship("Entity")

    def __str__(self):
        return "<DocumentEntity doc=%s, entity=%s, relevance=%f, count=%d>" % (
                self.document, self.entity, self.relevance, self.count)

Index('doc_entity_doc_id_entity_id_ix', DocumentEntity.doc_id, DocumentEntity.entity_id, unique=True)


class Utterance(Base):
    """
    A quotation by an entity in a document.
    """
    __tablename__ = "utterances"

    id        = Column(Integer, primary_key=True)
    doc_id    = Column(Integer, ForeignKey('documents.id'), index=True)
    entity_id = Column(Integer, ForeignKey('entities.id'), index=True)
    quote     = Column(Text, nullable=False)

    # TODO: document offsets

    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # Associations
    entity    = relationship("Entity")

    def __str__(self):
        return "<Utterance doc=%s, entity=%s, quote=\"%s\">" % (
                self.document, self.entity, (self.quote or "")[0:15] + "...")


class DocumentKeyword(Base):
    """
    A keyword (normally a non-entity keyword) in a document.
    """
    __tablename__ = "document_keywords"

    id        = Column(Integer, primary_key=True)
    doc_id    = Column(Integer, ForeignKey('documents.id'), index=True)
    keyword   = Column(String(100), index=True, nullable=False)
    relevance = Column(Float, index=True, nullable=False)

    def __str__(self):
        return "<DocumentKeyword doc=%s, keyword=%s, relevance=%f>" % (
                self.document, self.keyword, self.relevance)

Index('doc_keyword_doc_id_keyword_ix', DocumentKeyword.doc_id, DocumentKeyword.keyword, unique=True)
