# -*- coding: utf-8 -*-

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

    def __repr__(self):
        return "<Person id=%s, name=\"%s\">" % (self.id, self.name.encode('utf-8'))


class Gender(db.Model):
    __tablename__ = "genders"

    id        = Column(Integer, primary_key=True)
    name      = Column(String(150), index=True, nullable=False, unique=True)

    SYMBOLS = {
        'Male': u'♂',
        'Female': u'♀',
        'Other: Transgender, Transsexual': u'⚥'}

    def symbol(self):
        return self.SYMBOLS.get(self.name)

    def __repr__(self):
        return "<Gender name='%s'>" % (self.name)

    @classmethod
    def create_defaults(self):
        genders = []
        for s in self.SYMBOLS.values():
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
        return self.name[0]

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
