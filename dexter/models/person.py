# -*- coding: utf-8 -*-

from itertools import groupby

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

from .support import db
from ..forms import Form, MultiCheckboxField

class Person(db.Model):
    """
    A person, with a bit more info than just the 'person' entity. Multiple 'person' entities
    can link to a single person.
    """
    __tablename__ = "people"

    id          = Column(Integer, primary_key=True)
    name        = Column(String(100), index=True, nullable=False, unique=True)
    gender_id   = Column(Integer, ForeignKey('genders.id'))
    race_id     = Column(Integer, ForeignKey('races.id'))
    affiliation_id = Column(Integer, ForeignKey('affiliations.id'))

    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # Associations
    gender      = relationship("Gender", lazy=False)
    race        = relationship("Race", lazy=False)
    affiliation = relationship("Affiliation")

    def entity(self):
        """ Get an entity that is linked to this person. Because many entities can be linked, we
        try find the one with an exact name match before just returning any old one. """
        from . import Entity

        last = None

        # get all the entities and try to find the one that has an exact
        # name match
        for e in self.entities:
            last = e
            if e.name == self.name:
                return e

        # no exact match, just return the last one
        return last

    def get_alias_entity_ids(self):
        """
        Return a list of entity ids that are aliases for this person.
        """
        return [e.id for e in self.entities]

    def set_alias_entity_ids(self, ids):
        """
        Updated entities linked to this person by setting a list of
        entity ids.
        """
        from . import Entity
        self.entities = Entity.query.filter(Entity.id.in_(ids)).all()

    alias_entity_ids = property(get_alias_entity_ids, set_alias_entity_ids)


    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'race': self.race.name if self.race else None,
            'gender': self.gender.name if self.gender else None,
        }

    def __repr__(self):
        return "<Person id=%s, name=\"%s\">" % (self.id, self.name.encode('utf-8'))

    @classmethod
    def get_or_create(cls, name, gender=None, race=None):
        from . import Entity

        p = Person.query.filter(Person.name == name).first()
        if not p:
            p = Person()
            p.name = name

            if gender:
                p.gender = gender
            if race:
                p.race = race

            # link entities that are similar
            for e in Entity.query.filter(Entity.name == name, Entity.group == 'person', Entity.person == None).all():
                e.person = p

            db.session.add(p)
            # force a db write (within the transaction) so subsequent lookups
            # find this entity
            db.session.flush()
        return p


class PersonForm(Form):
    gender_id  = SelectField('Gender', default='')
    race_id    = SelectField('Race', default='')
    alias_entity_ids = MultiCheckboxField('Aliases')

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

        from . import Entity

        self.gender_id.choices = [['', '(unknown gender)']] + [[str(g.id), g.name] for g in Gender.query.order_by(Gender.name).all()]
        self.race_id.choices = [['', '(unknown race)']] + [[str(r.id), r.name] for r in Race.query.order_by(Race.name).all()]

        # we don't care if the entities are in the valid list or not
        self.alias_entity_ids.pre_validate = lambda form: True


class Gender(db.Model):
    __tablename__ = "genders"

    id        = Column(Integer, primary_key=True)
    name      = Column(String(150), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<Gender name='%s'>" % (self.name)

    def abbr(self):
        return self.name[0].upper()

    @classmethod
    def male(cls):
        return Gender.query.filter(Gender.name == 'Male').one()

    @classmethod
    def female(cls):
        return Gender.query.filter(Gender.name == 'Female').one()

    @classmethod
    def create_defaults(cls):
        text = """
        Female
        Male
        Other: Transgender, Transsexual
        """
        genders = []
        for s in text.strip().split("\n"):
            g = Gender()
            g.name = s.strip()
            genders.append(g)

        return genders


class Race(db.Model):
    __tablename__ = "races"

    id        = Column(Integer, primary_key=True)
    name      = Column(String(50), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<Race name='%s'>" % (self.name)

    def abbr(self):
        return self.name[0].upper()

    @classmethod
    def create_defaults(self):
        text = """
        Black
        White
        Coloured
        Asian
        Indian
        Other
        """

        races = []
        for s in text.strip().split("\n"):
            g = Race()
            g.name = s.strip()
            races.append(g)

        return races
