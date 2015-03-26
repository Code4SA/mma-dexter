from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Float,
    Index
    )

from ..app import db
from .with_offsets import WithOffsets

class DocumentKeyword(db.Model, WithOffsets):
    """
    A keyword (normally a non-entity keyword) in a document.
    """
    __tablename__ = "document_keywords"

    id        = Column(Integer, primary_key=True)
    doc_id    = Column(Integer, ForeignKey('documents.id', ondelete='CASCADE'), index=True)
    keyword   = Column(String(100), index=True, nullable=False)
    relevance = Column(Float, index=True, nullable=False)

    # offsets in the document, a space-separated list of offset:length pairs.
    offset_list  = Column(String(1024))

    def __repr__(self):
        return "<DocumentKeyword keyword='%s', relevance=%f, doc=%s>" % (
                self.keyword.encode('utf-8'), self.relevance, self.document)

Index('doc_keyword_doc_id_keyword_ix', DocumentKeyword.doc_id, DocumentKeyword.keyword, unique=True)
