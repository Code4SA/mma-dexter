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

from .support import db

class Person(db.Model):
    """
    A person, with a bit more info than just the 'person' entity. Multiple 'person' entities
    can link to a single person.
    """
    __tablename__ = "people"

    id          = Column(Integer, primary_key=True)
    name        = Column(String(50), index=True, nullable=False, unique=True)
    gender_id   = Column(Integer, ForeignKey('genders.id'))
    race_id     = Column(Integer, ForeignKey('races.id'))

    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # Associations
    gender      = relationship("Gender", lazy=False)
    race        = relationship("Race", lazy=False)

    def entity(self):
        """ Get an entity that is linked to this person. Because many entities can be linked, we
        try find the one with an exact name match before just returning any old one. """
        from . import Entity

        last = None

        # get all the entities and try to find the one that has an exact
        # name match
        for e in Entity.query.filter(Entity.person == self).all():
            last = e
            if e.name == self.name:
                return e

        # no exact match, just return the last one
        return last

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
        p = Person.query.filter(Person.name == name).first()
        if not p:
            p = Person()
            p.name = name
            if gender:
                p.gender = gender
            if race:
                p.race = race

            db.session.add(p)
            # force a db write (within the transaction) so subsequent lookups
            # find this entity
            db.session.flush()
        return p


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
