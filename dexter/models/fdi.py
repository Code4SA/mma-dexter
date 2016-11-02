# coding=utf-8
from sqlalchemy import (
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Float,
    Index,
)
from sqlalchemy.orm import relationship, backref
from .with_offsets import WithOffsets
from unidecode import unidecode

from wtforms import StringField, TextAreaField, validators, DateTimeField, HiddenField, IntegerField, DateField

from ..forms import Form, SelectField
from ..app import db


class Investment(db.Model):
    """
    An investment, the core unit of the FDI analysis module.
    """
    __tablename__ = "investments"

    id = Column(Integer, primary_key=True)
    doc_id = Column(Integer, ForeignKey('documents.id', ondelete='CASCADE'), index=True, nullable=False)
    name = Column(String(200), index=True, nullable=True)
    value = Column(Integer)
    temp_opps = Column(Integer)
    perm_opps = Column(Integer)
    company = Column(String(1024))
    additional_place = Column(String(1024))

    investment_begin = Column(Date, index=True, unique=False)
    investment_end = Column(Date, index=True, unique=False)

    currency_id = Column(Integer, ForeignKey('currencies.id'), index=True)
    phase_id = Column(Integer, ForeignKey('phases.id'), index=True)
    invest_origin_id = Column(Integer, ForeignKey('investment_origins.id'), index=True)
    invest_loc_id = Column(Integer, ForeignKey('investment_locations.id'), index=True)
    invest_type_id = Column(Integer, ForeignKey('investment_types.id'), index=True)
    sector_id = Column(Integer, ForeignKey('sectors.id'), index=True)
    involvement_id = Column(Integer, ForeignKey('involvements.id'), index=True)
    industry_id = Column(Integer, ForeignKey('industries.id'), index=True)

    currency = relationship("Currencies")
    phase = relationship("Phases")
    sector = relationship("Sectors")
    industry = relationship("Industries")
    involvement = relationship("Involvements")
    investment_type = relationship("InvestmentType")
    investment_origin = relationship("InvestmentOrigins")

    def add_gov(self, government):
        """ Add a new government involvement, but only if it's not already there. """
        for k in self.governments:
            # to compare, we emulate mysql's utf8_general_ci collation:
            # strip diacritics and lowercase
            if unidecode(k.gov).lower() == unidecode(government.gov).lower():
                return k.add_offsets(government.offsets())

        self.governments.append(government)
        return True

    def add_company(self, company):
        """ Add a new government involvement, but only if it's not already there. """
        for k in self.companies:
            # to compare, we emulate mysql's utf8_general_ci collation:
            # strip diacritics and lowercase
            if unidecode(k.name).lower() == unidecode(company.name).lower():
                return k.add_offsets(company.offsets())

        self.governments.append(company)
        return True

    def add_fin(self, finance):
        """ Add a new government involvement, but only if it's not already there. """
        for k in self.finances:
            # to compare, we emulate mysql's utf8_general_ci collation:
            # strip diacritics and lowercase
            if unidecode(k.name).lower() == unidecode(finance.name).lower():
                return k.add_offsets(finance.offsets())

        self.finances.append(finance)
        return True

    def __repr__(self):
        return "<Investment id=%s, Document id=%s>" % (self.id, self.doc_id)


# Note-type fields

# class Government(db.Model, WithOffsets):
#     """
#     Government involvement on investments.
#     """
#     __tablename__ = "government"
#
#     id = Column(Integer, primary_key=True)
#     inv_id = Column(Integer, ForeignKey('investments.id', ondelete='CASCADE'), index=True)
#     gov = Column(String(200), index=True, nullable=False)
#
#     # offsets in the document, a space-separated list of offset:length pairs.
#     offset_list = Column(String(1024))
#
#     def __repr__(self):
#         return "<Government='%s', inv=%s>" % (
#             self.gov.encode('utf-8'), self.investment)
#
#
# Index('inv_gov_inv_id_gov_ix', Government.inv_id, Government.gov, unique=True)
#
#
# class Companies(db.Model, WithOffsets):
#     """
#     The company investing.
#     """
#     __tablename__ = "companies"
#
#     id = Column(Integer, primary_key=True)
#     inv_id = Column(Integer, ForeignKey('investments.id', ondelete='CASCADE'), index=True)
#     name = Column(String(50), index=True, nullable=False)
#
#     # offsets in the document, a space-separated list of offset:length pairs.
#     offset_list = Column(String(1024))
#
#     def __repr__(self):
#         return "<Company='%s', inv=%s>" % (
#             self.name.encode('utf-8'), self.investment)
#
# Index('inv_comp_inv_id_comp_ix', Companies.inv_id, Companies.name, unique=True)
#
#
# class FinancePartners(db.Model, WithOffsets):
#     """
#     The finance partners.
#     """
#     __tablename__ = "finance"
#
#     id = Column(Integer, primary_key=True)
#     inv_id = Column(Integer, ForeignKey('investments.id', ondelete='CASCADE'), index=True)
#     name = Column(String(200), index=True, nullable=False, unique=True)
#
#     # offsets in the document, a space-separated list of offset:length pairs.
#     offset_list = Column(String(1024))
#
#     def __repr__(self):
#         return "<FinancePartner='%s', inv=%s>" % (
#             self.name.encode('utf-8'), self.investment)
#
# Index('inv_fin_inv_id_fin_ix', FinancePartners.inv_id, FinancePartners.name, unique=True)


