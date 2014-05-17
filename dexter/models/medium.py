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
    parent_org   = Column(String(100))

    def group_name(self):
        return self.medium_group or self.name

    @classmethod
    def create_defaults(cls):
        text = """
Beeld|print - daily|beeld.com|
Business Day|print - daily|bdlive.co.za|
Cape Argus|print - daily|iol.co.za/capeargus|
Cape Times|print - daily|iol.co.za/capetimes|
City Press|print - weekly|citypress.co.za|
Daily Dispatch|print - daily|dispatch.co.za|
Daily Maverick|daily|dailymaverick.co.za|
Daily Sun|print - daily|dailysun.mobi|
Daily Voice|print - daily|iol.co.za/2.1894|
Die Burger|print - daily|dieburger.com|
Etv English News|television||etv
Etv Sunrise|television||etv
Grocott's Mail|print - daily|grocotts.co.za|
Ilanga|ONLINE|ilanganews.co.za|
IOL|online|iol.co.za|
Isolezwe|print - daily|iol.co.za/isolezwe|
Kaya FM|radio||
Lesedi FM|radio||
Ligwalagwala FM|radio||
Lotus FM|radio||
Mail and Guardian|print - weekly|mg.co.za|
Metro FM|radio||
Motsweding FM|radio||
Munghana Lonene FM|radio||
News24|online|news24.com|
Phalaphala FM|radio||
Post|print - daily|iol.co.za/thepost|
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
Saturday Star|print - weekly|iol.co.za/saturday-star|
Sowetan|print - daily|sowetanlive.co.za|
Sunday Independent|print - weekly|iol.co.za/sundayindependant|
Sunday Sun|print - weekly||
Sunday Times|print - weekly|timeslive.co.za/sundaytimes|
Sunday Tribune|ONLINE|iol.co.za/sunday-tribune|
Sunday World|print - weekly|sundayworld.co.za|
Talk Radio 702|radio||
Citizen|print - daily|citizen.co.za|
The Daily News|print - daily|iol.co.za/dailynews|
The Free State Times|PRINT|fstimes.co.za|
The Herald|print - daily|heraldlive.co.za|
The Independent on Saturday|print - weekly|iol.co.za/ios|
The Mercury|print - daily|iol.co.za/mercury|
The New Age|print - daily|thenewage.co.za|
The Star|print - daily|iol.co.za/the-star|
The Witness|print - daily|witness.co.za|
Thobela FM|radio||
Times|print - daily|timeslive.co.za|
Ukhozi FM|radio||
Umhlobo Wenene FM|radio||
Unknown|other||
Volksbad|print - daily|volksblad.com|
Weekend Argus|print - weekly||
Weekend Dispatch|print - weekly||
Weekend Post|print - daily|weekendpost.co.za|
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
