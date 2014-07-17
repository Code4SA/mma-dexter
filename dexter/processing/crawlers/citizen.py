from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class CitizenCrawler(BaseCrawler):
    TL_RE = re.compile('(www\.)?citizen.co.za')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TL_RE.match(parts.netloc))

    def canonicalise_url(self, url):
        """ Strip anchors, etc. """
        parts = urlparse(url)

        # force http, strip www, enforce trailing slash
        path = parts.path
        if not path.endswith('/'):
            path = path + '/'

        return urlunparse(['http', 'citizen.co.za', path, parts.params, parts.query, None])

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(CitizenCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        doc.title = self.extract_plaintext(soup.select("h1.article-headline"))
        doc.summary = self.extract_plaintext(soup.select(".article-excerpt"))
        doc.text = doc.summary + "\n\n" + "\n\n".join(p.text for p in soup.select(".article-content > p"))
        doc.published_at = self.parse_timestamp(self.extract_plaintext(soup.select(".page-lead-datetime")))

        author = self.extract_plaintext(soup.select(".article-byline"))

        if author:
            doc.author = Author.get_or_create(author, AuthorType.journalist())
        else:
            doc.author = Author.unknown()
