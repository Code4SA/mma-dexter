from flask.ext.testing import TestCase
from flask.ext.fillin import FormWrapper

from dexter.core import app
from dexter.models.support import db
from dexter.models import Author
from dexter.models.seeds import seed_db

from tests.fixtures import dbfixture, DocumentData

class TestEditArticleAnalysis(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.db = db
        self.db.session.remove()
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

        self.fx = dbfixture.data(DocumentData)
        self.fx.setup()

        self.client.response_wrapper = FormWrapper

    def tearDown(self):
        self.fx.teardown()
        self.db.session.rollback()
        self.db.session.remove()
        self.db.drop_all()
  
    def test_edit_article_new_author(self):
        res = self.client.get('/articles/%s/analysis' % self.fx.DocumentData.simple.id)
        self.assert200(res)

        f = res.forms[0]
        f.fields['topic_id'] = ''

        res = f.submit(self.client)
        self.assertRedirects(res, '/articles/%s' % self.fx.DocumentData.simple.id)
