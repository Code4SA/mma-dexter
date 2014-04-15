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

    id           = Column(Integer, primary_key=True)
    name         = Column(String(100), index=True, nullable=False, unique=True)
    domain       = Column(String(100), unique=True)
    medium_type  = Column(String(100), index=True, nullable=False)
    medium_group = Column(String(100))

    @classmethod
    def create_defaults(cls):
        text = """
Beeld|daily|beeld.com|
Business Day|daily|bdlive.co.za|
Cape Argus|daily|iol.co.za/capeargus|
Cape Times|daily|iol.co.za/capetimes|
City Press|weekly|citypress.co.za|
Daily Dispatch|daily|dispatch.co.za|
Daily Maverick|daily|dailymaverick.co.za|
Daily Sun|daily|dailysun.mobi|
Daily Voice|daily|iol.co.za/2.1894|
Die Burger|daily|dieburger.com|
Etv English News|television||etv
Etv Sunrise|television||etv
Grocott's Mail|daily|grocotts.co.za|
Ilanga|ONLINE|ilanganews.co.za|
IOL|daily|iol.co.za|
Isolezwe|daily|iol.co.za/isolezwe|
Kaya FM|radio||
Lesedi FM|radio||
Ligwalagwala FM|radio||
Lotus FM|radio||
Mail and Guardian|weekly|mg.co.za|
Metro FM|radio||
Motsweding FM|radio||
Munghana Lonene FM|radio||
News24|daily|news24.com|
Phalaphala FM|radio||
Post|daily|iol.co.za/thepost|
Power FM|radio||
Public Eye|ONLINE|publiceye.co.ls|
RSG FM|radio||
SA Breaking News|ONLINE|sabreakingnews.co.za|
SABC 1 Elections programs|television||SABC 1
SABC 1 Isizulu/Isixhosa News|television||SABC 1
SABC 1 Siswati/Ndebele News|television||SABC 1
SABC 2 Afrikaans News|television||SABC 2
SABC 2 Morning Live|television||SABC 2
SABC 2 Sesotho/Setswana News|television||SABC 2
SABC 2 Special Elections Programs|television||SABC 2
SABC 2 Xitsonga/Tschivenda News|television||SABC 2
SABC 3 English News|television||SABC 3
SAfm|radio||
Saturday Star|weekly|iol.co.za/saturday-star|
Sowetan|daily|sowetanlive.co.za|
Sunday Independent|weekly|iol.co.za/sundayindependant|
Sunday Sun|weekly||
Sunday Times|weekly|timeslive.co.za/sundaytimes|
Sunday Tribune|ONLINE|iol.co.za/sunday-tribune|
Sunday World|weekly|sundayworld.co.za|
Talk Radio 702|radio||
Citizen|daily|citizen.co.za|
The Daily News|daily|iol.co.za/dailynews|
The Free State Times|PRINT|fstimes.co.za|
The Herald|daily|heraldlive.co.za|
The Independent on Saturday|weekly|iol.co.za/ios|
The Mercury|daily|iol.co.za/mercury|
The New Age|daily|thenewage.co.za|
The Star|daily|iol.co.za/the-star|
The Witness|daily|witness.co.za|
Thobela FM|radio||
Times|daily|timeslive.co.za|
Ukhozi FM|radio||
Umhlobo Wenene FM|radio||
Unknown|other||
Volksbad|daily|volksblad.com|
Weekend Argus|weekly||
Weekend Dispatch|weekly||
Weekend Post|daily|weekendpost.co.za|
            """

        mediums = []
        for medium in text.strip().split("\n"):
            m = Medium()

            components = medium.strip().split('|')
            m.name, m.medium_type, m.domain, m.medium_group = components
            if not m.domain:
                m.domain = None
            if not m.medium_group:
                m.medium_group = None

            mediums.append(m)

        return mediums
