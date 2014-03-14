import unittest

from dexter.models import Document, Entity, Person, DocumentEntity, Utterance, Gender
from dexter.models.support import db
from dexter.models.seeds import seed_db
from dexter.processing.extractors import SourcesExtractor

from tests.fixtures import dbfixture, EntityData

class TestSourcesExtractor(unittest.TestCase):
    def setUp(self):
        self.ex = SourcesExtractor()

        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

        self.fx = dbfixture.data(EntityData)
        self.fx.setup()

    def tearDown(self):
        self.fx.teardown()
        self.db.session.rollback()
        self.db.session.remove()
        self.db.drop_all()

    def test_guess_genders(self):
        d = Document()
        d.text = 'Fred Astair did something. He also did something else.'

        de = DocumentEntity()
        de.document = d
        de.entity = Entity.query.get(self.fx.EntityData.sue_no_gender.id)
        de.offset_list = '27:2'

        self.db.session.add(d)

        de.entity.person.gender = Gender.male()

        self.ex.guess_genders(d)
        self.assertEqual('Male', d.entities[0].entity.person.gender.name)

    def test_extract_sources(self):
        d = Document()
        d.text = 'Fred Astair did something. He also did something else.'

        u = Utterance()
        u.entity = self.fx.EntityData.zuma
        u.document = d

        self.ex.extract_sources(d)
        self.assertEqual(['Jacob Zuma'], [s.person.name for s in d.sources])

