from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
    )
from sqlalchemy.orm import relationship

from .support import db

class Author(db.Model):
    """
    A document author, which may be a single person (in which case it's linked to a Person),
    or it may be an agency.
    """
    __tablename__ = "authors"

    id          = Column(Integer, primary_key=True)
    name        = Column(String(50), index=True, nullable=False, unique=True)
    author_type_id = Column(Integer, ForeignKey('author_types.id'), nullable=False)
    person_id   = Column(Integer, ForeignKey('people.id'))

    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # Associations
    author_type = relationship("AuthorType", lazy=False)
    person      = relationship("Person", lazy=False)

    def json(self):
        return {
            'id': self.id,
            'name': self.person.name if self.person else self.name,
            'author_type': self.author_type.name,
        }


    def __repr__(self):
        return "<Author id=%s, type=%s, name=\"%s\", person=%s>" % (self.id, self.author_type, self.person, self.name.encode('utf-8'))


    @classmethod
    def get_or_create(cls, name, author_type):
        """ Get the author with this name or create it if it doesn't exist. """
        a = Author.query.filter(Author.name == name).first()
        if not a:
            a = Author()
            a.name = name
            a.author_type = author_type
            db.session.add(a)
            # force a db write (within the transaction) so subsequent lookups
            # find this entity
            db.session.flush()
        return a


class AuthorType(db.Model):
    """
    What type of author this is.
    """
    __tablename__ = "author_types"

    id        = Column(Integer, primary_key=True)
    name      = Column(String(150), index=True, nullable=False, unique=True)

    def __repr__(self):
        return "<AuthorType name='%s'>" % (self.name)

    @classmethod
    def journalist(cls):
        return AuthorType.query.filter(AuthorType.name == 'Journalist').one()

    @classmethod
    def create_defaults(cls):
        text = """
        Journalist
        Agency
        Guest Writer
        Many Journalists
        Journalist and Agency
        Unknown
        """
        types = []
        for s in text.strip().split("\n"):
            t = AuthorType()
            t.name = s.strip()
            types.append(t)

        return types
