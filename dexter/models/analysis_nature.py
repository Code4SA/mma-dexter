from sqlalchemy import (
    Column,
    Integer,
    String,
    )

from sqlalchemy.orm import relationship

from .support import db

from wtforms import StringField, TextAreaField, BooleanField, validators, DateTimeField, HiddenField
from ..forms import Form, MultiCheckboxField, IntegerField, SelectField, RadioField, YesNoField

class ElectionsAnalysisForm(Form):
    """
    Analysis of a document from an elections standpoint.
    """
    topic_id            = SelectField('Topic')
    issues              = MultiCheckboxField('Issues')
    origin_location_id  = SelectField('Origin')

    flagged             = BooleanField('Flagged')
    notes               = TextAreaField('Notes')

    def __init__(self, *args, **kwargs):
        super(ElectionsAnalysisForm, self).__init__(*args, **kwargs)

        from . import Topic, Location, Issue

        nature = self._obj.analysis_nature
        country = self._obj.country

        self.topic_id.choices = [['', '(none)']] + Topic.for_select_widget(nature.topics)
        self.issues.choices = [(str(issue.id), issue.name) for issue in nature.issues]
        self.origin_location_id.choices = [['', '(none)']] + [
                [str(loc.id), loc.name] for loc in country.locations()]


class ChildrenAnalysisForm(ElectionsAnalysisForm):
    """
    Analysis of a document from a children standpoint.
    """
    child_focus     = YesNoField('Children are a central focus?', [validators.Optional()])

    quality_basic_context = BooleanField('Basic context')
    quality_causes        = BooleanField('Causes are mentioned')
    quality_policies      = BooleanField('Relevant policies are mentioned')
    quality_solutions     = BooleanField('Solutions are offered')
    quality_consequences  = BooleanField('Consequences are mentioned')
    quality_self_help     = BooleanField('Self-help offered')

    abuse_source         = BooleanField('Child is a source')
    abuse_identified     = BooleanField("Child's identity is disclosed")
    abuse_victim         = BooleanField('Child is a victim of abuse')

    principle_supported_id = RadioField('Principle strongly supported', [validators.Optional()], default='')
    principle_violated_id  = RadioField('Principle clearly violated', [validators.Optional()], default='')

    def __init__(self, *args, **kwargs):
        super(ChildrenAnalysisForm, self).__init__(*args, **kwargs)

        from . import Principle

        principles = Principle.query.all()
        self.principle_descriptions = dict((p.name, p.description) for p in principles)

        self.principle_supported_id.choices = [['', '(none)']] + [(str(p.id), p.name) for p in principles]
        self.principle_violated_id.choices = self.principle_supported_id.choices


    @property
    def quality_fields(self):
        return [
            self.quality_basic_context,
            self.quality_causes,
            self.quality_consequences,
            self.quality_solutions,
            self.quality_policies,
            self.quality_self_help,
        ]

    @property
    def abuse_fields(self):
        return [
            self.abuse_source,
            self.abuse_identified,
            self.abuse_victim,
        ]



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

    ICONS = {
        ELECTIONS: 'fa-university',
        CHILDREN : 'fa-child',
    }

    id          = Column(Integer, primary_key=True)
    name        = Column(String(100), nullable=False, index=True, unique=True)

    # associations
    topics      = relationship("Topic", backref="analysis_nature", order_by="Topic.name")
    issues      = relationship("Issue", backref="analysis_nature", order_by="Issue.name")
    roles       = relationship("SourceRole", backref="analysis_nature", order_by="SourceRole.name")

    @property
    def form(self):
        return self.FORMS[self.id]


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


