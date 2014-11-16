import unittest
import datetime

from dexter.models import Document, DocumentSource, Person, Affiliation, Entity

from dexter.models.support import db
from dexter.models.seeds import seed_db

from tests.fixtures import dbfixture, DocumentData, PersonData, EntityData

class TestDocument(unittest.TestCase):
    def setUp(self):
        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

        self.fx = dbfixture.data(PersonData, DocumentData, EntityData)
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


    def test_merge(self):
        # we're going to merge joe into zuma
        joe = Person.query.get(self.fx.PersonData.joe_author.id)
        zuma = Person.query.get(self.fx.PersonData.zuma.id)

        joe.merge_into(zuma)
        db.session.flush()

        author = Entity.query.get(self.fx.AuthorData.joe_author.id)
        self.assertEqual(author.person, zuma)

        entity = Entity.query.get(self.fx.EntityData.joe_author.id)
        self.assertEqual(entity.person, zuma)

        # should be deleted
        joe = Person.query.filter(Person.id == joe.id).first()
        self.assertIsNone(joe)

        # new entity should exist
        e = Entity.query.filter(Entity.group == 'person', Entity.name == self.fx.PersonData.joe_author.name).one()
        self.assertEqual(zuma, e.person)


    def test_merge_dedup_sources(self):
        # we're going to merge joe into zuma
        joe = Person.query.get(self.fx.PersonData.joe_author.id)
        zuma = Person.query.get(self.fx.PersonData.zuma.id)

        doc1 = Document.query.get(self.fx.DocumentData.simple.id)
        doc2 = Document.query.get(self.fx.DocumentData.simple2.id)

        # doc1 already has Zuma and Joe as sources, so we should only
        # wind up with Zuma at the end
        doc1.add_source(DocumentSource(person=zuma, source_type='person'))
        doc1.add_source(DocumentSource(person=joe, source_type='person'))

        # doc2 only has joe
        doc2.add_source(DocumentSource(person=joe, source_type='person'))

        db.session.flush()
        db.session.commit()

        joe.merge_into(zuma)
        db.session.flush()
        db.session.commit()

        doc1 = Document.query.get(self.fx.DocumentData.simple.id)
        doc2 = Document.query.get(self.fx.DocumentData.simple2.id)

        self.assertEqual([zuma], [ds.person for ds in doc1.sources])
        self.assertEqual([zuma], [ds.person for ds in doc2.sources])
