from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Medium, Author, AuthorType

class TimesLiveCrawler(BaseCrawler):
    TL_RE = re.compile('(www\.)?timeslive.co.za')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TL_RE.match(parts.netloc))

    def crawl(self, doc):
        """ Crawl this document. """
        raw_html = self.fetch(doc.url)
        self.extract(doc, raw_html)

    def fetch(self, url):
        url = url + '?service=print'

        self.log.info("Fetching URL: " + url)

        r = requests.get(url)
        # raise an HTTPError on badness
        r.raise_for_status()

        return r.text.encode('utf8')

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """

        doc.medium = Medium.query.filter(Medium.domain == 'timeslive.co.za').one()

        soup = BeautifulSoup(raw_html)

        doc.title = self.extract_plaintext(soup.select(".articleheader h1"))
        doc.summary = self.extract_plaintext(soup.select(".articleheader h3"))
        doc.text = "\n\n".join(p.text for p in soup.select(".column > p"))

        extra = self.extract_plaintext(soup.select(".articleheader div"))
        date, author = [s.strip() for s in extra.split("|", 1)]

        doc.published_at = self.parse_timestamp(date)

        if author:
            doc.author = Author.get_or_create(author, AuthorType.journalist())
        else:
            doc.author = Author.unknown()
