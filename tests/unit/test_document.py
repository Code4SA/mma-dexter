import unittest
import datetime

from dexter.models import Document, DocumentEntity, Entity, Utterance, DocumentKeyword

from dexter.models.support import db
from dexter.models.seeds import seed_db

class TestDocument(unittest.TestCase):
    def setUp(self):
        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_add_keyword_no_dups(self):
        doc = Document()

        k = DocumentKeyword(keyword=u'foo')
        self.assertTrue(doc.add_keyword(k))

        self.assertTrue( doc.add_keyword(DocumentKeyword(keyword=u'gout')))
        # shouldn't work
        self.assertFalse(doc.add_keyword(DocumentKeyword(keyword=u'go\xfbt')))

    def test_add_entities_no_dups(self):
        doc = Document()

        e = Entity()
        e.group = 'group'
        e.name = u'name'

        de = DocumentEntity()
        de.entity = e
        de.relevance = 1.0
        de.count = 2

        doc.add_entity(de)
        self.assertEqual([de], list(doc.entities))


        e2 = Entity()
        e2.group = 'group'
        e2.name = u'name'

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
        u.entity.name = u'Fred'
        u.quote = u'Hello'

        self.assertTrue(doc.add_utterance(u))
        self.assertTrue(u in doc.utterances)

        # can't add twice
        self.assertFalse(doc.add_utterance(u))
        self.assertEqual(1, len(doc.utterances))

    def test_add_utterance_similar(self):
        doc = Document()
        doc.text = 'And Fred said "Hello there guys," to everyone.'
        
        u = Utterance()
        u.entity = Entity()
        u.entity.group = 'person'
        u.entity.name = u'Fred'
        u.quote = u'Hello there guys'

        self.assertTrue(doc.add_utterance(u))
        self.assertTrue(u in doc.utterances)

        # can't add similar quotations twice
        u2 = Utterance()
        u2.entity = Entity()
        u2.entity.group = 'person'
        u2.entity.name = u'Fred'
        u2.quote = u'\"Hello there guys,\" ...'

        self.assertFalse(doc.add_utterance(u2))
        self.assertEqual(1, len(doc.utterances))


    def test_add_utterance_update_offset(self):
        doc = Document()
        doc.text = u'And Fred said "Hello" to everyone.'
        
        u = Utterance()
        u.entity = Entity()
        u.entity.group = 'person'
        u.entity.name = u'Fred'
        u.quote = u'Hello'
        self.assertTrue(doc.add_utterance(u))

        u2 = Utterance()
        u2.entity = Entity()
        u2.entity.group = u'person'
        u2.entity.name = u'Fred'
        u2.quote = u'Hello'
        u2.offset = 10
        u2.length = 5

        self.assertTrue(doc.add_utterance(u2))
        self.assertEqual(10, u.offset)
        self.assertEqual(5, u.length)

        self.assertFalse(doc.add_utterance(u2))

    def test_delete_document(self):
        doc = Document()
        doc.text = u'And Fred said "Hello" to everyone.'
        doc.published_at = datetime.datetime.utcnow()
        
        u = Utterance()
        u.entity = Entity()
        u.entity.group = 'person'
        u.entity.name = u'Fred'
        u.quote = u'Hello'
        self.assertTrue(doc.add_utterance(u))

        de = DocumentEntity()
        de.document = doc
        de.entity = Entity.query.first()
        de.relevance = 0.5

        self.db.session.add(doc)
        self.db.session.commit()

        self.db.session.delete(doc)
        self.db.session.commit()
