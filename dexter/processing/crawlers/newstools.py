import requests
from dateutil.parser import parse

from .base import BaseCrawler
from ...models import Author, AuthorType, Medium, Document


class NewstoolsCrawler(BaseCrawler):
    def offer(self, url):
        """ Can this crawler process this URL?
        We only allow urls we have a medium for. """
        return Medium.for_url(url) is not None

    def crawl(self, item):
        """ Crawl this newstools feed item and return a document. """
        doc = Document()
        doc.url = item['url']
        doc.title = item['title']
        doc.published_at = parse(item['publishdate'])

        if item['author'] and item['author'].lower() != 'unknown':
            doc.author = Author.get_or_create(item['author'], AuthorType.journalist())
        else:
            doc.author = Author.unknown()

        doc.text = self.fetch_text(item['text_url'])

        # medium and country
        self.extract(doc, None)

        return doc

    def fetch_text(self, url):
        r = requests.get(url, verify=False)
        r.raise_for_status()
        return r.text
