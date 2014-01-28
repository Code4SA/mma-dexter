from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Text,
    func,
    Index
    )
from sqlalchemy.orm import relationship, backref

from .support import Base

class Utterance(Base):
    """
    A quotation by an entity in a document.

    Two instances are equal if they are from the same entity and have the same
    quotation.
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
    entity    = relationship("Entity", lazy=False)

    def __eq__(self, other):
        return isinstance(other, Utterance) and other.entity == self.entity and \
                other.quote == self.quote

    def __str__(self):
        return "<Utterance doc=%s, entity=%s, quote=\"%s\">" % (
                self.document, self.entity, (self.quote or "")[0:15] + "...")
