from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Boolean,
    Integer,
    String,
    func,
    )
from sqlalchemy.orm import relationship

from .support import db

class DocumentSource(db.Model):
    """
    A source is a source of information for an article.
    A source instance is bound to a document and an entity and describes the
    role in which the source was accessed, how they were accessed, etc.
    """
    __tablename__ = "document_sources"

    id        = Column(Integer, primary_key=True)
    doc_id    = Column(Integer, ForeignKey('documents.id'), index=True, nullable=False)
    entity_id = Column(Integer, ForeignKey('entities.id'), index=True)

    photographed = Column(Boolean)
    quoted       = Column(Boolean)

    # TODO: add role and method of access

    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # Associations
    entity    = relationship("Entity", lazy=False)


    def __repr__(self):
        return "<DocumentSource doc=%s, entity=%s>" % (self.document, self.entity)
