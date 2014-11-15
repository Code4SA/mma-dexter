# -*- coding: utf-8 -*-

from itertools import groupby
from datetime import datetime, timedelta
import logging

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
    desc,
    )
from sqlalchemy.orm import relationship, subqueryload
from wtforms import StringField, validators, SelectField, HiddenField, BooleanField
from flask.ext.login import current_user

from .support import db
from ..forms import Form, MultiCheckboxField
from ..utils import levenshtein

class Person(db.Model):
    """
    A person, with a bit more info than just the 'person' entity. Multiple 'person' entities
    can link to a single person.
    """
    __tablename__ = "people"

    log = logging.getLogger(__name__)

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
            'affiliation': self.affiliation.full_name() if self.affiliation else None,
        }


    def all_affiliations(self):
        """
        Get a list of [Affiliation, count] tuples for all affiliations
        for this source.
        """
        from . import DocumentSource, Affiliation

        rows = db.session.query(
                DocumentSource.affiliation_id,
                func.count(1).label('count'))\
                .filter(DocumentSource.person_id == self.id)\
                .filter(DocumentSource.affiliation_id != None)\
                .group_by(DocumentSource.affiliation_id)\
                .order_by(desc('count'))\
                .all()

        ids = [r[0] for r in rows]
        affiliations = Affiliation.query.filter(Affiliation.id.in_(ids)).all()
        affiliations = dict((a.id, a) for a in affiliations)

        return [(affiliations[r[0]], r[1]) for r in rows]


    def relearn_affiliation(self):
        """ Relearn this person's affiliation, based on a time-decaying
        weighted average of affiliation mappings taken from document
        sources. 
        
        We consider all changes that have taken place over the last 7
        days. The current affiliation (if any), is considered to have
        been set exactly 7 days ago.

        All dates are based on document publication dates.

        Returns True if the affiliation was updated, False otherwise.
        """
        from . import DocumentSource, Document

        now = datetime.utcnow()
        days_ago = now - timedelta(days=7)

        sources = DocumentSource.query\
                .options(subqueryload(DocumentSource.document))\
                .options(subqueryload(DocumentSource.affiliation))\
                .filter(Document.published_at >= days_ago)\
                .filter(DocumentSource.person == self)\
                .filter(DocumentSource.affiliation != None)\
                .order_by(Document.published_at)\
                .all()

        weights = {}

        # exponential decay. An affiliation from today is worth
        # only half that tomorrow, a half again the day after, etc.
        # Cap the weight at 100 so that we don't get overflow.
        weight = lambda d: 1.0 / (2 ** min(100.0, (now - d).days))

        # current affiliation
        if self.affiliation:
            weights[self.affiliation] = weight(days_ago)

        # accumulate weights for affiliations gathered over the last
        # period
        for source in sources:
            weights[source.affiliation] = \
                    weights.get(source.affiliation, 0) + \
                    weight(source.document.published_at)

        self.log.debug("Affiliation weights for %s: %s" % (self, weights))

        if weights:
            affiliation, _ = max(weights.items(), key=lambda pair: pair[1])

            if affiliation != self.affiliation:
                self.log.info("Learned new affiliation for %s: was=%s, now=%s" % (self, self.affiliation, affiliation))
                self.affiliation = affiliation
                return True

        return False


    def merge_into(self, dest):
        """
        Merge this person into +dest+, and delete
        this person.
        """
        from . import Author, DocumentSource, Entity

        if self.id is None or dest.id is None:
            raise ArgumentError("Both id's must be valid")

        for m in [Author, DocumentSource, Entity]:
            m.query.filter(m.person_id == self.id).update({'person_id': dest.id})

        # ensure we remember the old person as an alias of the new one
        e = Entity.get_or_create('person', self.name)
        e.person = dest

        self.log.info("Merged %s into %s" % (self, dest))

        db.session.delete(self)


    def similarly_named_people(self, threshold=0.8):
        """
        Return a list of (Person, similarity) tuples for instances that have similar names,
        within +threshold+.
        """
        return [(p, x) for p, x in Person.similarly_named_to(p.name, threshold) if p != self]

    @classmethod
    def similarly_named_to(cls, name, threshold=0.8):
        candidates = ((p, levenshtein(p.name, name)) for p in Person.query.all())
        return [(p, x) for p, x in candidates if x >= threshold]


    def guess_gender_from_doc(self, doc):
        """
        Guess the gender of this person, if it's not already set, by looking
        at quotations by this person in this document.
        """
        if self.gender:
            return

        for de in (de for de in doc.entities if de.entity.person == self):
            mentions = set(doc.text[offset:offset+length].lower() for offset, length in de.offsets())

            if 'he' in mentions or 'his' in mentions:
               self.gender = Gender.male()
               self.log.info("Learnt gender for %s" % self)
               return

            elif 'she' in mentions or 'her' in mentions:
               self.gender = Gender.female()
               self.log.info("Learnt gender for %s" % self)
               return


    def reset_all_affiliations(self):
        """
        Change the affiliation for ALL occurrences of this person
        to the current state.
        """
        from . import DocumentSource
        DocumentSource.query\
            .filter(DocumentSource.person_id == self.id)\
            .update({'affiliation_id': self.affiliation_id})


    def __repr__(self):
        return "<Person id=%s, name=\"%s\">" % (self.id, self.name.encode('utf-8'))

    @classmethod
    def get_or_create(cls, name, gender=None, race=None):
        from . import Entity

        p = Person.query.filter(Person.name == name).first()
        if not p:
            p = Person()
            p.name = name[0:100]

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
    affiliation_id   = SelectField('Affiliation', default='')
    reset_affiliation = BooleanField('Reset affiliation for ALL documents where this person is a source? THIS IS DANGEROUS!', default=False)
    alias_entity_ids = MultiCheckboxField('Aliases')

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

        from . import Entity, Affiliation

        self.gender_id.choices = [['', '(unknown gender)']] + [[str(g.id), g.name] for g in Gender.query.order_by(Gender.name).all()]
        self.race_id.choices = [['', '(unknown race)']] + [[str(r.id), r.name] for r in Race.query.order_by(Race.name).all()]
        self.affiliation_id.choices = [['', '(unknown affiliation)']] + [[str(a.id), a.name] for a in Affiliation.for_country(current_user.country)]

        # we don't care if the entities are in the valid list or not
        self.alias_entity_ids.pre_validate = lambda form: True


class Gender(db.Model):
    __tablename__ = "genders"

    id        = Column(Integer, primary_key=True)
    name      = Column(String(150), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<Gender name='%s'>" % (self.name)

    def abbr(self):
        return self.name[0:2].title()

    @classmethod
    def all(cls):
        return cls.query.order_by(cls.name).all()

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
        return self.name[0:2].title()

    @classmethod
    def all(cls):
        return cls.query.order_by(cls.name).all()

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
