import unittest

from dexter.models import Document, db
from dexter.models.seeds import seed_db
from dexter.processing.extractors import AlchemyExtractor

class TestAlchemyExtractor(unittest.TestCase):
    def setUp(self):
        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

        AlchemyExtractor.API_KEY = 'fake'
        self.ex = AlchemyExtractor()
        self.doc = Document()
        self.doc.text = 'foo'

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_extract_entities(self):
        entities = [
            {
                "type": "Person",
                "relevance": "0.703385",
                "count": "4",
                "text": "Adam Welkom"
            },
            {
                "type": "Person",
                "relevance": "0.562693",
                "count": "4",
                "text": "Joyce Moamogwa",
                "quotations": [{
                    "quotation": "\"We are not safe, we do not trust them. They are like our enemies,\" she said ...",
                }]
            }]
        self.ex.extract_entities(self.doc, entities)

        e = self.doc.entities[0]
        self.assertEqual('Adam Welkom', e.entity.name)
        self.assertEqual('person', e.entity.group)
        self.assertEqual(4, e.count)
        self.assertEqual(0.703385, e.relevance)

        e = self.doc.entities[1]
        self.assertEqual('Joyce Moamogwa', e.entity.name)
        self.assertEqual('person', e.entity.group)
        self.assertEqual(4, e.count)
        self.assertEqual(0.562693, e.relevance)

    def test_extract_keywords(self):
        keywords = [
            {
                "relevance": "0.703385",
                "text": u"morning",
            },
            {
                "relevance": "0.562693",
                "text": u"justice",
            }]

        self.ex.extract_keywords(self.doc, keywords)

        kw = self.doc.keywords[0]
        self.assertEqual('morning', kw.keyword)
        self.assertEqual(0.703385, kw.relevance)

        kw = self.doc.keywords[1]
        self.assertEqual('justice', kw.keyword)
        self.assertEqual(0.562693, kw.relevance)

    def test_keyword_offsets(self):
        self.doc.text = 'Oh what a beautiful morning for mob justice. In the morning. With justice.'
        keywords = [
            {
                "relevance": "0.703385",
                "text": u"morning",
            },
            {
                "relevance": "0.562693",
                "text": u"justice",
            }]

        self.ex.extract_keywords(self.doc, keywords)

        k = self.doc.keywords[0]
        self.assertEqual('morning', k.keyword)
        self.assertEqual('20:7 52:7', k.offset_list)

        k = self.doc.keywords[1]
        self.assertEqual('justice', k.keyword)
        self.assertEqual('36:7 66:7', k.offset_list)

    def test_entity_offsets(self):
        self.doc.text = 'Foo Adam Welkom: "We are not safe," she said. Another Adam Welkom.'
        entities = [
            {
                "type": "Person",
                "relevance": "0.703385",
                "count": "4",
                "text": "Adam Welkom"
            },
            ]

        self.ex.extract_entities(self.doc, entities)

        e = self.doc.entities[0]
        self.assertEqual('Adam Welkom', e.entity.name)
        self.assertEqual('4:11 54:11', e.offset_list)

    def test_all_offsets(self):
        offsets = self.ex.all_offsets('foo bar baz bar bam', 'bar')
        self.assertEqual('4:3 12:3', offsets)

    def test_utterance_offsets(self):
        self.doc.text = 'Foo Adam Welkom: "We are not safe," she said. Another Adam Welkom.'
        entities = [
            {
                "type": "Person",
                "relevance": "0.562693",
                "count": "4",
                "text": "Joyce Moamogwa",
                "quotations": [{
                    "quotation": "\"We are not safe,\" she said ...",
                }]
            }]

        self.ex.extract_entities(self.doc, entities)

        u = self.doc.utterances[0]
        self.assertEqual(17, u.offset)
        self.assertEqual(27, u.length)
