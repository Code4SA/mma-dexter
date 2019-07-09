from itertools import groupby
from urlparse import urlparse

from tld import get_tld

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    )
from sqlalchemy.orm import relationship

from ..app import db

class Medium(db.Model):
    """ A medium from which articles are drawn, such as a newspaper
    or radio station.
    """
    __tablename__ = 'mediums'

    id           = Column(Integer, primary_key=True)
    name         = Column(String(100), index=True, nullable=False, unique=True)
    domain       = Column(String(100), index=True)
    medium_type  = Column(String(100), index=True, nullable=False)
    medium_group = Column(String(100))
    parent_org   = Column(String(100))
    country_id   = Column(Integer, ForeignKey('countries.id'), nullable=False, index=True)

    country = relationship("Country", backref='mediums')

    def group_name(self):
        return self.medium_group or self.name

    @classmethod
    def is_tld_exception(cls, url):
        """ Test if the url falls within one of the exceptions, 
        this is intended to handle instances where get_tld() 
        calls fail to recognise urls (eg: .co.tz fials...)
        """
        url_exceptions = [
            'thecitizen.co.tz',
            'dailynews.co.tz',
            'nigeriatoday.ng',
            'nta.ng',
            'nan.ng',
            'leadership.ng',
            'independent.ng',
            'guardian.ng',
            'dailytimes.ng',
            'theinterview.ng',
            'city-press.news24.com'
        ]
        for ex in url_exceptions: 
            # check if it exists in the url add buffer for [https://www.] characters at start
            if ex in url[:len(ex)+12]:
                return ex
        
        return None

    @classmethod
    def for_url(cls, url):
        domain = get_tld(url, fail_silently=True)
        # fail silently
        
        if domain is None:
            domain = cls.is_tld_exception(url)
        
        if domain is None:
            return None

        parts = urlparse(url)

        # iol.co.za/isolezwe
        domain = domain + parts.path

        # explicitly look for city-press, subdomain does not play nice with current Dexter code
        if 'city-press.news24.com' in url:
            medium = Medium.query.get(5)
            return medium

        else:
        # find the medium with the longest matching domain
            for medium in sorted(Medium.query.all(), key=lambda m: len(m.domain or ''), reverse=True):
                if medium.domain and domain.startswith(medium.domain):
                    return medium

        return None


    @classmethod
    def for_select_widget(cls):
        from . import Country
        mediums = cls.query.join(Country).all()
        mediums.sort(key=lambda m: [m.country.name, m.name])

        choices = []
        for group, items in groupby(mediums, lambda m: m.country.name):
          choices.append((group, [[str(m.id), m.name] for m in items]))

        return choices

    @classmethod
    def create_defaults(cls):
        from . import Country

        text = """
Beeld|print - daily|beeld.com||za
Business Day|print - daily|bdlive.co.za||za
Cape Argus|print - daily|iol.co.za/capeargus||za
Cape Times|print - daily|iol.co.za/capetimes||za
City Press|print - weekly|citypress.co.za||za
Daily Dispatch|print - daily|dispatch.co.za||za
Daily Maverick|daily|dailymaverick.co.za||za
Daily Sun|print - daily|dailysun.mobi||za
Daily Voice|print - daily|iol.co.za/2.1894||za
Die Burger|print - daily|dieburger.com||za
Etv English News|television||etv|za
Etv Sunrise|television||etv|za
Grocott's Mail|print - daily|grocotts.co.za||za
Ilanga|ONLINE|ilanganews.co.za||za
IOL|online|iol.co.za||za
Isolezwe|print - daily|iol.co.za/isolezwe||za
Kaya FM|radio|||za
Lesedi FM|radio|||za
Ligwalagwala FM|radio|||za
Lotus FM|radio|||za
Mail and Guardian|print - weekly|mg.co.za||za
Metro FM|radio|||za
Motsweding FM|radio|||za
Munghana Lonene FM|radio|||za
News24|online|news24.com||za
Phalaphala FM|radio|||za
Post|print - daily|iol.co.za/thepost||za
Power FM|radio|||za
Public Eye|ONLINE|publiceye.co.ls||za
RSG FM|radio|||za
SA Breaking News|ONLINE|sabreakingnews.co.za||za
SABC 1 Elections programs|television||SABC 1|za
SABC 1 Isizulu/Isixhosa News|television||SABC 1|za
SABC 1 Siswati/Ndebele News|television||SABC 1|za
SABC 2 Afrikaans News|television||SABC 2|za
SABC 2 Morning Live|television||SABC 2|za
SABC 2 Sesotho/Setswana News|television||SABC 2|za
SABC 2 Special Elections Programs|television||SABC 2|za
SABC 2 Xitsonga/Tschivenda News|television||SABC 2|za
SABC 3 English News|television||SABC 3|za
SAfm|radio|||za
Saturday Star|print - weekly|iol.co.za/saturday-star||za
Sowetan|print - daily|sowetanlive.co.za||za
Sunday Independent|print - weekly|iol.co.za/sundayindependant||za
Sunday Sun|print - weekly|||za
Sunday Times|print - weekly|timeslive.co.za/sundaytimes||za
Sunday Tribune|ONLINE|iol.co.za/sunday-tribune||za
Sunday World|print - weekly|sundayworld.co.za||za
Talk Radio 702|radio|||za
Citizen|print - daily|citizen.co.za||za
The Daily News|print - daily|iol.co.za/dailynews||za
The Free State Times|PRINT|fstimes.co.za||za
The Herald|print - daily|heraldlive.co.za||za
The Independent on Saturday|print - weekly|iol.co.za/ios||za
The Mercury|print - daily|iol.co.za/mercury||za
The New Age|print - daily|thenewage.co.za||za
The Star|print - daily|iol.co.za/the-star||za
The Witness|print - daily|witness.co.za||za
Thobela FM|radio|||za
Times|print - daily|timeslive.co.za||za
Ukhozi FM|radio|||za
Umhlobo Wenene FM|radio|||za
Unknown|other|||za
Volksbad|print - daily|volksblad.com||za
Weekend Argus|print - weekly|||za
Weekend Dispatch|print - weekly|||za
Weekend Post|print - daily|weekendpost.co.za||za
Namibian|online|namibian.com.na||na
Daily Nation|online|zambiadailynation.com||zm
Lusaka Times|online|lusakatimes.com||zm
Zambian Watchdog|online|zambianwatchdog.com||zm
Zambia Daily Mail|online|daily-mail.co.zm||zm
Post Zambia|online|postzambia.com||zm
Times of Zambia|online|times.co.zm||zm
The Chronicle|online|chronicle.co.zw||zw
NewsDay Zimbabwe|online|newsday.co.zw||zw
The Citizen Tanzania|online|thecitizen.co.tz||tz
Deutsche Welle|online|dw.com||de
BBC|online|bbc.com||gb
Daily Nation (Kenya)|online|nation.co.ke||ke
Standard Digital|online|standardmedia.co.ke||ke
The Star (Kenya)|online|the-star.co.ke||ke
The East African|online|theeastafrican.co.ke||ke
Daily News (Tanzania)|online|dailynews.co.tz||tz
Daily News (Zimbabwe)|online|dailynews.co.zw||tz
            """

        mediums = []
        for medium in text.strip().split("\n"):
            m = Medium()

            components = medium.strip().split('|')
            m.name, m.medium_type, m.domain, m.medium_group, country = components
            if not m.domain:
                m.domain = None
            if not m.medium_group:
                m.medium_group = None

            if country:
              m.country = Country.query.filter(Country.code == country).one()

            mediums.append(m)

        return mediums
