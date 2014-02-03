import unittest

from dexter.models import Document, DocumentEntity, Entity

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
