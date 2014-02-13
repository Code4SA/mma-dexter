import unittest

from dexter.models import Document, Entity, Person, DocumentEntity, Utterance
from dexter.models.support import db
from dexter.models.seeds import seed_db
from dexter.processing import DocumentProcessor

class TestDocumentEntity(unittest.TestCase):
    def setUp(self):
        self.dp = DocumentProcessor()
        self.db = db
        self.db.create_all()
        seed_db(db)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_discover_people(self):
        d = Document()
        d.text = 'Fred Astair did something. He also did something else.'
        d.author = Entity()
        d.author.name = 'Joe Bloggs'
        d.author.group = 'person'

        u = Utterance()
        u.entity = Entity()
        u.entity.group = 'person'
        u.entity.name = 'Fred Astair'
        u.document = d

        de = DocumentEntity()
        de.entity = u.entity
        de.document = d
        de.offset_list = '27:2'


        people = self.dp.discover_people(d)
        self.assertEqual(['Fred Astair', 'Joe Bloggs'], [p.name for p in people])

        self.assertEqual('Fred Astair', people[0].name)
        self.assertEqual('Male', people[0].gender.name)

        self.assertEqual(people[1], d.author.person)
        self.assertEqual(people[0], d.utterances[0].entity.person)


    def test_discover_people_existing(self):
        joe = Person()
        joe.name = 'Joe Bloggs'
        self.db.session.add(joe)
        self.db.session.flush()

        d = Document()
        d.text = 'Fred Astair did something. He also did something else.'
        d.author = Entity()
        d.author.name = 'Joe Bloggs'
        d.author.group = 'person'

        people = self.dp.discover_people(d)
        self.assertEqual([], [p.name for p in people])
