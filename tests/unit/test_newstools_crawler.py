# -*- coding: utf-8 -*-
import unittest

from mock import MagicMock

from dexter.models import Document
from dexter.models.support import db
from dexter.models.seeds import seed_db
from dexter.processing.crawlers import NewstoolsCrawler

class TestNewstoolsCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = NewstoolsCrawler()

        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_offer(self):
        self.assertEqual(self.crawler.offer('http://example.com'), False)
        self.assertEqual(self.crawler.offer('http://news24.com'), True)

    def test_crawl(self):
        item = {'url': 'http://mg.co.za/article/2014-05-22-dont-miss-this-eat-listen-watch', 'text_url': 'http://www.newstools.co.za/data/texts/SFM-9VNENUOQNCNT503VVLYE.txt', 'author': 'M&G Reporters', 'publishdate': '2014-05-23 00:00:00', 'title': "DON'T MISS THIS: Oliver 'Tuku' Mtukudzi, the DStv Delicious Festival and City Hall Sessions"}

        self.crawler.fetch_text = MagicMock(return_value='This is the text.')

        doc = self.crawler.crawl(item)

        self.assertEqual(item['url'], doc.url)
        self.assertEqual('M&G Reporters', doc.author.name)
        self.assertEqual('23 05 2014', doc.published_at.strftime('%d %m %Y'))
        self.assertEqual("DON'T MISS THIS: Oliver 'Tuku' Mtukudzi, the DStv Delicious Festival and City Hall Sessions", doc.title)
        self.assertEqual("This is the text.", doc.text)
        self.assertEqual('Mail and Guardian', doc.medium.name)

    def test_unescape(self):
        self.assertEqual(self.crawler.unescape('people &#x201C;who want him to be removed as the provincial commissioner&#x201D;.'),
                u"people “who want him to be removed as the provincial commissioner”.")
