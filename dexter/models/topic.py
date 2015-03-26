from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    )

from itertools import groupby
from ..app import db

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


    def sort_key(self):
        try:
            # sort ("10. Foo", "10.2 Bar") by the code
            parts = (self.group.split(' ', 1)[0], self.name.split(' ', 1)[0])

            return [int(k.replace('.', '')) for k in parts]
        except:
            return (self.group, self.name)


    @classmethod
    def for_select_widget(cls, topics):
        choices = []
        topics.sort(key=cls.sort_key)
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
2|1.1. Adoption - international local and other related issues|1. Adoption
2|2.1. Child Labour - exploitation of children for work as cheap labour|2. Child Abuse
2|2.2. Child Pornography|2. Child Abuse
2|2.3. General when codes below don't apply|2. Child Abuse
2|2.4. Physical Abuse-beatings, burnings|2. Child Abuse
2|2.5. Mental & Emotional Abuse-verbal and consistently making derogatory remarks|2. Child Abuse
2|2.6. Child Prostitution-use of children for sex work|2. Child Abuse
2|2.7. Child Abduction/ Trafficking/ Slavery - abducting a child for sexual purposes or slavery|2. Child Abuse
2|2.8. Kidnapping- taking a child ifor ransom purposes|2. Child Abuse
2|2.9. Child Rape-non-consensual includes penetrative and non-penetrative sex with a  minor includes statutory rape|2. Child Abuse
2|2.10. Sexual Abuse- the abuse of boys and girls and included indecent assault and sodomy|2. Child Abuse
2|2.11. Child Neglect-failure to adequately attend to a child's needs|2. Child Abuse
2|2.12. Maintenance and child support-bills, divorce cases|2. Child Abuse
2|3.1. Conflict, Political Violence - Demonstration, Protests, War|3. Conflict, Political Violence
2|4.1. Crime - Murder, robbery, hijacking, theft, Corruption-bribery, fraud at both government and corporate levels|4. Crime
2|5.1. Cultural practices and traditions|5. Cultural practicies and traditions
2|6.1. Development - Policies, projects|6. Development
2|7.1. Disabilities-mental or physical|7. Disabilities
2|8.1. Disaster/Accident - Earthquakes, famine, typhoons, accidents, tragedy|8. Disaster/Accident
2|9.1. Economics - Includes business, corporate news, finance issues, trade agreements|9. Economics
2|10.1.  Education General - where the codes below do not apply.|10. Education
2|10.2. Policy related: state of schools, education policies, etc.|10. Education
2|10.3. Events and Achievements: school fun days, awards etc.|10. Education
2|10.4. Violence: levels of violence among learners and school related disasters and tragedies.|10. Education
2|11.1. Environment - Pollution, extinction of animal/plant species|11. Environment
2|12.1. Family-reports on values, the ideal family or focus on a specific family|12. Family
2|13.1. Funds-monies donated for the treatment of HIV|13. Funds
2|14.1. Gender - where the central focus of the story is on a gender related element.|14. Gender
2|15.1. Health - general health issues, diabetes, cancer, nutrition, excludes HIV/AIDS|15. Health
2|16.1. Aids Orphans/children affected by HIV, where children have parents/caregivers due to HIV/AIDS|16. HIV/AIDS
2|16.2. Treatment of HIV/AIDS-items relating to ARVs or nevirapine or treatment in general|16. HIV/AIDS
2|16.3. Sex Education-items on practicing safe sex in relation to HIV/AIDS and in STD's|16. HIV/AIDS
2|16.4. HIV/AIDS - general when other codes  don't apply|16. HIV/AIDS
2|17.1. Housing - Includes policies, lack of housing, government initiatives|17. Housing
2|18.1. Human Rights-includes a variety of rights|18. Human Rights
2|19.1. Justice system - Court rulings, constitutional issues, legislation, bills, amendments, judicial system|19. Justice System
2|20.1. Media and arts - New media, freedom of expression, entertainment, culture-theatre, lifestyle issues, fashion, religion and tradition|20. Media and Arts
2|21.1. Personalities/Profiles - Features on prominent personalities or upcoming people|21. Personalities/Profiles
2|22.1. Politics (International) - Diplomacy efforts, political news from outside South Africa|22. Politics
2|22.2. SA National Politics - Includes SA Gov & Parliament-national government, national issues, parliament, national politics|22. Politics
2|22.3. Provincial & Local Govt - Includes municipalities, policies affecting only certain provinces, local government finance|22. Politics
2|23.1. Poverty Rate - Policies|23. Poverty rate
2|24.1. Racism & Xenophobia- incidents of racism & discrimination based on a person's ethnicity or nationality|24. Racism and Xenophobia
2|25.1. Refugee children-asylum seekers, refugees rights|25. Refugee Children
2|26.1. Science-reports about new inventions, technology|26. Science
2|27.1. Social Welfare - Policies on welfare grants, pension, child grants|27. Social Welfare
2|28.1. Sport - news on sport events, reports, athletes, policies|28. Sports
2|29.1. Substance Abuse-drugs and alcohol|29. Substance Abuse
2|30.1. Teenage pregnancy|30. Teenage Pregnancy
2|31.1. Other- to be used as a last resort|31. Other
        """

        topics = []
        for s in text.strip().split("\n"):
            parts = s.split("|")

            t = Topic()
            t.analysis_nature_id = int(parts[0])
            t.name = parts[1].strip()

            if len(parts) > 2:
              t.group = parts[2].strip()

            topics.append(t)

        return topics
