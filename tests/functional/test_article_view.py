import datetime

from mock import patch, MagicMock

from . import UserSessionTestCase
from dexter.core import app
from dexter.models import Document, DocumentFairness, db

from tests.fixtures import dbfixture, PersonData, EntityData, UserData

class TestArticleView(UserSessionTestCase):
    def setUp(self):
        super(TestArticleView, self).setUp()

        self.fx = dbfixture.data(EntityData, UserData)
        self.fx.setup()

        self.login()

    def test_show_article_analysis(self):
        d = Document()
        d.text = "text"
        d.published_at = datetime.datetime.utcnow()

        df = DocumentFairness()
        df.document = d

        self.db.session.add(d)
        self.db.session.add(df)
        self.db.session.commit()

        res = self.client.get('/articles/%d' % d.id)
        self.assert200(res)
