import unittest
import datetime

from dexter.models import Document, Cluster, ClusteredDocument, db
from dexter.models.seeds import seed_db

class TestCluster(unittest.TestCase):
    def setUp(self):
        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_find_or_create(self):
        docs = [Document(url='foo-%s' % i) for i in xrange(3)]
        for d in docs:
            d.published_at = datetime.datetime.now()

        # get ids
        db.session.add_all(docs)
        db.session.flush()

        cluster = Cluster.find_or_create(docs=docs)
        self.assertEqual(cluster.fingerprint, '202cb962ac59075b964b07152d234b70')
        self.assertEqual(sorted(cluster.documents), sorted(docs))

        db.session.add(cluster)
        db.session.flush()

        cluster2 = Cluster.find_or_create(docs=docs)
        self.assertIsNotNone(cluster2.id)
        self.assertEqual(cluster.id, cluster2.id)

    def test_delete_cascades(self):
        docs = [Document(url='foo-%s' % i) for i in xrange(3)]
        for d in docs:
            d.published_at = datetime.datetime.now()

        # get ids
        db.session.add_all(docs)
        db.session.flush()

        cluster = Cluster.find_or_create(docs=docs)
        db.session.add(cluster)
        db.session.flush()

        deleted = docs[0]
        rest = docs[1:]

        db.session.delete(deleted)
        db.session.flush()
        db.session.commit()

        cluster = db.session.query(Cluster).filter(Cluster.id == cluster.id).one()
        self.assertEqual(sorted(rest), sorted(cluster.documents))
