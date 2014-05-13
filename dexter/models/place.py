from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Float,
    String,
    func,
    or_,
    )
from sqlalchemy.orm import relationship, backref

import logging
log = logging.getLogger(__name__)

from .support import db
from .with_offsets import WithOffsets

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

    @property
    def full_name(self):
        parents = [self.subplace_name, self.mainplace_name, self.municipality_name, self.province_name]
        return ', '.join(x for x in parents if x)

    @property
    def name(self):
        return getattr(self, '%s_name' % self.level)

    @property
    def code(self):
        return getattr(self, '%s_code' % self.level)

    @property
    def geo_id(self):
        return '%s-%s' % (self.level, self.code)

    @property
    def geo_type(self):
        """ What type of geo is this, a point or an id? """
        if self.lat and self.lng:
            return "point"
        else:
            return "region"

    @property
    def geo_data(self):
        """ Data for this place. If it's a point, a lat,lng string.
        Otherwise a level-id string."""
        if self.lat and self.lng:
            return '%s, %s' % (self.lat, self.lng)
        else:
            return '%s-%s' % (self.level, self.code)


    def as_dict(self):
        d = {
            'type': self.geo_type,
            'id': self.geo_id,
            'level': self.level,
            'code': self.code,
            'full_name': self.full_name,
            'name': self.name,
        }

        if d['type'] == 'point':
            d['coordinates'] = [self.lat, self.lng]

        return d


    def __repr__(self):
        return "<Place level=%s, province=%s, muni=%s, mainplace='%s', subplace='%s'>" % (
                self.level, self.province_code, self.municipality_code,
                self.mainplace_name, self.subplace_name)


    @classmethod
    def find(cls, term):
        """
        See if we have a place that matches this name.
        """
        if term in PLACE_STOPWORDS:
            return

        p = Place.query\
                .filter(Place.level == 'province')\
                .filter(Place.province_name == term).first()
        if p:
            return p

        p = Place.query\
                .filter(Place.level == 'municipality')\
                .filter(or_(
                    Place.municipality_name == term,
                    Place.municipality_name == 'City of %s' % term)).first()
        if p:
            return p

        p = Place.query\
                .filter(Place.level == 'mainplace')\
                .filter(or_(
                    Place.mainplace_name == term,
                    Place.mainplace_name == '%s MP' % term)).first()
        if p:
            return p

        # subplaces are almost always wrong, since they have names like 'Paris' and 'Zuma'
        #p = Place.query\
        #        .filter(Place.level == 'subplace')\
        #        .filter(or_(
        #            Place.subplace_name == term,
        #            Place.subplace_name == '%s SP' % term)).first()
        #if p:
        #    return p

        return None


class DocumentPlace(db.Model, WithOffsets):
    """
    Place in an article.
    """
    __tablename__ = "document_places"

    id        = Column(Integer, primary_key=True)
    doc_id    = Column(Integer, ForeignKey('documents.id', ondelete='CASCADE'), index=True, nullable=False)

    place_id  = Column(Integer, ForeignKey('places.id'), index=True, nullable=False)
    relevance = Column(Float, index=True, nullable=True)
    relevant  = Column(Boolean, index=True, default=False)

    # offsets in the document, a space-separated list of offset:length pairs.
    offset_list  = Column(String(1024))
    
    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # Associations
    place        = relationship('Place', lazy=False)

    def as_dict(self):
        p = self.place.as_dict()
        p['relevance'] = self.relevance
        return p


    def __repr__(self):
        return "<DocumentPlace id=%s, place=%s, relevance=%s, doc=%s>" % (self.id, self.place, self.relevance, self.document)


    @classmethod
    def summary_for_docs(cls, docs):
        """
        Generate a summary description for places in these docs for plotting on maps.
        """
        mentions = {}
        origins = {}
        count = 0

        for d in docs:
            # TODO: origin

            places = d.get_places()
            if places:
                count += 1

                for dp in places:
                    geo_id = dp.place.geo_id

                    if not geo_id in mentions:
                        mentions[geo_id] = dp.place.as_dict()
                        mentions[geo_id]['documents'] = []

                    mentions[geo_id]['documents'].append(d.id)

        return {
            'document_count': count,
            'mentions': mentions.values(),
            'origins': origins,
        }


