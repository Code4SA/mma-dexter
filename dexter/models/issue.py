from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Float,
    Index
    )

from .support import db

class DocumentIssue(db.Model):
    """
    An issue linked to a document.
    """
    __tablename__ = "document_issues"

    id        = Column(Integer, primary_key=True)
    doc_id    = Column(Integer, ForeignKey('documents.id'), index=True)
    issue_id  = Column(Integer, index=True, nullable=False)

    # associations

    def __repr__(self):
        return "<DocumentIssue issue='%s', doc=%s>" % (
                self.issue.encode('utf-8'), self.document)

Index('doc_issue_doc_id_issue_ix', DocumentIssue.doc_id, DocumentIssue.issue_id, unique=True)

class Issue(db.Model):
    """
    An issue raised in a document.
    """
    __tablename__ = "issues"

    id          = Column(Integer, primary_key=True)
    name        = Column(String(50), index=True, nullable=False, unique=True)
    description = Column(String(100), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<Issue name='%s'>" % (self.name.encode('utf-8'),)

    @classmethod
    def create_defaults(self):
        text = """
human rights|Issue of human rights is broadly raised
race/racism|Issues of race/racism are raised
homophobia|Issues of homophobia are raised
gender and gender discrimination|Issues of gender and gender discrimination is raised (including gender quota in parties & govt)
gender-based violence|Issues of gender-based violence is raised
living with AIDS|Issues of people living with AIDS is raised
AIDS myths|Issues of myths surrounding AIDS
xenophobia|Issue of xenophobia is raised
general discrimination|Issues of any other discrimination is raised
disabilities|Issues of differently-abled people is raised
children's rights|Issues of children's rights is raised
child abuse|Issues of child abuse are raised
diversity in sport|Issue of diversity in sport
sexual harassment|Issues of sexual harassment are raised
war crimes|Report raises issues concerning war crimes
political intolerance|Issues of No-go-areas and political intolerance are raised
free and fair elections|Report raises issues of free and fair elections
political smear campaigns|The report interrogates smear campaigns between parties
land|Issues of land and access to land are raised
economic policy|Economic policy issues are raised
elected leadership|Issues relating to leadership are raised (at all levels: party, national, provincial and local govt)
service delivery|Issues of service delivery are broadly raised
job creation|Issues of job creation are raised
crime and corruption|The report raises issues of crime and corruption
        """

        issues = []
        for s in text.strip().split("\n"):
            i = Issue()
            i.name, i.description = s.strip().split('|')
            issues.append(i)

        return issues
