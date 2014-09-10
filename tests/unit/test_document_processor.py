import unittest

import xml.etree.ElementTree as ET

from mock import MagicMock

from datetime import date

from dexter.models import Document
from dexter.models.support import db
from dexter.models.seeds import seed_db
from dexter.processing import DocumentProcessor
from dexter.processing.extractors import AlchemyExtractor

class TestDocumentProcessor(unittest.TestCase):
    def setUp(self):
        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

        AlchemyExtractor.API_KEY = 'fake'
        self.dp = DocumentProcessor()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_fetch_daily_feed_items(self):
        xml = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:sy="http://purl.org/rss/1.0/modules/syndication/" xmlns:admin="http://webns.net/mvcb/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:content="http://purl.org/rss/1.0/modules/content/">
<channel>
    <title>Dexter Articles</title>
    <link>http://www.newstools.co.za/dexter/articles/</link>
    <description>crawled articles for dexter</description>
    <dc:language>en-en</dc:language>
    <dc:creator>support@newstools.co.za</dc:creator>
    <dc:rights>All content Copyright original authors or copyright owners</dc:rights>
    <admin:generatorAgent rdf:resource="http://www.newstools.co.za/" />
    <item>
        <url>http://mg.co.za/article/2014&#45;05&#45;22&#45;kitchen&#45;cabinet&#45;helps&#45;jz&#45;to&#45;rule</url>
        <publisher>MG</publisher>
        <contenttype>news</contenttype>
        <contenttypeverified>false</contenttypeverified>
        <publishdate>2014-05-23 00:00:00</publishdate>
        <crawldate>2014-05-23 00:03:03</crawldate>
        <title>&apos;Kitchen cabinet&apos; helps Jacob Zuma rule</title>
        <author>Political Team</author>
        <text>http://www.newstools.co.za/data/texts/SFM-5TC9PUI3J6XGJC4Q7WAR.txt</text>
    </item>
    <item>
        <url>http://mg.co.za/article/2014&#45;05&#45;22&#45;dont&#45;miss&#45;this&#45;eat&#45;listen&#45;watch</url>
        <publisher>MG</publisher>
        <contenttype>news</contenttype>
        <contenttypeverified>false</contenttypeverified>
        <publishdate>2014-05-23 00:00:00</publishdate>
        <crawldate>2014-05-23 00:03:05</crawldate>
        <title>DON&apos;T MISS THIS: Oliver &apos;Tuku&apos; Mtukudzi, the DStv Delicious Festival and City Hall Sessions</title>
        <author>M&amp;G Reporters</author>
        <text>http://www.newstools.co.za/data/texts/SFM-9VNENUOQNCNT503VVLYE.txt</text>
    </item>
</channel>
</rss>
"""

        et = ET.fromstring(xml)
        today = date.today()

        self.dp.fetch_daily_feeds = MagicMock(return_value=et)
        items = list(self.dp.fetch_daily_feed_items(today))

        self.assertEqual(items, [
            {'url': 'http://mg.co.za/article/2014-05-22-kitchen-cabinet-helps-jz-to-rule', 'text_url': 'http://www.newstools.co.za/data/texts/SFM-5TC9PUI3J6XGJC4Q7WAR.txt', 'author': 'Political Team', 'publishdate': '2014-05-23 00:00:00', 'title': "'Kitchen cabinet' helps Jacob Zuma rule"},
            {'url': 'http://mg.co.za/article/2014-05-22-dont-miss-this-eat-listen-watch', 'text_url': 'http://www.newstools.co.za/data/texts/SFM-9VNENUOQNCNT503VVLYE.txt', 'author': 'M&G Reporters', 'publishdate': '2014-05-23 00:00:00', 'title': "DON'T MISS THIS: Oliver 'Tuku' Mtukudzi, the DStv Delicious Festival and City Hall Sessions"},
            ])
