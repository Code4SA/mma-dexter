from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Boolean,
    Integer,
    String,
    func,
    )
from sqlalchemy.orm import relationship
from wtforms import StringField, validators, HiddenField, BooleanField, RadioField

from ..app import db
from .with_offsets import WithOffsets
from ..forms import Form, SelectField

class DocumentSource(db.Model, WithOffsets):
    """
    A source is a source of information for an article.
    A source can be one of:

     - a named person (linked via person_id)
     - an unnamed person or child (in which case gender_id and race_id are meaningful)
     - a non-person secondary source (only name is applicable)

    A document cannot have more than one of the same source. See `__eq__()` for
    a description of how sources are compared.
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
    photographed = Column(Boolean)

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
        utterances = [u for u in self.document.utterances
                      if (self.person and u.entity.person == self.person)
                        or (not self.person and u.entity.name == self.name)]

        return sorted(utterances, key=lambda u: u.offset)


    def friendly_name(self):
        if self.person:
            return self.person.name

        if self.unnamed:
            return 'Unnamed'

        return self.name or '(none)'


    def sort_key(self):
        return [not self.manual, self.source_type, self.friendly_name()]


    @property
    def gender(self):
        if self.person:
            return self.person.gender
        return self.unnamed_gender

    @gender.setter
    def gender(self, val):
        """ Form helper for setting the gender of this source. """
        if self.person:
            self.person.gender = val
            self.unnamed_gender = None
        else:
            self.unnamed_gender = val

    @property
    def race(self):
        if self.person:
            return self.person.race
        return self.unnamed_race

    @race.setter
    def race(self, val):
        """ Form helper for setting the race of this source. """
        if self.person:
            self.person.race = val
            self.unnamed_race = None
        else:
            self.unnamed_race = val

    @property
    def named(self):
        return not self.unnamed

    @named.setter
    def named(self, val):
        self.unnamed = not val

    @property
    def offset_list(self):
        """ String of offset:length pairs of places in this document the entity
        is mentioned or quoted, may be empty. """
        offsets = ['%d:%d' % (u.offset, u.length) for u in self.utterances() if u.offset]
        for de in self.document_entities():
            if de.offset_list:
                offsets.append(de.offset_list)

        return ' '.join(offsets)


    def __eq__(self, other):
        """ Two sources are the same if:
  
        - they are a named person sources and:
          - the associated person is the same, and
          - the function and affiliation are the same
        - they are an unnamed person source and:
          - the gender and race are the same, and
          - the function and affiliation are the same
        - they are child sources and:
          - the name, race and gender are the same, and
          - the age and role are the same
        """
        return type(self) is type(other) and self.tuple() == other.tuple()


    def tuple(self):
        """ Generate a tuple suitable for comparing with `__eq__()` """
        return (self.source_type,
                self.unnamed,
                self.name,
                self.person,
                self.race,
                self.gender,
                self.function,
                self.role,
                self.age,
                self.affiliation,
               )


    def __repr__(self):
        return "<DocumentSource %s, person=%s, unnamed=%s, name=%s, doc=%s>" % \
                (self.source_type, self.person, self.unnamed, self.name and self.name.encode('utf-8'), self.document)


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
    def all(cls):
        return cls.query.order_by(cls.name).all()


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
