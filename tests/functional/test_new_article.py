from mock import patch, MagicMock

from . import UserSessionTestCase

from dexter.models import Author, db
from dexter.processing.crawlers import MGCrawler
from dexter.processing.extractors import AlchemyExtractor, CalaisExtractor

from tests.fixtures import dbfixture, PersonData, EntityData, UserData


class TestNewArticle(UserSessionTestCase):
    def setUp(self):
        super(TestNewArticle, self).setUp()

        self.fx = dbfixture.data(UserData, EntityData)
        self.fx.setup()

        self.login()

        AlchemyExtractor.fetch_entities = MagicMock(return_value=[])
        AlchemyExtractor.fetch_keywords = MagicMock(return_value=[])
        CalaisExtractor.fetch_data = MagicMock(return_value={})
  
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

        f = res.forms[1]
        f.fields['url'] = 'http://mg.co.za/article/2013-12-22-foo'
        res = f.submit(self.client)

        self.assertRedirects(res, '/articles/1/analysis')

    def test_new_article_existing_author(self):
        res = self.client.get('/articles/new')
        self.assert200(res)

        f = res.forms[2]
        f.fields['url'] = 'http://fake'
        f.fields['title'] = 'headline'
        f.fields['published_at'] = '2013/12/22 00:00'
        f.fields['text'] = 'the article text'
        f.fields['medium_id'] = '1'
        f.fields['document_type_id'] = '1'
        f.fields['country_id'] = '1'
        f.fields['author-name'] = str(self.fx.EntityData.joe_author.name)

        res = f.submit(self.client)
        self.assertRedirects(res, '/articles/1/analysis')

    def test_new_article_new_author(self):
        res = self.client.get('/articles/new')
        self.assert200(res)

        f = res.forms[2]
        f.fields['url'] = 'http://fake'
        f.fields['title'] = 'headline'
        f.fields['published_at'] = '2013/12/22 00:00'
        f.fields['text'] = 'the article text'
        f.fields['medium_id'] = '1'
        f.fields['document_type_id'] = '1'
        f.fields['country_id'] = '1'
        f.fields['author-name'] = 'Sue Skosana'
        f.fields['author-person_gender_id'] = '1'
        f.fields['author-person_race_id'] = '1'

        res = f.submit(self.client)
        self.assertRedirects(res, '/articles/1/analysis')

        sue = Author.query.filter(Author.name == 'Sue Skosana').one()
        self.assertEqual('Female', sue.person.gender.name)
        self.assertEqual('Black', sue.person.race.name)
