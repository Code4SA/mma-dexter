from sqlalchemy import (
    Column,
    Integer,
    String,
    )

from sqlalchemy.orm import relationship

from ..app import db


class AnalysisNature(db.Model):
    """
    The type of analysis performed on a document.
    """
    __tablename__ = "analysis_natures"

    ELECTIONS = 1
    CHILDREN  = 2
    ANCHOR    = 3

    ICONS = {
        ELECTIONS: 'fa-university',
        CHILDREN : 'fa-child',
        ANCHOR   : 'fa-dot-circle-o',
    }

    id          = Column(Integer, primary_key=True)
    name        = Column(String(100), nullable=False, index=True, unique=True)

    # associations
    roles       = relationship("SourceRole", backref="analysis_nature", order_by="SourceRole.name")

    @property
    def form(self):
        from dexter.analysis.forms import AnchorAnalysisForm, ElectionsAnalysisForm, ChildrenAnalysisForm

        return {
            self.ANCHOR   : AnchorAnalysisForm,
            self.ELECTIONS: ElectionsAnalysisForm,
            self.CHILDREN : ChildrenAnalysisForm,
        }[self.id]


    def icon(self):
        return self.ICONS.get(self.id)


    def __str__(self):
        return self.name


    def __repr__(self):
        return "<AnalysisNature name='%s'>" % (self.name.encode('utf-8'),)


    def __eq__(self, other):
        # when comparing with an int, compare based on id
        if isinstance(other, int):
            return self.id == other
        else:
            return NotImplemented


    def __ne__(self, other):
        # when comparing with an int, compare based on id
        if isinstance(other, int):
            return self.id != other
        else:
            return NotImplemented


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

        anchor = AnalysisNature()
        anchor.id = cls.ANCHOR
        anchor.name = 'anchor'

        return [elections, children, anchor]

    @classmethod
    def all(cls):
        return cls.query.all()


