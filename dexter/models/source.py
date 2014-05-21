from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Boolean,
    Integer,
    String,
    func,
    event,
    )
from sqlalchemy.orm import relationship
from wtforms import StringField, validators, HiddenField, BooleanField, RadioField

from .support import db
from .with_offsets import WithOffsets
from ..forms import Form, SelectField

class DocumentSource(db.Model, WithOffsets):
    """
    A source is a source of information for an article.
    A source can be one of:

     - a named person (linked via person_id)
     - an unnamed person (in which case gender_id and race_id are meaningful)
     - a non-person secondary source (only name is applicable)
    """
    __tablename__ = "document_sources"

    id        = Column(Integer, primary_key=True)
    doc_id    = Column(Integer, ForeignKey('documents.id', ondelete='CASCADE'), index=True, nullable=False)

    # The type of this source. This impacts which other fields are valid and how they're interpreted.
    # 
    # person:
    #   - if unnamed is False, then
    #     - person_id is valid and links to the person
    #   - if unnamed is True, then
    #     - person_id is not valid
    #     - unnamed_* are all valid
    #   - source_function and affiliation are valid
    #   - quoted is valid
    #   - everything else (role, age, etc.) are ignored
    #
    # child:
    #   - unnamed is valid and, if False, 'name' has the source name
    #   - race and gender are valid
    #   - age and role are valid
    #   - quoted is alid
    #   - affiliation and function are ignored
    #
    # secondary:
    #   - only name, affiliation and function are valid
    source_type = Column(String(50), nullable=False, default='person')

    person_id = Column(Integer, ForeignKey('people.id', ondelete='CASCADE'), index=True)

    # if this is True, then person_id is ignored and this is an anonymous source
    unnamed           = Column(Boolean, default=False)
    unnamed_gender_id = Column(Integer, ForeignKey('genders.id'))
    unnamed_race_id   = Column(Integer, ForeignKey('races.id'))

    # if unnamed is False and person_id is null, then this is a secondary, named source
    name         = Column(String(100))

    source_function_id = Column(Integer, ForeignKey('source_functions.id', ondelete='SET NULL'))
    source_role_id     = Column(Integer, ForeignKey('source_roles.id', ondelete='SET NULL'))
    source_age_id      = Column(Integer, ForeignKey('source_ages.id', ondelete='SET NULL'))

    quoted       = Column(Boolean)

    # was this source added manually or was it inferred by machine learning?
    manual       = Column(Boolean, default=False, nullable=False)

    # who is the person affiliated with?
    affiliation_id = Column(Integer, ForeignKey('affiliations.id', ondelete='SET NULL'), index=True)

    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # Associations
    person      = relationship("Person", foreign_keys=[person_id], lazy=False)
    function    = relationship("SourceFunction", lazy=False)
    affiliation = relationship("Affiliation", lazy=False)
    role        = relationship("SourceRole", lazy=False)
    age         = relationship("SourceAge", lazy=False)
    unnamed_gender = relationship("Gender", lazy=False)
    unnamed_race   = relationship("Race", lazy=False)

    def document_entities(self):
        """ List of DocumentEntity instances that matches this source for this document. May be empty. """
        if not self.person:
            return []
        return [de for de in self.document.entities if de.entity.person == self.person]

    def utterances(self):
        """ A potentially empty list of Utterances from this source in this document. """
        return sorted([u for u in self.document.utterances if self.person and u.entity.person == self.person],
                key=lambda u: u.offset)


    def friendly_name(self):
        if self.person:
            return self.person.name

        if self.unnamed:
            return 'Unnamed'

        return self.name or '(none)'


    def sort_key(self):
        return [not self.manual, self.friendly_name()]


    def gender(self):
        if self.person:
            return self.person.gender
        return self.unnamed_gender

    def race(self):
        if self.person:
            return self.person.race
        return self.unnamed_race


    @property
    def offset_list(self):
        """ String of offset:length pairs of places in this document the entity
        is mentioned or quoted, may be empty. """
        offsets = ['%d:%d' % (u.offset, u.length) for u in self.utterances() if u.offset]
        for de in self.document_entities():
            if de.offset_list:
                offsets.append(de.offset_list)

        return ' '.join(offsets)


    def __repr__(self):
        return "<DocumentSource doc=%s, person=%s, unnamed=%s, name='%s'>" % (self.document, self.person, self.unnamed, self.name.encode('utf-8'))


