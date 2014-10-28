from urlparse import urlparse, urlunparse
import HTMLParser
import requests
from dateutil.parser import parse

from .base import BaseCrawler
from ...models import Author, AuthorType, Medium, Document


class NewstoolsCrawler(BaseCrawler):
    def offer(self, url):
        """ Can this crawler process this URL?
        We only allow urls we have a medium for. """
        m = Medium.for_url(url)
        if m is None:
            return False

        parts = urlparse(url)

        # ignore citizen AFP articles
        if parts.path.startswith('/afp_feed_article'):
            return False

        # ignore citypress non-articles
        if m.domain == 'citypress.co.za':
          for prefix in ['/category/', '/author/', '/entertainment/', '/lifestyle/']:
              if parts.path.startswith(prefix):
                  return False

        # ignore IOL world articles
        if parts.path.startswith('/news/world/'):
            return False

        return True


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
        r = requests.get(url, verify=False, timeout=60)
        r.raise_for_status()
        return self.unescape(r.text)

    def unescape(self, text):
        html_parser = HTMLParser.HTMLParser()
        return html_parser.unescape(text)
