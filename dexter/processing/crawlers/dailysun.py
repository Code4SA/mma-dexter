from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Medium, Author, AuthorType

class DailysunCrawler(BaseCrawler):
    TL_RE = re.compile('(www\.)?dailysun.mobi')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TL_RE.match(parts.netloc))

    def canonicalise_url(self, url):
        """ Strip anchors, etc. """
        parts = urlparse(url)

        # force http, strip www, strip trailing slash
        return urlunparse(['http', 'dailysun.mobi', parts.path.rstrip('/'), parts.params, parts.query, None])

    def crawl(self, doc):
        """ Crawl this document. """
        raw_html = self.fetch(doc.url)
        self.extract(doc, raw_html)

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """

        doc.medium = Medium.query.filter(Medium.domain == 'dailysun.mobi').one()

        soup = BeautifulSoup(raw_html)

        doc.title = self.extract_plaintext(soup.select("h2.sub-heading"))
        doc.summary = self.extract_plaintext(soup.select(".article-excerpt"))
        doc.text = "\n\n".join(p.text for p in soup.select(".article-fullview > p") if not 'class' in p.attrs)

        date = self.extract_plaintext(soup.select(".publish-date")).replace('Published:', '')
        doc.published_at = self.parse_timestamp(date)

        author = self.extract_plaintext(soup.select("p.meta")).split(":", 2)
        if len(author) >= 2:
            author = author[1]
        else:
            author = author[0]

        if author:
            doc.author = Author.get_or_create(author.rstrip('Photo').strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()
