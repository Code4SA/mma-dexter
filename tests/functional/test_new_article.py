from flask.ext.testing import TestCase
from flask.ext.fillin import FormWrapper

from mock import patch, MagicMock

from dexter.core import app
from dexter.models.support import db
from dexter.models.seeds import seed_db
from dexter.processing.crawlers import MGCrawler
from dexter.processing.extractors import AlchemyExtractor, CalaisExtractor

class TestNewArticle(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.db = db
        self.db.create_all()
        seed_db(db)
        self.client.response_wrapper = FormWrapper

        AlchemyExtractor.fetch_entities = MagicMock(return_value=[])
        AlchemyExtractor.fetch_keywords = MagicMock(return_value=[])
        CalaisExtractor.fetch_data = MagicMock(return_value={})

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()
  
    def test_new_article_path(self):
        res = self.client.get('/articles/new')
        self.assert200(res)

    def test_new_article_by_url(self):
        res = self.client.get('/articles/new')
        self.assert200(res)

        html = """
<div class="headline_printable">title</div>
<div class="blurb_printable">blurb</div>
<div class="body_printable"><p>body</p></div>
<div class="content_place_line">2013/12/22</div>
<div class="content_place_line_author">Joe Bloggs</div>
        """
        MGCrawler.fetch = MagicMock(return_value=html)

        f = res.forms[0]
        f.fields['url'] = 'http://mg.co.za/article/2013-12-22-foo'
        res = f.submit(self.client)

        self.assertRedirects(res, '/articles/1')

    def test_new_article(self):
        res = self.client.get('/articles/new')
        self.assert200(res)

        f = res.forms[1]
        f.fields['url'] = 'http://fake'
        f.fields['title'] = 'headline'
        f.fields['published_at'] = '2013/12/22'
        f.fields['text'] = 'the article text'
        f.fields['medium_id'] = '1'

        res = f.submit(self.client)
        self.assertRedirects(res, '/articles/1')
