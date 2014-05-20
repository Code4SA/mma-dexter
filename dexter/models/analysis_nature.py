from sqlalchemy import (
    Column,
    Integer,
    String,
    )

from sqlalchemy.orm import relationship

from .support import db

from wtforms import StringField, TextAreaField, BooleanField, validators, DateTimeField, HiddenField
from ..forms import Form, MultiCheckboxField, IntegerField, SelectField

class ElectionsAnalysisForm(Form):
    """
    Analysis of a document from an elections standpoint.
    """
    topic_id            = SelectField('Topic')
    issues              = MultiCheckboxField('Issues')
    origin_location_id  = SelectField('Origin')

    def __init__(self, *args, **kwargs):
        super(ElectionsAnalysisForm, self).__init__(*args, **kwargs)

        from . import Topic, Location, Issue

        nature = self._obj.analysis_nature

        self.topic_id.choices = [['', '(none)']] + Topic.for_select_widget(nature.topics)
        self.issues.choices = [(str(issue.id), issue.name) for issue in nature.issues]
        self.origin_location_id.choices = [['', '(none)']] + [
                [str(loc.id), loc.name] for loc in Location.query.order_by(Location.name).all()]


class ChildrenAnalysisForm(ElectionsAnalysisForm):
    """
    Analysis of a document from a children standpoint.
    """
    child_focus     = BooleanField('Children are a central focus')


class AnalysisNature(db.Model):
    """
    The type of analysis performed on a document.
    """
    __tablename__ = "analysis_natures"

    ELECTIONS = 1
    CHILDREN  = 2

    FORMS = {
        ELECTIONS: ElectionsAnalysisForm,
        CHILDREN : ChildrenAnalysisForm
    }

    id          = Column(Integer, primary_key=True)
    name        = Column(String(100), nullable=False, index=True, unique=True)

    # associations
    topics      = relationship("Topic", backref="analysis_nature", order_by="Topic.name")
    issues      = relationship("Issue", backref="analysis_nature", order_by="Issue.name")

    @property
    def form(self):
        return self.FORMS[self.id]


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


