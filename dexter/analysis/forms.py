from functools import partial

from wtforms import BooleanField, validators, HiddenField, widgets
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms_alchemy import ModelFieldList

from dexter.forms import ModelForm, FormField, MultiCheckboxField, IntegerField, SelectField, RadioField, YesNoField
from dexter.models import *  # noqa


QueryRadioField = partial(QuerySelectField, widget=widgets.ListWidget(prefix_label=False), option_widget=widgets.RadioInput())


class DocumentSourceForm(ModelForm):
    """ Form for editing a document source. """
    class Meta:
        model = DocumentSource
        only = ['name', 'quoted', 'photographed']
        field_args = {'name': {'label': 'Name'}}

    id          = HiddenField('id', [validators.Optional()])
    deleted     = HiddenField('deleted', default='0')
    person_id   = IntegerField('person_id', widget=widgets.HiddenInput())

    named       = BooleanField('The source is named', default=True)
    source_type = RadioField('Type', default='person', choices=[['person', 'Adult'], ['child', 'Child'], ['secondary', 'Secondary (not a person)']])

    gender      = QueryRadioField('Gender', get_label='name', allow_blank=True, blank_text='?', query_factory=Gender.all)
    race        = QueryRadioField('Race', get_label='name', allow_blank=True, blank_text='?', query_factory=Race.all)

    function    = QuerySelectField('Function', get_label='name', allow_blank=True, blank_text='(none)', query_factory=SourceFunction.all)
    role        = QuerySelectField('Role', get_label='name', allow_blank=True, blank_text='(none)')
    age         = QuerySelectField('Age', get_label='name', allow_blank=True, blank_text='(none)', query_factory=SourceAge.all)
    affiliation = QuerySelectField('Affiliation', get_label='full_name', allow_blank=True, blank_text='(none)')

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

    def is_empty(self):
        return self.is_new() and self.named.data and not self.name.data

    def is_deleted(self):
        return self.deleted.data == '1'

    def validate(self):
        if self.source_type.data == 'person':
            self.role.data = None
            self.age.data = None
            # link to a person
            if self.named.data and self.name.data:
                self.person_id.data = Person.get_or_create(self.name.data).id

        elif self.source_type.data == 'child':
            self.person_id.data = None
            self.function.data = None
            self.affiliation.data = None

        elif self.source_type.data == 'secondary':
            self.person_id.data = None
            self.gender.data = None
            self.race.data = None
            self.role.data = None
            self.age.data = None
            self.named.data = True

        # ignore some data, based on the source type
        if not self.named.data:
            # it's anonymous, so ignore the name field
            self.name.data = None

        return super(DocumentSourceForm, self).validate()

    def populate_obj(self, obj):
        # the form only deals with person_id to make life simpler,
        # so if it's set, also set the person field. Do this
        # before everything else so the race and gender
        # get set on the person directly in the super() call.
        if self.person_id.data:
            obj.person = Person.query.get(self.person_id.data)
            obj.name = None

        super(DocumentSourceForm, self).populate_obj(obj)

        if self.is_new():
            # a newly created source
            obj.manual = True
            obj.id = None

        # the form only deals with person_id to make life simpler,
        # so if it's set, also set the person field
        if obj.person:
            # override the 'quoted' attribute if we know this person has
            # utterances in this document
            if any(obj.person == u.entity.person for u in obj.document.utterances):
                obj.quoted = True

            if not obj.person.gender:
                obj.person.guess_gender_from_doc(obj.document)

        # if it's linked to a person, clear the other crap
        # the form sets
        if obj.named:
            obj.unnamed = False
            obj.unnamed_gender = None
            obj.unnamed_race = None


class DocumentAnalysisForm(ModelForm):
    class Meta:
        model = Document
        only = ['flagged', 'notes']

    sources = ModelFieldList(FormField(DocumentSourceForm))

    def __init__(self, *args, **kwargs):
        # pass the document into the DocumentSourcesForm constructor
        self.sources.args[0].kwargs['form_kwargs'] = {'document': kwargs.get('obj')}

        super(DocumentAnalysisForm, self).__init__(*args, **kwargs)

    @property
    def non_new_sources(self):
        return [s.form for s in self.sources if not s.form.is_new()]

    @property
    def new_sources(self):
        return [s.form for s in self.sources if s.form.is_new()]


class AnchorAnalysisForm(DocumentAnalysisForm):
    """
    Anchor (automated) analysis of a document
    """
    issues = MultiCheckboxField('Issues')
    topic_id = SelectField('Topic')
    origin_location_id = SelectField('Origin')

    def __init__(self, *args, **kwargs):
        super(AnchorAnalysisForm, self).__init__(*args, **kwargs)

        country = self._obj.country
        self.origin_location_id.choices = [['', '(none)']] + [
            [str(loc.id), loc.name] for loc in Location.for_country(country)]

        nature = self._obj.analysis_nature
        self.issues.choices = [(str(issue.id), issue.name) for issue in Issue.for_nature(nature)]
        self.topic_id.choices = [['', '(none)']] + Topic.for_select_widget(Topic.for_nature(nature))


class ElectionsAnalysisForm(AnchorAnalysisForm):
    """
    Analysis of a document from an elections standpoint.
    """
    pass


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
