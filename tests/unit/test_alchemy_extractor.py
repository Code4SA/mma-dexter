import unittest

from dexter.models import Document
from dexter.processing.extractors import AlchemyExtractor

class TestAlchemyExtractor(unittest.TestCase):
    def setUp(self):
        self.ex = AlchemyExtractor()
        self.doc = Document()

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

        self.ex.fetch_entities = lambda t: entities
        self.ex.extract_entities(self.doc)

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
                "text": "morning",
            },
            {
                "relevance": "0.562693",
                "text": "justice",
            }]

        self.ex.fetch_keywords = lambda t: keywords
        self.ex.extract_keywords(self.doc)

        kw = self.doc.keywords[0]
        self.assertEqual('morning', kw.keyword)
        self.assertEqual(0.703385, kw.relevance)

        kw = self.doc.keywords[1]
        self.assertEqual('justice', kw.keyword)
        self.assertEqual(0.562693, kw.relevance)
