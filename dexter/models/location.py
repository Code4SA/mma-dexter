from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
    )

from .support import db

class Location(db.Model):
    """
    A geographical location.
    """
    __tablename__ = "locations"

    id          = Column(Integer, primary_key=True)
    name        = Column(String(50), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<Location id=%s, name=\"%s\">" % (self.id, self.name.encode('utf-8'))

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
