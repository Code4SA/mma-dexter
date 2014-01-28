from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Float,
    func,
    Index
    )
from sqlalchemy.orm import relationship

from .support import Base

class Entity(Base):
    """
    An entity (person, place etc.) mentioned or quoted in a document.

    Two instances are equal if they have the same name and group.
    """
    __tablename__ = "entities"

    id          = Column(Integer, primary_key=True)
    group       = Column(String(50), index=True, nullable=False)
    name        = Column(String(150), index=True, nullable=False)

    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    def __eq__(self, other):
        return isinstance(other, Entity) and self.group == other.group \
            and self.name == other.name

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
    entity    = relationship("Entity", lazy=False)

    def __str__(self):
        return "<DocumentEntity doc=%s, entity=%s, relevance=%f, count=%d>" % (
                self.document, self.entity, self.relevance, self.count)

Index('doc_entity_doc_id_entity_id_ix', DocumentEntity.doc_id, DocumentEntity.entity_id, unique=True)
