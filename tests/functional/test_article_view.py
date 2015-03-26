import datetime

from mock import patch, MagicMock

from . import UserSessionTestCase
from dexter.core import app
from dexter.models import Document, DocumentFairness, db, Author, Medium, Country

from tests.fixtures import dbfixture, DocumentData, EntityData, UserData, AuthorData

class TestArticleView(UserSessionTestCase):
    def setUp(self):
        super(TestArticleView, self).setUp()

        self.fx = dbfixture.data(EntityData, DocumentData)
        self.fx.setup()

        self.login()

    def test_show_article_analysis(self):
        d = Document.query.get(self.fx.DocumentData.simple.id)

        df = DocumentFairness()
        df.document = d

        self.db.session.add(d)
        self.db.session.add(df)
        self.db.session.commit()

        res = self.client.get('/articles/%d' % d.id)
        self.assert200(res)
