from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
    )
from sqlalchemy.orm import relationship

from wtforms import StringField, validators, SelectField, HiddenField

from . import Person, Gender, Race
from .support import db
from ..forms import Form

import logging
log = logging.getLogger(__name__)

class Author(db.Model):
    """
    A document author, which may be a single person (in which case it's linked to a Person),
    or it may be an agency.
    """
    __tablename__ = "authors"

    id          = Column(Integer, primary_key=True)
    name        = Column(String(50), index=True, nullable=False, unique=True)
    author_type_id = Column(Integer, ForeignKey('author_types.id'), nullable=False)
    person_id   = Column(Integer, ForeignKey('people.id'))

    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # Associations
    author_type = relationship("AuthorType", lazy=False)
    person      = relationship("Person", lazy=False)

    def json(self):
        return {
            'id': self.id,
            'name': self.person.name if self.person else self.name,
            'author_type': self.author_type.name,
        }


    def __repr__(self):
        return "<Author id=%s, type=%s, name=\"%s\", person=%s>" % (self.id, self.author_type, self.person, self.name.encode('utf-8'))

    @classmethod
    def unknown(cls):
        return cls.get_or_create('Unknown', AuthorType.unknown())

    @classmethod
    def get_or_create(cls, name, author_type, gender=None, race=None):
        """ Get the author with this name or create it if it doesn't exist. """
        a = Author.query.filter(Author.name == name).first()
        if not a:
            a = Author()
            a.name = name
            a.author_type = author_type

            if a.author_type.name in ['Journalist', 'Guest Writer']:
                # create an associated person
                a.person = Person.get_or_create(name, gender, race)

            # force a db write (within the transaction) so subsequent lookups
            # find this entity
            db.session.add(a)
            db.session.flush()
        return a


class AuthorType(db.Model):
    """
    What type of author this is.
    """
    __tablename__ = "author_types"

    id        = Column(Integer, primary_key=True)
    name      = Column(String(150), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<AuthorType name='%s'>" % (self.name)

    @classmethod
    def journalist(cls):
        return AuthorType.query.filter(AuthorType.name == 'Journalist').one()

    @classmethod
    def unknown(cls):
        return AuthorType.query.filter(AuthorType.name == 'Unknown').one()

    @classmethod
    def create_defaults(cls):
        text = """
        Journalist
        Agency
        Guest Writer
        Many Journalists
        Journalist and Agency
        Unknown
        """
        types = []
        for s in text.strip().split("\n"):
            t = AuthorType()
            t.name = s.strip()
            types.append(t)

        return types


class AuthorForm(Form):
    name              = StringField('Author', [validators.Length(max=50)], default='Unknown')
    author_type_id    = SelectField('Type', default=1)
    person_gender_id  = SelectField('Gender', default='')
    person_race_id    = SelectField('Race', default='')

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)

        from . import Gender, Race

        self.author_type_id.choices = [[str(a.id), a.name] for a in AuthorType.query.order_by(AuthorType.name).all()]
        self.person_gender_id.choices = [['', '(unknown gender)']] + [[str(g.id), g.name] for g in Gender.query.order_by(Gender.name).all()]
        self.person_race_id.choices = [['', '(unknown race)']] + [[str(r.id), r.name] for r in Race.query.order_by(Race.name).all()]

    def get_or_create_author(self):
        """ Get or create an author matching this form. Returns None if the form is not valid. """
        if not self.validate():
            return None

        return Author.get_or_create(
                name        = self.name.data,
                author_type = AuthorType.query.get(self.author_type_id.data),
                gender      = Gender.query.get(self.person_gender_id.data) if self.person_gender_id.data else None,
                race        = Race.query.get(self.person_race_id.data) if self.person_race_id.data else None)
