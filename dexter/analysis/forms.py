from wtforms import StringField, TextAreaField, BooleanField, validators, DateTimeField, HiddenField

from dexter.forms import Form, MultiCheckboxField, IntegerField, SelectField, RadioField, YesNoField
from dexter.models import *

class AnchorAnalysisForm(Form):
    """
    Anchor (automated) analysis of a document
    """
    flagged             = BooleanField('Flagged')
    notes               = TextAreaField('Notes')


class ElectionsAnalysisForm(AnchorAnalysisForm):
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
        country = self._obj.country

        self.topic_id.choices = [['', '(none)']] + Topic.for_select_widget(nature.topics)
        self.issues.choices = [(str(issue.id), issue.name) for issue in nature.issues]
        self.origin_location_id.choices = [['', '(none)']] + [
                [str(loc.id), loc.name] for loc in Location.for_country(country)]


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