# Fixed-list fields


class InvestmentType(db.Model):
    """
    The type of investment being made.
    """
    __tablename__ = "investment_types"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<Investment type='%s'>" % (self.name)

    @classmethod
    def create_defaults(self):
        text = """
        Greenfields
        Brownfields
        Expansion
        Upgrading
        Disinvestment
        unspecified
        """

        investment_type = []
        for s in text.strip().split("\n"):
            i = InvestmentType()
            i.name = s.strip()
            investment_type.append(i)

        return investment_type

    @classmethod
    def all(cls):
        return cls.query.order_by(InvestmentType.name).all()


class Sectors(db.Model):
    """
    The sector an investment type falls under.
    """
    __tablename__ = "sectors"

    id = Column(Integer, primary_key=True)
    name = Column(String(130), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<Sector='%s'>" % (self.name)

    @classmethod
    def create_defaults(self):
        text = """
        Industry
        Crop and animal production, hunting and related service activities
        Forestry and logging
        Fishing and aquaculture
        Mining of coal and lignite
        Extraction of crude petroleum and natural gas
        Mining of metal ores
        Other mining and quarrying
        Mining support service activities
        Manufacturing of food products
        Manufacturing of beverages
        Manufacturing of tobacco products
        Manufacturing of textiles
        Manufacturing of wearing apparel
        Manufacturing of leather and related products
        Manufacturing of wood and product if wood or cork, except furniture; manufacte of articles of straw and plaiting materials
        Manufacturing of paper and paper products
        Printing and reproduction of recorded media
        Manufacture of cole and refined petroleum products
        Manufcature of chemicals and chemical products
        Manufacture of pharmaceuticals, medicinal chemical and botanical products
        Manufacture of rubber abd plastic products
        Manufacture of other non-metallic mineral products
        Manufacture of basic metals
        Manufacture of fabricated metal products, except machinery and equipment
        Manufacturer of computer, electronic and optical products
        Manufacture of electrical equipment
        Manufacture of machinery and equipment n.e.c
        Manufacture of motor vehicles, trailer and semi-trailers
        Manufacture of other transport equipment
        Manufacture of furniture
        Other manufacturing
        Repair and installation of machinery and equipment
        Electricty, gas, steam, and air conditioning supply
        Water collection, treatment and supply
        Sewerage
        Waste collection, treatment and disposal activitites; materials recovery
        Remediation activities and other waste management services
        Construction of buildings
        Civil Engineering
        Specialised construction activities
        Wholesale and retail trade and repair of motor vehicles and motorcycles
        Wholesale trade, except of motor vehicles and motorcylcles
        Retail trade, except of motor vehicles and motorcyles
        Land transport abd transport via pipelines
        Water transport
        Air transport
        Warehousing and support activities for transportation
        Postal and courier activities
        Accommodation
        Food and beverage service activities
        Publishing activities
        Motion picture, video and television programme production, sound recording and music publishing activities
        Programming and broadcasting activities
        Telecommunications
        Computer programming, consultancy and related activities
        Information service activities
        Financial service activities, except insurance and pension funding
        Insurance, reinsurance and pension funding, except compulsory social security
        Activities auxiliary to financial service and insurance activities
        Real estate activities
        Legal and accounting activities
        Activities of head offices; management consultancy activities
        Architectural and engineering activities; technical testing and analysis
        Scientific research and development
        Advertising and market research
        Other professional, scientific and technical activities
        Veterinary activities
        Rental and leasing activities
        Employment activities
        Travel agency, tour operator, reservation service and related activities
        Security and investigation activities
        Services to buildings and landscape activities
        Office administrative, office support and other business support activities
        Public administration and defence; compulsory social security
        Education
        Human health activities
        Residential care activities
        Social work activities without accommodation
        Creative, arts and entertainment activities
        Libraries, archives, museums and other cultural activities
        Gambling and betting activities
        Sports activities and amusement and recreation activities
        Activities of membership organizations
        Repair of computers and personal and household goods
        Other personal service activities
        Activities of households as employers of domestic personnel
        Undifferentiated goods- and services-producing activities of private households for own use
        Activities of extraterritorial organizations and bodies, not economically active, people, unemployed people etc.
        unspecified
        """

        sectors = []
        for s in text.strip().split("\n"):
            i = Sectors()
            i.name = s.strip()
            sectors.append(i)

        return sectors

    @classmethod
    def all(cls):
        return cls.query.order_by(Sectors.name).all()


class Phases(db.Model):
    """
    The phase of the investment.
    """
    __tablename__ = "phases"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<Phase='%s'>" % (self.name)

    @classmethod
    def create_defaults(self):
        text = """
        Planning
        Pre-feasibility
        Feasibility
        Construction
        Complete
        unspecified
        """

        phases = []
        for s in text.strip().split("\n"):
            i = Phases()
            i.name = s.strip()
            phases.append(i)

        return phases

    @classmethod
    def all(cls):
        return cls.query.order_by(Phases.name).all()


class Currencies(db.Model):
    """
    The original currency of the investment.
    """
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<Currency='%s'>" % (self.name)

    @classmethod
    def create_defaults(self):
        text = """
        AFA
        ALL
        DZD
        AOR
        ARS
        AMD
        AWG
        AUD
        AZN
        BSD
        BHD
        BDT
        BBD
        BYN
        BZD
        BMD
        BTN
        BOB
        BWP
        BRL
        GBP
        BND
        BGN
        BIF
        KHR
        CAD
        CVE
        KYD
        XOF
        XAF
        XPF
        CLP
        CNY
        COP
        KMF
        CDF
        CRC
        HRK
        CUP
        CZK
        DKK
        DJF
        DOP
        XCD
        EGP
        SVC
        ERN
        EEK
        ETB
        EUR
        FKP
        FJD
        GMD
        GEL
        GHS
        GIP
        XAU
        XFO
        GTQ
        GNF
        GYD
        HTG
        HNL
        HKD
        HUF
        ISK
        XDR
        INR
        IDR
        IRR
        IQD
        ILS
        JMD
        JPY
        JOD
        KZT
        KES
        KWD
        KGS
        LAK
        LVL
        LBP
        LSL
        LRD
        LYD
        LTL
        MOP
        MKD
        MGA
        MWK
        MYR
        MVR
        MRO
        MUR
        MXN
        MDL
        MNT
        MAD
        MZN
        MMK
        NAD
        NPR
        ANG
        NZD
        NIO
        NGN
        KPW
        NOK
        OMR
        PKR
        XPD
        PAB
        PGK
        PYG
        PEN
        PHP
        XPT
        PLN
        QAR
        RON
        RUB
        RWF
        SHP
        WST
        STD
        SAR
        RSD
        SCR
        SLL
        XAG
        SGD
        SBD
        SOS
        ZAR
        KRW
        LKR
        SDG
        SRD
        SZL
        SEK
        CHF
        SYP
        TWD
        TJS
        TZS
        THB
        TOP
        TTD
        TND
        TRY
        TMT
        AED
        UGX
        XFU
        UAH
        UYU
        USD
        UZS
        VUV
        VEF
        VND
        YER
        ZMK
        ZWL
        unspecified
        """

        currencies = []
        for s in text.strip().split("\n"):
            i = Currencies()
            i.name = s.strip()
            currencies.append(i)

        return currencies

    @classmethod
    def all(cls):
        return cls.query.order_by(Currencies.name).all()


class InvestmentOrigins(db.Model):
    """
    Origin of the investment being made.
    """
    __tablename__ = "investment_origins"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<Investment origin='%s'>" % (self.name)

    @classmethod
    def create_defaults(self):
        text = """
            Afghanistan
            Albania
            Algeria
            Andorra
            Angola
            Antigua and Barbuda
            Argentina
            Armenia
            Australia
            Austria
            Azerbaijan
            Bahamas
            Bahrain
            Bangladesh
            Barbados
            Belarus
            Belgium
            Belize
            Benin
            Bhutan
            Bolivia
            Bosnia and Herzegovina
            Botswana
            Brazil
            Brunei Darussalam
            Bulgaria
            Burkina Faso
            Burundi
            Cabo Verde
            Cambodia
            Cameroon
            Canada
            Central African Republic
            Chad
            Chile
            China
            Colombia
            Comoros
            Congo
            Costa Rica
            Côte d'Ivoire
            Croatia
            Cuba
            Cyprus
            Czech Republic
            Democratic People's Republic of Korea (North Korea)
            Democratic Republic of the Cong
            Denmark
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
            Fiji
            Finland
            France
            Gabon
            Gambia
            Georgia
            Germany
            Ghana
            Greece
            Grenada
            Guatemala
            Guinea
            Guinea-Bissau
            Guyana
            Haiti
            Honduras
            Hungary
            Iceland
            India
            Indonesia
            Iran
            Iraq
            Ireland
            Israel
            Italy
            Jamaica
            Japan
            Jordan
            Kazakhstan
            Kenya
            Kiribati
            Kuwait
            Kyrgyzstan
            Lao People's Democratic Republic (Laos)
            Latvia
            Lebanon
            Lesotho
            Liberia
            Libya
            Liechtenstein
            Lithuania
            Luxembourg
            Macedonia
            Madagascar
            Malawi
            Malaysia
            Maldives
            Mali
            Malta
            Marshall Islands
            Mauritania
            Mauritius
            Mexico
            Micronesia (Federated States of)
            Monaco
            Mongolia
            Montenegro
            Morocco
            Mozambique
            Myanmar
            Namibia
            Nauru
            Nepal
            Netherlands
            New Zealand
            Nicaragua
            Niger
            Nigeria
            Norway
            Oman
            Pakistan
            Palau
            Panama
            Papua New Guinea
            Paraguay
            Peru
            Philippines
            Poland
            Portugal
            Qatar
            Republic of Korea (South Korea)
            Republic of Moldova
            Romania
            Russian Federation
            Rwanda
            Saint Kitts and Nevis
            Saint Lucia
            Saint Vincent and the Grenadines
            Samoa
            San Marino
            Sao Tome and Principe
            Saudi Arabia
            Senegal
            Serbia
            Seychelles
            Sierra Leone
            Singapore
            Slovakia
            Slovenia
            Solomon Islands
            Somalia
            South Africa
            South Sudan
            Spain
            Sri Lanka
            Sudan
            Suriname
            Swaziland
            Sweden
            Switzerland
            Syrian Arab Republic
            Tajikistan
            Thailand
            Timor-Leste
            Togo
            Tonga
            Trinidad and Tobago
            Tunisia
            Turkey
            Turkmenistan
            Tuvalu
            Uganda
            Ukraine
            United Arab Emirates
            United Kingdom of Great Britain and Northern Ireland
            United Republic of Tanzania
            United States of America
            Uruguay
            Uzbekistan
            Vanuatu
            Venezuela
            Vietnam
            Yemen
            Zambia
            Zimbabwe
            unspecified
            """

        countries = []
        for s in text.strip().split("\n"):
            i = InvestmentOrigins()
            i.name = s.strip()
            countries.append(i)

        return countries

    @classmethod
    def all(cls):
        return cls.query.order_by(InvestmentOrigins.name).all()


class InvestmentLocations(db.Model):
    """
    Origin of the investment being made.
    """
    __tablename__ = "investment_locations"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<Investment location='%s'>" % (self.name)


class Involvements(db.Model):
    """
    The phase of the investment.
    """
    __tablename__ = "involvements"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<Phase='%s'>" % (self.name)

    @classmethod
    def create_defaults(self):
        text = """
        Department of Trade and Industry
        Economic Development Department
        Department of Small Business Development
        National Treasury
        Investment Promotion Agency
        Provincial Government or Agency
        Municipal Government or Agency
        Special Economic Zone
        State Owned Enterprises
        Sectoral Regulator or Agency
        Other
        None
        unspecified
        """

        involvements = []
        for s in text.strip().split("\n"):
            i = Phases()
            i.name = s.strip()
            involvements.append(i)

        return involvements

    @classmethod
    def all(cls):
        return cls.query.order_by(Involvements.name).all()


class Industries(db.Model):
    """
    The phase of the investment.
    """
    __tablename__ = "industries"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<Phase='%s'>" % (self.name)

    @classmethod
    def create_defaults(self):
        text = """
        Agriculture
        Mining
        Manufacturing
        Utilities
        Construction
        Trade
        Transport
        Finance
        Community and social services
        Private households
        Other
        unspecified
        """

        industries = []
        for s in text.strip().split("\n"):
            i = Phases()
            i.name = s.strip()
            industries.append(i)

        return industries

    @classmethod
    def all(cls):
        return cls.query.order_by(Industries.name).all()
