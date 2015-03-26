from flask.ext.testing import TestCase
from flask.ext.fillin import FormWrapper

from . import UserSessionTestCase
from dexter.models import Document, db

from tests.fixtures import dbfixture, DocumentData, UserData

class TestEditArticleAnalysis(UserSessionTestCase):
    def setUp(self):
        super(TestEditArticleAnalysis, self).setUp()

        self.fx = dbfixture.data(DocumentData, UserData)
        self.fx.setup()

        self.login()
  
    def test_edit_article_analysis(self):
        res = self.client.get('/articles/%s/analysis' % self.fx.DocumentData.simple.id)
        self.assert200(res)

        # check that no issues have been selected yet
        doc = Document.query.get(self.fx.DocumentData.simple.id)
        self.assertEqual(0, len(doc.issues))

        f = res.forms[1]

        # select an issue
        f.fields['issues'] = ['2', ]

        res = f.submit(self.client)
        self.assertRedirects(res, '/articles/%s/analysis' % self.fx.DocumentData.simple.id)

        # check that an issue has been selected
        doc = Document.query.get(self.fx.DocumentData.simple.id)
        self.assertEqual(1, len(doc.issues))
