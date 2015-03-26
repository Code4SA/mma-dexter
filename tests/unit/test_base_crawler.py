import unittest

from dexter.models import Document, db
from dexter.models.seeds import seed_db
from dexter.processing.crawlers.base import BaseCrawler

class TestBaseCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = BaseCrawler()

        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_mediums(self):
        doc = Document()

        doc.url = 'http://www.iol.co.za/isolezwe/ezikamalema-zethule-abazo-ekzn-1.1667768#.Uzk8La2SxWu'
        self.assertEquals(self.crawler.identify_medium(doc).name, 'Isolezwe')

        doc.url = 'http://www.iol.co.za/news/politics/nkandla-job-not-finished-madonsela-1.1669787#.UzvP7K2SxWs'
        self.assertEquals(self.crawler.identify_medium(doc).name, 'IOL')

        doc.url = 'http://www.iol.co.za/news/politics/nkandla-job-not-finished-madonsela-1.1669787#.UzvP7K2SxWs'
        self.assertEquals(self.crawler.identify_medium(doc).name, 'IOL')
