from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Float,
    Index
    )

from .support import db
from .with_offsets import WithOffsets

class DocumentKeyword(db.Model, WithOffsets):
    """
    A keyword (normally a non-entity keyword) in a document.
    """
    __tablename__ = "document_keywords"

    id        = Column(Integer, primary_key=True)
    doc_id    = Column(Integer, ForeignKey('documents.id'), index=True)
    keyword   = Column(String(100), index=True, nullable=False)
    relevance = Column(Float, index=True, nullable=False)

    # offsets in the document, a space-separated list of offset:length pairs.
    offset_list  = Column(String(1024))

    def __repr__(self):
        return "<DocumentKeyword keyword='%s', relevance=%f, doc=%s>" % (
                self.keyword.encode('utf-8'), self.relevance, self.document)

Index('doc_keyword_doc_id_keyword_ix', DocumentKeyword.doc_id, DocumentKeyword.keyword, unique=True)

class Topic(db.Model):
    """
    Primary topic for an article.
    """
    __tablename__ = "topics"

    id        = Column(Integer, primary_key=True)
    name      = Column(String(100), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<Topic name='%s'>" % (self.name.encode('utf-8'),)

    @classmethod
    def create_defaults(self):
        text = """
        2/3 majority
        Coalitions and party co-operation
        Election Fraud
        Election funding
        IEC/Election Logistics
        Opinion Polls
        Party manifesto outline or analyses
        Party politics(internal and/or external)
        Political party campaigning (only when no other code applies)
        Political Violence & Intimidation
        Service Delivery
        Voter Education & registration
        Affirmative Action
        Arts/Culture/Entertainment/Religion
        Black Economic Empowerment
        Children/Child Abuse
        Corruption Govt & party
        Crime
        Death Penalty
        Diplomacy
        Gender Based Violence
        HIV/Aids
        Housing
        International Politics
        Justice System
        Land
        Personalities and Profiles
        Poverty
        Race & Racism
        Refugees
        War on Terror & Terrorism
        Corruption, general
        Demonstrations
        Development
        Disaster
        Economics
        Education
        Environment
        Gender
        Health
        Human Rights
        Labour, Strikes, Unemployment
        Media
        Science
        Sport
        Other (Last Resort)
        """

        topics = []
        for s in text.strip().split("\n"):
            g = Topic()
            g.name = s.strip()
            topics.append(g)

        return topics
