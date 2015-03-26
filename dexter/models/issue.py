from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Float,
    Index,
    Table
)

from ..app import db


class DocumentIssue(db.Model):
    """
    An issue linked to a document.
    """
    __tablename__ = "document_issues"

    id        = Column(Integer, primary_key=True)
    doc_id    = Column(Integer, ForeignKey('documents.id'), index=True)
    issue_id  = Column(Integer, ForeignKey('issues.id'), index=True, nullable=False)

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
    analysis_nature_id = Column(Integer, ForeignKey("analysis_natures.id"), default=1, nullable=False)

    def __repr__(self):
        return "<Issue name='%s'>" % (self.name.encode('utf-8'),)

    @classmethod
    def create_defaults(self):
        text = """
free and fair elections
political party funding
two-thirds majority
xenophobia
homophobia
gender discrimination
gender parity
gender-based violence & rape
sexual harassment
children's rights
child abuse
diversity in sport
police brutality
death penalty
war crimes
terrorism
media and ICTs
BEE and BBBEE
economic policy
foreign policy
leadership
job creation
unemployment
land reform
rural development
access to housing
access to education
access to sanitation
access to health
access to water
access to electricity
access to justice
        """

        issues = []
        for s in text.strip().split("\n"):
            i = Issue()
            i.name = s.strip()
            i.description = i.name
            issues.append(i)

        return issues
