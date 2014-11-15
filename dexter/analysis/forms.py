from wtforms import StringField, TextAreaField, BooleanField, validators, DateTimeField, HiddenField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms_alchemy import ModelFieldList

from dexter.forms import ModelForm, FormField, MultiCheckboxField, IntegerField, SelectField, RadioField, YesNoField
from dexter.models import *


class DocumentSourceForm(ModelForm):
    """ Form for editing a document source. """
    class Meta:
        model = DocumentSource
        only = ['id', 'name', 'quoted', 'photographed']

    deleted     = BooleanField('deleted')

    named       = BooleanField('The source is named', default=True)
    source_type = RadioField('Type', default='person', choices=[['person', 'Adult'], ['child', 'Child'], ['secondary', 'Secondary (not a person)']])
    gender      = QuerySelectField('Gender', get_label='name', allow_blank=True, query_factory=Gender.all)
    race        = QuerySelectField('Race', get_label='name', allow_blank=True, query_factory=Race.all)
    function    = QuerySelectField('Function', get_label='name', allow_blank=True, query_factory=SourceFunction.all)
    role        = QuerySelectField('Role', get_label='name', allow_blank=True)
    age         = QuerySelectField('Age', get_label='name', allow_blank=True, query_factory=SourceAge.all)
    affiliation = QuerySelectField('Affiliation', get_label='name', allow_blank=True)


    def __init__(self, document, *args, **kwargs):
        self.role.kwargs['query_factory'] = lambda: document.analysis_nature.roles
        self.affiliation.kwargs['query_factory'] = lambda: Affiliation.organisations(document.country)
        super(DocumentSourceForm, self).__init__(*args, **kwargs)

    @property
    def source(self):
        """ the associated source object, if any """
        return self._obj


    def is_new(self):
        return self.source is None


    def validate(self):
        # ignore some data, based on the source type
        if not self.named.data:
            # it's anonymous, so ignore the name field
            self.name.data = ''

        if self.source_type.data == 'person':
            self.role.data = None
            self.age.data = None

        elif self.source_type.data == 'child':
            self.function.data = None
            self.affiliation.data = None

        elif self.source_type.data == 'secondary':
            self.gender.data = None
            self.race.data = None
            self.role.data = None
            self.age.data = None

        return super(DocumentSourceForm, self).validate()


    def populate_obj(self, obj):
        super(DocumentSourceForm, self).populate_obj(obj)

        # TODO: move this into DocumentSource itself
        if obj.unnamed or obj.person_id:
            obj.name = None

        # if it's linked to a person, clear the other crap
        # the form sets
        # TODO: is this being duped by above?
        if obj.named:
            obj.unnamed = False
            obj.unnamed_gender_id = None
            obj.unnamed_race_id = None

        # TODO: do this correctly
        if self.name.data:
            obj.person = Person.get_or_create(self.name.data)

        # TODO: handle person creation

        if obj.id is None:
            # a newly created source
            obj.manual = True


class DocumentAnalysisForm(ModelForm):
    class Meta:
        model = Document
        only = ['flagged', 'notes']

    sources = ModelFieldList(FormField(DocumentSourceForm))

    def __init__(self, *args, **kwargs):
        # pass the document into the DocumentSourcesForm constructor
        self.sources.args[0].kwargs['form_kwargs'] = {'document': kwargs.get('obj')}

        super(DocumentAnalysisForm, self).__init__(*args, **kwargs)


class AnchorAnalysisForm(DocumentAnalysisForm):
    """
    Anchor (automated) analysis of a document
    """
    pass


class ElectionsAnalysisForm(AnchorAnalysisForm):
    """
    Analysis of a document from an elections standpoint.
    """
    topic_id            = SelectField('Topic')
    issues              = MultiCheckboxField('Issues')
    origin_location_id  = SelectField('Origin')

    def __init__(self, *args, **kwargs):
        super(ElectionsAnalysisForm, self).__init__(*args, **kwargs)

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


