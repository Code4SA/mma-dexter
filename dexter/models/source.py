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
from wtforms import StringField, validators, SelectField, HiddenField, BooleanField

from .support import db
from .with_offsets import WithOffsets
from ..forms import Form

class DocumentSource(db.Model, WithOffsets):
    """
    A source is a source of information for an article.
    A source instance is bound to a document and an entity and describes the
    role in which the source was accessed, how they were accessed, etc.
    """
    __tablename__ = "document_sources"

    id        = Column(Integer, primary_key=True)
    doc_id    = Column(Integer, ForeignKey('documents.id'), index=True, nullable=False)
    entity_id = Column(Integer, ForeignKey('entities.id'), index=True)
    source_function_id = Column(Integer, ForeignKey('source_functions.id'))

    photographed = Column(Boolean)
    quoted       = Column(Boolean)
    named        = Column(Boolean)

    # TODO: add role and method of access

    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # Associations
    entity    = relationship("Entity", lazy=False)
    function  = relationship("SourceFunction", lazy=False)

    def document_entity(self):
        """ The DocumentEntity instance that matches this source for this document. May be None. """
        for de in self.document.entities:
            if de.entity == self.entity:
                return de
        return None

    def utterances(self):
        """ A potentially empty list of Utterances from this source in this document. """
        return sorted([u for u in self.document.utterances if u.entity == self.entity],
                key=lambda u: u.offset)


    @property
    def person(self):
        """ Direct access to the person associated with this source's entity, which may
        be None. """
        return self.entity.person if self.entity else None


    @property
    def offset_list(self):
        """ String of offset:length pairs of places in this document the entity
        is mentioned or quoted, may be empty. """
        offsets = ['%d:%d' % (u.offset, u.length) for u in self.utterances() if u.offset]
        de = self.document_entity()
        if de and de.offset_list:
            offsets.append(de.offset_list)

        return ' '.join(offsets)


    def __repr__(self):
        return "<DocumentSource doc=%s, entity=%s>" % (self.document, self.entity)


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


class DocumentSourceForm(Form):
    person_name       = StringField('Name', [validators.Length(max=50)])
    source_function_id = SelectField('Function', [validators.Required()], default=1)
    quoted            = BooleanField('Quoted', default=False)

    def __init__(self, *args, **kwargs):
        super(DocumentSourceForm, self).__init__(*args, **kwargs)

        self.source_function_id.choices = [[str(s.id), s.name] for s in SourceFunction.query.order_by(SourceFunction.name).all()]


    def get_or_create_entity(self):
        from . import Person, Entity

        """ Get or create an entity that matches the name of this document source.
        We try, in order:

        * a person with that name
        * a person entity with that name (and create a person if not already linked)
        * any entity with that name

        If all fail, we create a new entity and a new person.
        """
        name = self.person_name.data
        if not name:
            return None

        person = Person.query.filter(Person.name == name).first()

        if person:
            entity = person.entity()
        else:
            # find a person entity
            entity = Entity.query.filter(Entity.name == name, Entity.group == 'person').first()

            if not entity:
                # find an arbitrary entity
                entity = Entity.query.filter(Entity.name == name).first()

                if not entity:
                    # create the entity
                    entity = Entity()
                    entity.group = 'person'
                    entity.name = name
                    db.session.add(entity)

            # link a person to the entity if it doesn't exist
            if entity.group == 'person' and not entity.person:
                person = Person()
                person.name = entity.name
                entity.person = person

        return entity
