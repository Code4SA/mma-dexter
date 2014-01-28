import unittest

from dexter.processing.crawlers import MGCrawler

class TestMGCrawler(unittest.TestCase):
    def setUp(self):
        self.mg = MGCrawler()

    def test_canonicalise_url(self):
        self.assertEqual(self.mg.canonicalise_url(
            'https://www.mg.co.za/article/foo/#bar'),
            'http://mg.co.za/article/foo')
