from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    )

from itertools import groupby
from .support import db

class Topic(db.Model):
    """
    Primary topic for an article.
    """
    __tablename__ = "topics"

    id        = Column(Integer, primary_key=True)
    name      = Column(String(150), index=True, nullable=False, unique=True)
    group     = Column(String(100))
    analysis_nature_id = Column(Integer, ForeignKey('analysis_natures.id'), index=True, nullable=False, default=1)

    def __repr__(self):
        return "<Topic name='%s'>" % (self.name.encode('utf-8'),)


    @classmethod
    def for_select_widget(cls, topics):
        choices = []
        topics.sort(key=lambda t: [t.group, t.name])
        for group, items in groupby(topics, lambda t: t.group):
            choices.append((group, [[str(t.id), t.name] for t in items]))
        return choices


    @classmethod
    def create_defaults(self):
        text = """
1|Voter education & registration
1|Election fraud
1|Election funding
1|Election logistics 
1|Election results
1|Opinion polls
1|Political party campaigning (only when no other code applies)
1|Political party manifesto outlines / analyses
1|Political party coalitions & co-operation
1|Political party politics (internal &/or external)
1|Political violence & intimidation
1|Service delivery
1|Education
1|Environment
1|Health
1|HIV & Aids
1|Corruption (govt, political party, private sector)
1|Crime
1|Justice system
1|Housing
1|Land
1|Gender
1|Children
1|Poverty
1|Race / Racism
1|Refugees / Migration
1|Affirmative action
1|Diplomacy
1|International politics
1|Personalities and profiles
1|Demonstrations / Protests
1|Development
1|Disaster
1|Economics
1|Arts / Culture / Entertainment / Religion
1|Human rights
1|Labour
1|Media
1|Science
1|Sport
1|Disabilities
1|Other (Last Resort)
"""
        text = """
2|Economics - Includes business, corporate news, finance issues, trade agreements|Economics
2|Politics (International) - Diplomacy efforts, political news from outside South Africa|Politics (International)
2|Disaster/Accident - Earthquakes, famine, typhoons, accidents, tragedy|Disaster/Accident
2|Conflict, Political Violence - Demonstration, Protests, War|Conflict, Political Violence
2|Crime - Murder, robbery, hijacking, theft, Corruption-bribery, fraud at both government and corporate levels|Crime
2|Justic system - Court rulings, constitutional issues, legislation, bills, amendments, judicial system|Justice System
2|SA National Politics - Includes SA Gov & Parliament-national government, national issues, parliament, national politics|SA National Politics
2|Provincial & Local Govt - Includes municipalities, policies affecting only certain provinces, local government finance|Provincial & Local Govt
2|Housing - Includes policies, lack of housing, government initiatives|Housing
2|Social Welfare - Policies on welfare grants, pension, child grants|Social Welfare
2|Poverty Rate - Policies|Poverty rate
2|Health - general health issues, diabetes, cancer, nutrition, excludes HIV/AIDS|Health
2|Development - Policies, projects|Development
2|Environment - Pollution, extinction of animal/plant species|Environment
2|Media and arts - New media, freedom of expression, entertainment, culture-theatre, lifestyle issues, fashion, religion and tradition|Media and Arts
2|Sport - news on sport events, reports, athletes, policies|Sport
2|Personalities/Profiles - Features on prominent personalities or upcoming people|Personalities/Profiles
2|Cultural practices and traditions|Cultural practicies and traditions
2|Child Labour - exploitation of children for work as cheap labour|Child Abuse
2|Child Pornography|Child Abuse
2|General when codes below don't apply|Child Abuse
2|Physical Abuse-beatings, burnings|Child Abuse
2|Mental & Emotional Abuse-verbal and consistently making derogatory remarks|Child Abuse
2|Child Prostitution-use of children for sex work|Child Abuse
2|Child Abduction/ Trafficking/ Slavery - abducting a child for sexual purposes or slavery|Child Abuse
2|Kidnapping- taking a child ifor ransom purposes|Child Abuse
2|Child Rape-non-consensual includes penetrative and non-penetrative sex with a  minor includes statutory rape|Child Abuse
2|Sexual Abuse- the abuse of boys and girls and included indecent assault and sodomy|Child Abuse
2|Child Neglect-failure to adequately attend to a child's needs|Child Abuse
2|Maintenance and child support-bills, divorce cases|Child Abuse
2|Adoption - international local and other related issues|Adoption
2|Education General - where the codes below do not apply.|Education
2|Policy related: state of schools, education policies, etc.|Education
2|Events and Achievements: school fun days, awards etc.|Education
2|Violence: levels of violence among learners and school related disasters and tragedies.|Education
2|Science-reports about new inventions, technology|Science
2|Human Rights-includes a variety of rights|Human Rights
2|Gender - where the central focus of the story is on a gender related element.|Gender
2|Racism & Xenophobia- incidents of racism & discrimination based on a person's ethnicity or nationality|Racism and Xenophobia
2|Disabilities-mental or physical|Disabilities
2|Family-reports on values, the ideal family or focus on a specific family|Family
2|HIV/AIDS - general when codes below don't apply|HIV/AIDS
2|Aids Orphans/children affected by HIV, where children have parents/caregivers due to HIV/AIDS|Treatment of HIV/AIDS
2|Sex Education-items on practicing safe sex in relation to HIV/AIDS and in STD's|Sex Education
2|Treatment of HIV/AIDS-items relating to ARVs or nevirapine or treatment in general|Treatment of HIV/AIDS
2|Funds-monies donated for the treatment of HIV|Funds
2|Teenage pregnancy|Teenage Pregnancy
2|Substance Abuse-drugs and alcohol|Substance Abuse
2|Refugee children-asylum seekers, refugees rights|Refugee Children
2|Other- to be used as a last resort|Z Other
2|Not Relevant - for Television and Radio only|ZZ Not Relevant
        """

        topics = []
        for s in text.strip().split("\n"):
            parts = s.split("|")

            t = Topic()
            t.analysis_nature_id = int(parts[0])
            t.name = parts[1].strip()
            if len(parts) > 2:
              t.group = parts[2]
            topics.append(t)

        return topics
