from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Float,
    Index
    )

from .support import Base

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
