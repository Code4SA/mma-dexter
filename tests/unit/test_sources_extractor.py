import unittest

from dexter.models import Document, Entity, DocumentEntity, Utterance, db
from dexter.models.seeds import seed_db
from dexter.processing.extractors import SourcesExtractor

from tests.fixtures import dbfixture, EntityData, DocumentData


class TestSourcesExtractor(unittest.TestCase):
    def setUp(self):
        self.ex = SourcesExtractor()

        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

        self.fx = dbfixture.data(DocumentData, EntityData)
        self.fx.setup()

    def tearDown(self):
        self.db.session.rollback()
        self.fx.teardown()
        self.db.session.remove()
        self.db.drop_all()

    def test_guess_genders(self):
        d = Document.query.get(self.fx.DocumentData.simple.id)
        d.text = 'Fred Astair did something. He also did something else.'

        de = DocumentEntity()
        de.document = d
        de.relevance = 1.0
        de.entity = Entity.query.get(self.fx.EntityData.sue_no_gender.id)
        de.offset_list = '27:2'

        self.db.session.add(d)

        self.ex.guess_genders(d)
        self.assertEqual('Male', d.entities[0].entity.person.gender.name)

    def test_extract_sources(self):
        d = Document.query.get(self.fx.DocumentData.simple.id)
        d.text = 'Fred Astair did something. He also did something else.'

        u = Utterance()
        u.entity = Entity.query.get(self.fx.EntityData.zuma.id)
        u.document = d
        u.quote = 'a quote'

        self.ex.extract_sources(d)
        self.assertEqual(['Jacob Zuma'], [s.person.name for s in d.sources])

    def test_match_people(self):
        d = Document.query.get(self.fx.DocumentData.simple.id)
        d.text = 'Fred Astair did something. He also did something else.'

        u = Utterance()
        u.entity = Entity()
        u.entity.group = 'people'
        u.entity.name = 'Jacob Zume'  # will fix to zuma
        u.quote = 'a quote'
        u.document = d

        u2 = Utterance()
        u2.entity = Entity()
        u2.entity.group = 'people'
        u2.entity.name = 'Jacob Zooma'  # too different
        u2.quote = 'a quote'
        u2.document = d

        self.ex.discover_people(d)
        self.assertEqual('Jacob Zuma', u.entity.person.name)
        self.assertIsNone(u2.entity.person)

    def test_clean_name(self):
        self.assertEqual('Cyril Ramaphosa', self.ex.clean_name('Deputy President Cyril Ramaphosa'))
        self.assertEqual('Nelson Mandela', self.ex.clean_name('President Nelson Mandela'))
        self.assertEqual('NelsonPresident Mandela', self.ex.clean_name('NelsonPresident Mandela'))
        self.assertEqual('Moegoeng Moegoeng', self.ex.clean_name('Chief Justice Moegoeng Moegoeng'))
        self.assertEqual('Alexis Tsipras', self.ex.clean_name('Prime Minister Alexis Tsipras'))
