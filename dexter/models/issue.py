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

    id        = Column(Integer, primary_key=True)
    name      = Column(String(100), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<Issue name='%s'>" % (self.name.encode('utf-8'),)

    @classmethod
    def create_defaults(self):
        text = """
Issue of human rights is broadly raised
Issues of race/racism are raised
Issues of homophobia are raised
Issues of gender and gender discrimination is raised (including gender quota in parties & govt)
Issues of gender-based violence is raised
Issues of people living with AIDS is raised
Issues of myths surrounding AIDS
Issue of xenophobia is raised
Issues of any other discrimination is raised
Issues of differently-abled people is raised
Issues of children's rights is raised
Issues of child abuse are raised
Issue of diversity in sport
Issues of sexual harassment are raised
Report raises issues concerning war crimes
Issues of No-go-areas and political intolerance are raised
Report raises issues of free and fair elections
The report interrogates smear campaigns between parties
Issues of land and access to land are raised
Economic policy issues are raised
Issues relating to leadership are raised (at all levels: party, national, provincial and local govt)
Issues of service delivery are broadly raised
Issues of job creation are raised
The report raises issues of crime and corruption
        """

        issues = []
        for s in text.strip().split("\n"):
            i = Issue()
            i.name = s.strip()
            issues.append(i)

        return issues
