from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
    )
from sqlalchemy.orm import relationship

import logging
log = logging.getLogger(__name__)

from .support import db

class Country(db.Model):
    """
    A country groups users and the media and locations
    they process articles from.
    """
    __tablename__ = "countries"

    id          = Column(Integer, primary_key=True)
    name        = Column(String(50), nullable=False)

    # http://en.wikipedia.org/wiki/ISO_3166-1 alpha-2 -- basically TLD cods
    code        = Column(String(2), nullable=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Country code=%s>" % (self.code,)

    @classmethod
    def all(cls):
        return cls.query.order_by(Country.name).all()

    @classmethod
    def create_defaults(cls):
        text = """
South Africa|za
Lesotho|ls
Zambia|zm
Namibia|na
            """

        countries = []
        for country in text.strip().split("\n"):
            c = Country()
            c.name, c.code = country.strip().split('|')
            countries.append(c)

        return countries
