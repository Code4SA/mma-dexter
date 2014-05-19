from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    )

from .support import db

class Topic(db.Model):
    """
    Primary topic for an article.
    """
    __tablename__ = "topics"

    id        = Column(Integer, primary_key=True)
    name      = Column(String(100), index=True, nullable=False, unique=True)
    analysis_nature_id = Column(Integer, ForeignKey('analysis_natures.id'), index=True, nullable=False, default=1)

    def __repr__(self):
        return "<Topic name='%s'>" % (self.name.encode('utf-8'),)

    @classmethod
    def create_defaults(self):
        text = """
Voter education & registration
Election fraud
Election funding
Election logistics 
Election results
Opinion polls
Political party campaigning (only when no other code applies)
Political party manifesto outlines / analyses
Political party coalitions & co-operation
Political party politics (internal &/or external)
Political violence & intimidation
Service delivery
Education
Environment
Health
HIV & Aids
Corruption (govt, political party, private sector)
Crime
Justice system
Housing
Land
Gender
Children
Poverty
Race / Racism
Refugees / Migration
Affirmative action
Diplomacy
International politics
Personalities and profiles
Demonstrations / Protests
Development
Disaster
Economics
Arts / Culture / Entertainment / Religion
Human rights
Labour
Media
Science
Sport
Disabilities
Other (Last Resort)
        """

        topics = []
        for s in text.strip().split("\n"):
            g = Topic()
            g.name = s.strip()
            topics.append(g)

        return topics
