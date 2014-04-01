from sqlalchemy import (
    Column,
    Integer,
    String,
    )

from .support import db

class Medium(db.Model):
    """ A medium from which articles are drawn, such as a newspaper
    or radio station.
    """
    __tablename__ = 'mediums'

    id          = Column(Integer, primary_key=True)
    name        = Column(String(100), index=True, nullable=False, unique=True)
    domain      = Column(String(100), unique=True)
    medium_type = Column(String(100), index=True, nullable=False)

    @classmethod
    def create_defaults(cls):
        text = """
            Unknown|UNKNOWN
            Beeld|PRINT
            Business Day|PRINT|bdlive.co.za
            Cape Argus|PRINT
            Citizen|PRINT|citizen.co.za
            City Press|PRINT|citypress.co.za
            Daily Dispatch|PRINT
            Daily Maverick|ONLINE
            Daily Sun|PRINT|dailysun.mobi
            Daily Voice|PRINT
            Die Burger|PRINT
            EP Herald|PRINT
            Etv English News|TELEVISION
            Grocotts|PRINT
            IOL|ONLINE|iol.co.za
            Kaya FM|RADIO
            Lesedi FM|RADIO
            Ligwalagwala FM|RADIO
            Mail and Guardian|PRINT|mg.co.za
            Metro FM|RADIO
            Motsweding FM|RADIO
            News24|ONLINE|news24.com
            Phalaphala FM|RADIO
            Public Eye|PRINT
            RSG FM|RADIO
            SABC 1 Elections programs|TELEVISION
            SABC 1 Isizulu/Isixhosa News|TELEVISION
            SABC 2 Afrikaans News|TELEVISION
            SABC 2 Sesotho/Setswana News|TELEVISION
            SABC 2 Special Elections Programs|TELEVISION
            SABC 3 English News|TELEVISION
            Safm|RADIO
            Saturday Star|PRINT
            Sowetan|PRINT|sowetanlive.co.za
            Sunday Independent|PRINT
            Sunday Sun|PRINT
            Sunday Times|PRINT
            Sunday World|PRINT
            Talk Radio 702|RADIO
            The Free State Times|PRINT
            The New Age|PRINT
            The Star|PRINT
            Thobela FM|RADIO
            Times|PRINT|timeslive.co.za
            Ukhozi FM|RADIO
            Umhlobo Wenene FM|RADIO
            Volksbad|PRINT
            Weekend Argus|PRINT
            Weekend Dispatch|PRINT
            """

        mediums = []
        for medium in text.strip().split("\n"):
            m = Medium()
            components = medium.strip().split('|')
            m.name, m.medium_type = components[0], components[1]
            if len(components) > 2:
                m.domain = components[2]
            mediums.append(m)

        return mediums