@event.listens_for(DocumentSource.source_type, 'set')
def source_type_set(target, value, oldvalue, initiator):
    if value == 'person':
        target.source_role_id = None
        target.source_age_id = None

    elif value == 'child':
        target.person = None

    elif value == 'secondary':
        target.person = None
        target.unnamed_gender_id = None
        target.unnamed_race_id = None
        target.source_role_id = None
        target.source_age_id = None


class SourceFunction(db.Model):
    """
    In what role/function was the source for a document accessed?
    """
    __tablename__ = "source_functions"

    id        = Column(Integer, primary_key=True)
    name      = Column(String(50), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<SourceFunction name='%s'>" % (self.name)


    @classmethod
    def create_defaults(self):
        text = """
        Do not know
        Subject
        Expert
        Personal Experience
        Eye Witness
        Popular Opinion
        Secondary Sources
        Representative/Spokesperson
        Other
        """

        functions = []
        for s in text.strip().split("\n"):
            g = SourceFunction()
            g.name = s.strip()
            functions.append(g)

        return functions


def none_coerce(v):
    from wtforms.compat import text_type
    return text_type('' if v is None else v)


class DocumentSourceForm(Form):
    name              = StringField('Name', [validators.Length(max=100)])
    unnamed           = BooleanField('Anonymous', [validators.Optional()], default=False)
    unnamed_gender_id = SelectField('Gender', [validators.Optional()], default='', coerce=none_coerce)
    unnamed_race_id   = SelectField('Race', [validators.Optional()], default='', coerce=none_coerce)

    source_type       = RadioField('Type', default='person', choices=[['person', 'Person/Adult'], ['child', 'Child'], ['secondary', 'Secondary (not person)']])

    quoted            = BooleanField('Quoted', default=False)

    source_function_id  = SelectField('Function', default='')
    source_role_id      = SelectField('Role', default='')
    source_age_id       = SelectField('Age', default='')
    affiliation_id      = SelectField('Affiliation', default='')

    deleted           = HiddenField('deleted', default='0')

    def __init__(self, *args, **kwargs):
        super(DocumentSourceForm, self).__init__(*args, **kwargs)

        from . import SourceAge

        if 'nature' in kwargs:
            nature = kwargs['nature']
        elif self.source:
            nature = self.source.document.analysis_nature
        else:
            raise ArgumentError("Missing analysis nature. Either pass in obj or nature")


        self.source_function_id.choices = [['', '(none)']] + [[str(s.id), s.name] for s in SourceFunction.query.order_by(SourceFunction.name).all()]
        self.source_role_id.choices = [['', '(none)']] + [[str(s.id), s.name] for s in nature.roles]
        self.source_age_id.choices = [['', '(none)']] + [[str(s.id), s.name] for s in SourceAge.query.order_by(SourceAge.name).all()]

        from . import Gender, Race
        self.unnamed_gender_id.choices = [['', '(unknown gender)']] + [[str(g.id), g.name] for g in Gender.query.order_by(Gender.name).all()]
        self.unnamed_race_id.choices = [['', '(unknown race)']] + [[str(r.id), r.name] for r in Race.query.order_by(Race.name).all()]

        # because this list is heirarchical, we class 'organisations' as
        # this with only 0 or two dots
        from . import Affiliation
        orgs = [i for i in Affiliation.query.all() if i.code.count('.') <= 1]
        orgs.sort(key=Affiliation.sort_key)
        self.affiliation_id.choices = [['', '(none)']] + [[str(s.id), s.full_name()] for s in orgs]


    @property
    def source(self):
        """ the associated source object, if any """
        return self._obj


    def is_new(self):
        return self.source is None


    def create_or_update(self, document):
        if self.deleted.data == '1':
            document.sources.remove(self.source)
        elif self.is_new():
            return self.create_source(document)
        else:
            self.populate_obj(self.source)

        return None


    def create_source(self, document):
        from . import Person

        src = DocumentSource()
        src.document = document

        self.populate_obj(src)
        src.manual = True
        
        # link to person if they chose that option
        if self.source_type.data == 'person':
            src.person = Person.get_or_create(self.name.data)

            # override the 'quoted' attribute if we know this entity has utterances in
            # this document
            if any(src.person == u.entity.person for u in document.utterances):
                src.quoted = True

        return src
