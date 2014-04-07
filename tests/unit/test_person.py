import unittest
import datetime

from dexter.models import Document, DocumentSource, Person, Affiliation

from dexter.models.support import db
from dexter.models.seeds import seed_db

from tests.fixtures import dbfixture, DocumentData, PersonData

class TestDocument(unittest.TestCase):
    def setUp(self):
        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

        self.fx = dbfixture.data(PersonData, DocumentData)
        self.fx.setup()

    def tearDown(self):
        self.fx.teardown()
        self.db.session.rollback()
        self.db.session.remove()
        self.db.drop_all()

    def test_relearn_affiliation_changes_none_set(self):

        zuma = Person.query.get(self.fx.PersonData.zuma.id)
        self.assertIsNone(zuma.affiliation)

        # shouldn't do anything
        self.assertFalse(zuma.relearn_affiliation())

        # add an ANC source
        doc = Document.query.get(self.fx.DocumentData.simple.id)
        doc.published_at = datetime.datetime.utcnow()

        ds = DocumentSource()
        ds.document = doc
        ds.person = zuma
        anc = Affiliation.query.filter(Affiliation.code == '4.3').one()
        ds.affiliation = anc

        self.db.session.add(ds)
        self.db.session.flush()

        self.assertTrue(zuma.relearn_affiliation())
        self.assertEqual(anc, zuma.affiliation)


    def test_relearn_affiliation_remains_same(self):
        zuma = Person.query.get(self.fx.PersonData.zuma.id)
        self.assertIsNone(zuma.affiliation)

        # set to ANC
        anc = Affiliation.query.filter(Affiliation.code == '4.3').one()
        zuma.affiliation = anc

        # shouldn't do anything
        self.assertFalse(zuma.relearn_affiliation())

        # add an ANC source from today
        doc1 = Document.query.get(self.fx.DocumentData.simple.id)
        doc1.published_at = datetime.datetime.utcnow()
        ds = DocumentSource()
        ds.document = doc1
        ds.person = zuma
        ds.affiliation = anc

        # add a DA source from a while ago
        doc2 = Document.query.get(self.fx.DocumentData.simple.id)
        doc2.published_at = datetime.datetime.utcnow() - datetime.timedelta(days=3)
        ds = DocumentSource()
        ds.document = doc2
        ds.person = zuma
        ds.affiliation = Affiliation.query.filter(Affiliation.code == '4.8').one()

        self.db.session.add(ds)
        self.db.session.flush()

        self.assertFalse(zuma.relearn_affiliation())
        self.assertEqual(anc, zuma.affiliation)
