import datetime

from fixture import DataSet, NamedDataStyle, SQLAlchemyFixture

from dexter.models import db, Person, Entity, Author, Document

class PersonData(DataSet):
    class joe_author:
        name = 'Joe Author'
        gender_id = 2
        race_id = 1

class EntityData(DataSet):
    class joe_author:
        name = 'Joe Author'
        group = 'person'
        person = PersonData.joe_author

class AuthorData(DataSet):
    class joe_author:
        name = 'Joe Author'
        author_type_id = 1
        person = PersonData.joe_author

class DocumentData(DataSet):
    class simple:
        url = 'http://mg.co.za/articles/2012-01-01-foo'
        title = 'Title'
        summary = 'A document summary'
        text = 'Today, we do fun things.'
        published_at = datetime.datetime(2012, 1, 1)
        medium_id = 1
        document_type_id = 1
        author = AuthorData.joe_author


dbfixture = SQLAlchemyFixture(
    env=globals(),
    style=NamedDataStyle(),
    engine=db.engine)
