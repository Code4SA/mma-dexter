from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Float,
    Index,
    Table
)

from .support import db


class SourceRole(db.Model):
    """
    A role linked to a document source.
    """
    __tablename__ = "source_roles"

    id          = Column(Integer, primary_key=True)
    name        = Column(String(100), index=True, nullable=False, unique=True)
    analysis_nature_id = Column(Integer, ForeignKey("analysis_natures.id"))

    def __repr__(self):
        return "<SourceRole name='%s'>" % (self.name.encode('utf-8'),)

    @classmethod
    def create_defaults(self):
        text = """
Learner, student|2
Baby/infant|2
Toddler|2
Child |2
Teenager|2
Youth - be sure it is not a child!|2
Survivor|2
Victim|2
Missing child|2
Caregiver: domestic or nanny|2
Child Soldier|2
Child Slave/ Trafficked Child|2
Refugee|2
Sick child|2
Child with disability|2
Child in need|2
Head of household|2
Orphan|2
Perpetrator|2
Criminal|2
Child Offender|2
Gang member|2
Suspect|2
Ward of court|2
Award winners|2
Entertainer|2
Hero|2
Activist/protestor|2
Fan/supporter|2
Friend|2
Member of a group  of children|2
Leader|2
Spokesperson|2
Sportsperson|2
Artist|2
Sex Worker|2
Sex Object|2
Beauty contestant/model|2
Labourer|2
Street Child|2
Child as member of family unit, e.g., son daughter, nephew etc.|2
Dependents|2
Other|2
Unknown|2
Child Witness|2
Teenage Mother|2
        """

        roles = []
        for x in text.strip().split("\n"):
            r = SourceRole()

            parts = x.strip().split("|", 1)
            r.name = parts[0]
            r.analysis_nature_id = int(parts[1])

            roles.append(r)

        return roles
