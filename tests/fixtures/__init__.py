from fixture import DataSet, NamedDataStyle, SQLAlchemyFixture

from dexter.models import db, Person, Entity

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

dbfixture = SQLAlchemyFixture(
    env=globals(),
    style=NamedDataStyle(),
    engine=db.engine)
