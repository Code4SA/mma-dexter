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
        International|
        Africa|
        National|
        Regional|
        Gauteng|za
        Western Cape|za
        KwaZulu-Natal|za
        Eastern Cape|za
        Limpopo|za
        Free State|za
        Mpumalanga|za
        North West|za
        Northern Cape|za
        Unclear (Last Resort)
        """
        locations = []
        countries = {}
        for s in text.strip().split("\n"):
            loc = Location()

            parts = s.split("|")
            loc.name = parts[0].strip()

            if len(parts) > 1:
                code = parts[1]
                if not code in countries:
                    countries[code] = Country.query.filter(Country.code == code).one()
                loc.country = countries[code]

            locations.append(loc)

        return locations
