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
    name        = Column(String(200), index=True, nullable=False, unique=True)
    analysis_nature_id = Column(Integer, ForeignKey("analysis_natures.id"))

    def __repr__(self):
        return "<Principle name='%s'>" % (self.name.encode('utf-8'),)

    @classmethod
    def create_defaults(self):
        text = """
The Story does/does not seek and express the truth|2
The Story is/is not independent and objective|2
The Story does/does not minimise harm |2
Children are afforded special protection|2
Avoid stereotypes|2
Children's interests are/are not taken into account|2
Child Abuse is a Human Rights Violation|2
Stories do/do not respect and engage with cultural and sexual practices as well as drug awareness |2
Be aware of the HIV/AIDS dimensions to child abuse stories|2
Be gender proactive and consider the gender angles to all stories |2
Even where you are trying to tell people about harm to children or about a children's issue or promote children's rights you always need to respect the best interest of the individual child.|2
Always respect children's dignity and well being.|2
When interviewing and reporting on a child, respect their privacy and confidentiality and make sure you protect them from harm and potential consequences. |2
Children have a right to have their views heard on matters that affect them, so try and include them. |2
When doing a story on children ask those who know or work with them, or are experts on the issue about the potential consequences of telling their story. |2
Always hide a child's identity where the child might be at risk. |2
Children involved in legal proceedings need even more protection, and are at greater risk so make sure to always protect their identity. |2
If you want to name or show a child, make sure you are allowed to do so by law, that you have informed consent from the child (and guardian) and that you still protect them from potential harm.|2
Make sure to protect a child's HIV status. If in doubt leave it out. |2
Challenge negative stereotypes about children and conventional roles children occupy in the media (e.g. helpless victims) whenever you can. |2
Treat girls and boys the same in your stories, with equal care, dignity and respect. |2
When doing a story on a vulnerable child make sure to be extra careful.|2
Do not show children in a sexual manner.|2
Do not make promises you cannot keep and don't bribe children for your story.|2
        """

        principles = []
        for x in text.strip().split("\n"):
            p = Principle()

            parts = x.strip().split("|", 1)
            p.name = parts[0]
            p.analysis_nature_id = int(parts[1])

            principles.append(p)

        return principles
