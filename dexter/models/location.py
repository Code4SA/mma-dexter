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

from ..app import db

class Location(db.Model):
    """
    A geographical location.
    """
    __tablename__ = "locations"

    id          = Column(Integer, primary_key=True)
    name        = Column(String(50), index=True, nullable=False, unique=True)
    group       = Column(String(50), nullable=True)
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
        International||
        Africa||
        National||
        Regional||
        Gauteng|Provincial|za
        Western Cape|Provincial|za
        KwaZulu-Natal|Provincial|za
        Eastern Cape|Provincial|za
        Limpopo|Provincial|za
        Free State|Provincial|za
        Mpumalanga|Provincial|za
        North West|Provincial|za
        Northern Cape|Provincial|za
        Unclear (Last Resort)||
        """
        locations = []
        countries = {}
        for s in text.strip().split("\n"):
            loc = Location()

            parts = s.split("|")
            loc.name = parts[0].strip()

            if len(parts) > 1 and parts[1]:
                loc.group = parts[1]

            if len(parts) > 2 and parts[2]:
                code = parts[2]
                if not code in countries:
                    countries[code] = Country.query.filter(Country.code == code).one()
                loc.country = countries[code]

            locations.append(loc)

        return locations
