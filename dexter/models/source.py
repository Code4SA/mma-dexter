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
from .with_offsets import WithOffsets

class DocumentSource(db.Model, WithOffsets):
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
    named        = Column(Boolean)

    # TODO: add role and method of access

    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # Associations
    entity    = relationship("Entity", lazy=False)

    def document_entity(self):
        """ The DocumentEntity instance that matches this source for this document. May be None. """
        for de in self.document.entities:
            if de.entity == self.entity:
                return de
        return None

    def utterances(self):
        """ A potentially empty list of Utterances from this source in this document. """
        return sorted([u for u in self.document.utterances if u.entity == self.entity],
                key=lambda u: u.offset)


    @property
    def offset_list(self):
        """ String of offset:length pairs of places in this document the entity
        is mentioned or quoted, may be empty. """
        offsets = ['%d:%d' % (u.offset, u.length) for u in self.utterances() if u.offset]
        de = self.document_entity()
        if de and de.offset_list:
            offsets.append(de.offset_list)

        return ' '.join(offsets)


    def __repr__(self):
        return "<DocumentSource doc=%s, entity=%s>" % (self.document, self.entity)
