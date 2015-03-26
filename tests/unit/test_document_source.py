import unittest

from dexter.models import Document, DocumentSource, db
from dexter.models.seeds import seed_db

class TestDocumentSource(unittest.TestCase):
    def test_same_person(self):
        self.assertEqual(
            DocumentSource(
                source_type='person', unnamed=False, person_id=1, source_function_id=1,
                affiliation_id=1, quoted=1),
            DocumentSource(
                source_type='person', unnamed=False, person_id=1, source_function_id=1,
                affiliation_id=1, quoted=0))

    def test_same_person_unnamed(self):
        self.assertEqual(
            DocumentSource(
                source_type='person', unnamed=True, source_function_id=1, affiliation_id=1,
                quoted=1),
            DocumentSource(
                source_type='person', unnamed=True, source_function_id=1, affiliation_id=1,
                quoted=0))

    def test_diff_person_unnamed(self):
        self.assertNotEqual(
            DocumentSource(
                source_type='person', unnamed=True, source_function_id=1, affiliation_id=1),
            DocumentSource(
                source_type='person', unnamed=True, source_function_id=1, affiliation_id=2))

        self.assertNotEqual(
            DocumentSource(
                source_type='person', unnamed=True, source_function_id=1, affiliation_id=1),
            DocumentSource(
                source_type='person', unnamed=True, source_function_id=2, affiliation_id=1))

    def test_diff_person(self):
        self.assertNotEqual(
            DocumentSource(
                source_type='person', unnamed=False, person_id=1, source_function_id=1, affiliation_id=1),
            DocumentSource(
                source_type='person', unnamed=False, person_id=2, source_function_id=1, affiliation_id=2))

    def test_same_child(self):
        self.assertEqual(
            DocumentSource(
                source_type='child', unnamed=False, name='Foo', unnamed_race_id=1, unnamed_gender_id=1,
                source_age_id=1, source_role_id=1, quoted=0),
            DocumentSource(
                source_type='child', unnamed=False, name='Foo', unnamed_race_id=1, unnamed_gender_id=1,
                source_age_id=1, source_role_id=1, quoted=1))

    def test_same_child_unnamed(self):
        self.assertEqual(
            DocumentSource(
                source_type='child', unnamed=True, unnamed_race_id=1, unnamed_gender_id=1,
                source_age_id=1, source_role_id=1, quoted=0),
            DocumentSource(
                source_type='child', unnamed=True, unnamed_race_id=1, unnamed_gender_id=1,
                source_age_id=1, source_role_id=1, quoted=1))


    def test_diff_child_unnamed(self):
        self.assertNotEqual(
            DocumentSource(
                source_type='child', unnamed=True, unnamed_race_id=2, unnamed_gender_id=1,
                source_age_id=1, source_role_id=1, quoted=0),
            DocumentSource(
                source_type='child', unnamed=True, unnamed_race_id=1, unnamed_gender_id=1,
                source_age_id=1, source_role_id=1, quoted=0))


    def test_diff_child_named(self):
        self.assertNotEqual(
            DocumentSource(
                source_type='child', unnamed=False, name='Fred', unnamed_race_id=2, unnamed_gender_id=1,
                source_age_id=1, source_role_id=1, quoted=0),
            DocumentSource(
                source_type='child', unnamed=False, name='Fred', unnamed_race_id=1, unnamed_gender_id=1,
                source_age_id=1, source_role_id=1, quoted=0))

        self.assertNotEqual(
            DocumentSource(
                source_type='child', unnamed=False, name='Fred', unnamed_race_id=1, unnamed_gender_id=2,
                source_age_id=1, source_role_id=1, quoted=0),
            DocumentSource(
                source_type='child', unnamed=False, name='Fred', unnamed_race_id=1, unnamed_gender_id=1,
                source_age_id=1, source_role_id=1, quoted=0))

        self.assertNotEqual(
            DocumentSource(
                source_type='child', unnamed=False, name='Fred', unnamed_race_id=1, unnamed_gender_id=1,
                source_age_id=2, source_role_id=1, quoted=0),
            DocumentSource(
                source_type='child', unnamed=False, name='Fred', unnamed_race_id=1, unnamed_gender_id=1,
                source_age_id=1, source_role_id=1, quoted=0))

        self.assertNotEqual(
            DocumentSource(
                source_type='child', unnamed=False, name='Joe', unnamed_race_id=1, unnamed_gender_id=1,
                source_age_id=1, source_role_id=1, quoted=0),
            DocumentSource(
                source_type='child', unnamed=False, name='Ben', unnamed_race_id=1, unnamed_gender_id=1,
                source_age_id=1, source_role_id=1, quoted=0))

    def test_same_secondary(self):
        self.assertEqual(
            DocumentSource(
                source_type='secondary', unnamed=False, name='Source', source_function_id=1, affiliation_id=1),
            DocumentSource(
                source_type='secondary', unnamed=False, name='Source', source_function_id=1, affiliation_id=1))

    def test_diff_secondary(self):
        self.assertNotEqual(
            DocumentSource(
                source_type='secondary', unnamed=False, name='Source', source_function_id=1, affiliation_id=1),
            DocumentSource(
                source_type='secondary', unnamed=False, name='Source', source_function_id=2, affiliation_id=1))

        self.assertNotEqual(
            DocumentSource(
                source_type='secondary', unnamed=False, name='Source', source_function_id=1, affiliation_id=1),
            DocumentSource(
                source_type='secondary', unnamed=False, name='Source', source_function_id=1, affiliation_id=2))

        self.assertNotEqual(
            DocumentSource(
                source_type='secondary', unnamed=False, name='Blah  ', source_function_id=1, affiliation_id=1),
            DocumentSource(
                source_type='secondary', unnamed=False, name='Source', source_function_id=1, affiliation_id=1))
