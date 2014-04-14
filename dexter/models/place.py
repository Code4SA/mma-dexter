from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
    )

import logging
log = logging.getLogger(__name__)

from .support import db

class Place(db.Model):
    """
    A geographical place in South Africa.

    The table is pre-populated using the subplace information
    from the 2011 Census.
    
    There is a place heirarchy:

      Nation -> Province -> District -> Municipality -> Mainplace -> Subplace

    We don't store District information because it's rarely used.

    Each place has a lat/long pair associated with it. This is the centroid
    of the place, all places are actually geographical areas.
    
    The table is not well normalised because we don't really need normalisation
    information at this point. For example, a municipality will have province
    and muni information, but not mainplace or subplace, which will be null.
    """
    __tablename__ = "places"

    id          = Column(Integer, primary_key=True)

    # eg: province, municipality, mainplace, or subplace
    level       = Column(String(15), index=True)

    # province name and code
    province_name = Column(String(20), index=True)
    province_code = Column(String(5), index=True)

    # municipality
    municipality_name = Column(String(50), index=True)
    municipality_code = Column(String(10), index=True)

    # mainplace
    mainplace_name = Column(String(50), index=True)
    mainplace_code = Column(String(10), index=True)

    # subplace
    subplace_name = Column(String(50), index=True)
    subplace_code = Column(String(10), index=True, unique=True)

    lat = Column(String(10))
    lng = Column(String(10))
