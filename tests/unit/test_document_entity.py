import unittest

from dexter.models import Document, DocumentEntity, Entity

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
