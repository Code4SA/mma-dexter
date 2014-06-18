from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
    or_,
    )
from sqlalchemy.orm import relationship

from .support import db

class Location(db.Model):
    """
    A geographical location.
    """
    __tablename__ = "locations"

    id          = Column(Integer, primary_key=True)
    name        = Column(String(50), index=True, nullable=False, unique=True)
    country_id  = Column(Integer, ForeignKey('countries.id'), nullable=True, index=True)

    # associations
    country     = relationship("Country")

    def __repr__(self):
        return "<Location id=%s, name=\"%s\">" % (self.id, self.name.encode('utf-8'))


    @classmethod
    def for_country(cls, country):
        return cls.query\
            .filter(
                or_(cls.country_id == country.id,
                    cls.country_id == None)
            )\
            .order_by(cls.name)\
            .all()


    @classmethod
    def create_defaults(cls):
        text = """
        International
        Africa
        National
        Regional
        Gauteng
        Western Cape
        KwaZulu-Natal
        Eastern Cape
        Limpopo
        Free State
        Mpumalanga
        North West
        Northern Cape
        Unclear (Last Resort)
        """
        locations = []
        for s in text.strip().split("\n"):
            loc = Location()
            loc.name = s.strip()
            locations.append(loc)

        return locations
