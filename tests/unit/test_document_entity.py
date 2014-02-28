import unittest

from dexter.models import Document, DocumentEntity, Entity
from dexter.models.entity import sanitise_name
from dexter.models.support import db
from dexter.models.seeds import seed_db

class TestDocumentEntity(unittest.TestCase):
    def test_offsets_empty(self):
        de = DocumentEntity()
        self.assertEqual([], de.offsets())

    def test_offsets(self):
        de = DocumentEntity()
        de.offset_list = '  4:5  1:2 3:4   '
        self.assertEqual([(1,2), (3, 4), (4, 5)], de.offsets())

    def test_offsets_add_new(self):
        de = DocumentEntity()
        de.offset_list = '1:2 3:4'
        self.assertTrue(de.add_offset((4, 5)))
        self.assertEqual('1:2 3:4 4:5', de.offset_list)

    def test_offsets_add_exists(self):
        de = DocumentEntity()
        de.offset_list = '1:2 3:4'
        self.assertFalse(de.add_offset((3, 4)))
        self.assertEqual('1:2 3:4', de.offset_list)

class TestEntity(unittest.TestCase):
    def setUp(self):
        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_add_entity(self):
        self.assertEqual(Entity.get_or_create('person', 'Zuma'), Entity.get_or_create('person', 'Zuma]'))

    def test_sanitise_name(self):
        self.assertEqual('foo', sanitise_name('foo'))
        self.assertEqual('A.N.C', sanitise_name('A.N.C.'))
        self.assertEqual('Zuma', sanitise_name('Zuma,]'))
        self.assertEqual('Jacob Zuma', sanitise_name(u'Jacob\xa0Zuma'))
        self.assertEqual('Zuma', sanitise_name(u'Zuma -'))