# Places we know aren't in SA, but sometimes match something in our DB
PLACE_STOPWORDS = set(x.strip() for x in """
London
New York
Afghanistan
Akrotiri
Albania
Algeria
American Samoa
Andorra
Angola
Anguilla
Antarctica
Antigua and Barbuda
Argentina
Armenia
Aruba
Ashmore and Cartier Islands
Australia
Austria
Azerbaijan
Bahamas
Bahrain
Bangladesh
Barbados
Bassas da India
Belarus
Belgium
Belize
Benin
Bermuda
Bhutan
Bolivia
Bosnia and Herzegovina
Botswana
Bouvet Island
Brazil
British Indian Ocean Territory
British Virgin Islands
Brunei
Bulgaria
Burkina Faso
Burma
Burundi
Cambodia
Cameroon
Canada
Cape Verde
Cayman Islands
Central African Republic
Chad
Chile
China
Christmas Island
Clipperton Island
Cocos (Keeling) Islands
Colombia
Comoros
Congo
Congo
Cook Islands
Coral Sea Islands
Costa Rica
Cote d'Ivoire
Croatia
Cuba
Cyprus
Czech Republic
Denmark
Dhekelia
Djibouti
Dominica
Dominican Republic
Ecuador
Egypt
El Salvador
Equatorial Guinea
Eritrea
Estonia
Ethiopia
Europa Island
Falkland Islands (Islas Malvinas)
Faroe Islands
Fiji
Finland
France
French Guiana
French Polynesia
French Southern and Antarctic Lands
Gabon
Gambia
Gaza Strip
Georgia
Germany
Ghana
Gibraltar
Glorioso Islands
Greece
Greenland
Grenada
Guadeloupe
Guam
Guatemala
Guernsey
Guinea
Guinea-Bissau
Guyana
Haiti
Heard Island and McDonald Islands
Holy See (Vatican City)
Honduras
Hong Kong
Hungary
Iceland
India
Indonesia
Iran
Iraq
Ireland
Isle of Man
Israel
Italy
Jamaica
Jan Mayen
Japan
Jersey
Jordan
Juan de Nova Island
Kazakhstan
Kenya
Kiribati
North Korea
South Korea
Kuwait
Kyrgyzstan
Laos
Latvia
Lebanon
Lesotho
Liberia
Libya
Liechtenstein
Lithuania
Luxembourg
Macau
Macedonia
Madagascar
Malawi
Malaysia
Maldives
Mali
Malta
Marshall Islands
Martinique
Mauritania
Mauritius
Mayotte
Mexico
Micronesia
Moldova
Monaco
Mongolia
Montserrat
Morocco
Mozambique
Namibia
Nauru
Navassa Island
Nepal
Netherlands
Netherlands Antilles
New Caledonia
New Zealand
Nicaragua
Niger
Nigeria
Niue
Norfolk Island
Northern Mariana Islands
Norway
Oman
Pakistan
Palau
Panama
Papua New Guinea
Paracel Islands
Paraguay
Peru
Philippines
Pitcairn Islands
Poland
Portugal
Puerto Rico
Qatar
Reunion
Romania
Russia
Rwanda
Saint Helena
Saint Kitts and Nevis
Saint Lucia
Saint Pierre and Miquelon
Saint Vincent and the Grenadines
Samoa
San Marino
Sao Tome and Principe
Saudi Arabia
Senegal
Serbia and Montenegro
Seychelles
Sierra Leone
Singapore
Slovakia
Slovenia
Solomon Islands
Somalia
South Africa
South Georgia and the South Sandwich Islands
Spain
Spratly Islands
Sri Lanka
Sudan
Suriname
Svalbard
Swaziland
Sweden
Switzerland
Syria
Taiwan
Tajikistan
Tanzania
Thailand
Timor-Leste
Togo
Tokelau
Tonga
Trinidad and Tobago
Tromelin Island
Tunisia
Turkey
Turkmenistan
Turks and Caicos Islands
Tuvalu
Uganda
Ukraine
United Arab Emirates
United Kingdom
United States
Uruguay
Uzbekistan
Vanuatu
Venezuela
Vietnam
Virgin Islands
Wake Island
Wallis and Futuna
West Bank
Western Sahara
Yemen
Zambia
Zimbabwe
""".strip().split("\n"))
