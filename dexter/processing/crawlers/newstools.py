import requests
from dateutils.parser import parse

from .base import BaseCrawler
from ...models import Author, AuthorType


class NewstoolsCrawler(BaseCrawler):
    def offer(self, url):
        """ Can this crawler process this URL? """

        return True

    def crawl(self, item):
        """ Crawl this newstools feed item and return a document. """
        doc = Document()
        doc.url = item['url']
        doc.title = item['title']
        doc.published_on = parse(item['publishdate'])

        if item['author'] and item['author'] != 'unknown':
            doc.author = Author.get_or_create(item['author'], AuthorType.journalist())

        doc.text = self.fetch_text(item['text_url'])

        # medium and country
        self.extract(doc, None)

        return doc

    def fetch_text(self, url):
        r = requests.get(url)
        r.raise_for_status()
        return r.text
