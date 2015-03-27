from __future__ import division

from unidecode import unidecode

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

from ..app import db
from ..utils import levenshtein

class Utterance(db.Model):
    """
    A quotation by an entity in a document.

    Two instances are equal if they are from the same entity and have the same
    quotation.
    """
    __tablename__ = "utterances"

    id        = Column(Integer, primary_key=True)
    doc_id    = Column(Integer, ForeignKey('documents.id', ondelete='CASCADE'), index=True)
    entity_id = Column(Integer, ForeignKey('entities.id'), index=True)
    quote     = Column(Text, nullable=False)

    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # Associations
    entity    = relationship("Entity", lazy=False)

    # offset and length of quotation in the document
    offset    = Column(Integer)
    length    = Column(Integer)


    def similarity(self, other):
        """ Return a similarity ratio of two quotes. 0 means the strings are not similar at all,
        1.0 means they're identical. """
        return levenshtein(self.quote, other.quote)

    def snippet(self, mark=True, context=150):
        """ Get a snippet from the document surrounding this utterance.
        If `mark` is True, then surround it with <mark> tags.
        """
        if self.offset is None or self.length is None:
            return None

        start = max(0, self.offset-context)
        quote_end = self.offset + self.length
        end   = min(len(self.document.text), quote_end + context)

        if start > 0:
            # find the first space
            start = max(start, self.document.text.find(' ', start, self.offset))

        if end < len(self.document.text):
            # find the first space
            end = max(quote_end, self.document.text.rfind(' ', quote_end, end))

        if mark:
            snippet = '%s<mark>%s</mark>%s' % (
                    self.document.text[start:self.offset],
                    self.document.text[self.offset:quote_end],
                    self.document.text[quote_end:end]
                    )
        else:
            snippet = self.document.text[start:end]

        if start > 0:
            snippet = "... " + snippet
        if end < len(self.document.text):
            snippet = snippet + " ..."

        return snippet


    def __eq__(self, other):
        # to compare, we emulate mysql's utf8_general_ci collation:
        # strip diacritics and lowercase
        return isinstance(other, Utterance) and other.entity == self.entity and \
                (unidecode(other.quote).lower() == unidecode(self.quote).lower() or self.similarity(other) >= 0.8)

    def __repr__(self):
        return "<Utterance doc=%s, entity=%s, quote=\"%s\">" % (
                self.document, self.entity, (self.quote or "").encode('utf-8')[0:15] + "...")
