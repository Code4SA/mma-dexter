from sqlalchemy import (
    Column,
    Integer,
    String,
    )

from sqlalchemy.orm import relationship

from .support import db

class AnalysisNature(db.Model):
    """
    The type of analysis performed on a document.
    """
    __tablename__ = "analysis_natures"

    ELECTIONS = 1
    CHILDREN  = 2

    id          = Column(Integer, primary_key=True)
    name        = Column(String(100), nullable=False, index=True, unique=True)

    # associations
    topics      = relationship("Topic", backref="analysis_nature", order_by="Topic.name")
    issues      = relationship("Issue", backref="analysis_nature", order_by="Issue.name")

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<AnalysisNature name='%s'>" % (self.name.encode('utf-8'),)


    @classmethod
    def lookup(cls, name):
        return cls.query.filter(cls.name == name).first()

    @classmethod
    def create_defaults(cls):
        elections = AnalysisNature()
        elections.id = cls.ELECTIONS
        elections.name = 'elections'

        children = AnalysisNature()
        children.id = cls.CHILDREN
        children.name = 'children'

        return [elections, children]

    @classmethod
    def all(cls):
        return cls.query.all()
