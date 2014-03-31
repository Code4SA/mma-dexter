import datetime

from flask.ext.testing import TestCase
from flask.ext.fillin import FormWrapper

from mock import patch, MagicMock

from dexter.core import app
from dexter.models.support import db
from dexter.models import Document, DocumentFairness
from dexter.models.seeds import seed_db

from tests.fixtures import dbfixture, PersonData, EntityData

class TestArticleView(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.db = db
        self.db.session.remove()
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

        self.fx = dbfixture.data(EntityData)
        self.fx.setup()

        self.client.response_wrapper = FormWrapper

    def tearDown(self):
        self.fx.teardown()
        self.db.session.rollback()
        self.db.session.remove()
        self.db.drop_all()
  
    def test_show_article_analysis(self):
        d = Document()
        d.text = "text"
        d.published_at = datetime.datetime.utcnow()

        df = DocumentFairness()
        df.document = d

        self.db.session.add(d)
        self.db.session.add(df)
        self.db.session.commit()

        df.fairness_id = None
        self.db.session.commit()

        res = self.client.get('/articles/%d' % d.id)
        print res.data
        self.assert200(res)
