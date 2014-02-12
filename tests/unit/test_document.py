import unittest

from dexter.models import Document, DocumentEntity, Entity, Utterance

class TestDocument(unittest.TestCase):
    def test_add_entities_no_dups(self):
        doc = Document()

        e = Entity()
        e.group = 'group'
        e.name = 'name'

        de = DocumentEntity()
        de.entity = e
        de.relevance = 1.0
        de.count = 2

        doc.add_entity(de)
        self.assertEqual([de], list(doc.entities))


        e2 = Entity()
        e2.group = 'group'
        e2.name = 'name'

        de2 = DocumentEntity()
        de2.entity = e
        de2.relevance = 0.5
        de2.count = 3

        doc.add_entity(de2)
        # shouldn't add dup
        self.assertEqual([de], list(doc.entities))

    def test_add_utterance(self):
        doc = Document()
        doc.text = 'And Fred said "Hello" to everyone.'
        
        u = Utterance()
        u.entity = Entity()
        u.entity.group = 'person'
        u.entity.name = 'Fred'
        u.quote = 'Hello'

        self.assertTrue(doc.add_utterance(u))
        self.assertTrue(u in doc.utterances)

        # can't add twice
        self.assertFalse(doc.add_utterance(u))
        self.assertEqual(1, len(doc.utterances))


    def test_add_utterance_update_offset(self):
        doc = Document()
        doc.text = 'And Fred said "Hello" to everyone.'
        
        u = Utterance()
        u.entity = Entity()
        u.entity.group = 'person'
        u.entity.name = 'Fred'
        u.quote = 'Hello'
        self.assertTrue(doc.add_utterance(u))

        u2 = Utterance()
        u2.entity = Entity()
        u2.entity.group = 'person'
        u2.entity.name = 'Fred'
        u2.quote = 'Hello'
        u2.offset = 10
        u2.length = 5

        self.assertTrue(doc.add_utterance(u2))
        self.assertEqual(10, u.offset)
        self.assertEqual(5, u.length)

        self.assertFalse(doc.add_utterance(u2))
