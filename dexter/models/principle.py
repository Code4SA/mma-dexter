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


class Principle(db.Model):
    """
    A principle linked to a document, either supported or violated.
    """
    __tablename__ = "principles"

    id          = Column(Integer, primary_key=True)
    name        = Column(String(50), nullable=False, unique=True)
    description = Column(String(200), nullable=False)
    analysis_nature_id = Column(Integer, ForeignKey("analysis_natures.id"))

    def __repr__(self):
        return "<Principle name='%s'>" % (self.name.encode('utf-8'),)

    @classmethod
    def create_defaults(self):
        text = """
Child's best interest|Even where you are trying to tell people about harm to other children or another children's issue or promote children's rights you always need to respect the best interests of the individual child|2
Child's dignity|Always respect children's dignity and well being.|2
Privacy and confidentiality|When interviewing a child, respect their privacy and confidentiality and make sure you protect them from harm and potential consequences. |2
Children's voices|Children have a right to have their views heard on matters that affect them, so try and include them. |2
Interview relevant sources |When doing a story on children ask those who know or work with them, or are experts on the issue about the potential consequences of telling their story. |2
Children's Identity|Always hide a child's identity where the child might be at risk. |2
Legal proceedings|Children involved in legal proceedings need even more protection, and are at greater risk so make sure to always protect their identity. |2
Informed Consent|If you want to name or show a child, make sure you are allowed to do so by law, that you have informed consent from the child (and guardian) and that you still protect them from potential harm.|2
HIV status|Make sure to protect a child's HIV status. If in doubt leave it out.|2
Stereotypes on children |Challenge negative stereotypes about children and conventional roles children occupy in the media (e.g. helpless victims) whenever you can. |2
Gender-based stereotypes|Treat girls and boys the same in your stories, with equal care, dignity and respect. |2
Vulnerable children|When doing a story on a vulnerable child make sure to be extra careful.|2
Sexual portrayal|Do not show children in a sexual manner.|2
Bribing for stories|Do not make promises you cannot keep and don't try bribe children for your story.|2
        """

        principles = []
        for x in text.strip().split("\n"):
            p = Principle()

            parts = x.strip().split("|", 2)
            p.name = parts[0].strip()
            p.description = parts[1].strip()
            p.analysis_nature_id = int(parts[2])

            principles.append(p)

        return principles
