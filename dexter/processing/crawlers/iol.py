from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class IOLCrawler(BaseCrawler):
    TL_RE = re.compile('(www\.)?iol.co.za')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TL_RE.match(parts.netloc))

    def canonicalise_url(self, url):
        """ Strip anchors, etc. """
        url = super(IOLCrawler, self).canonicalise_url(url)
        parts = urlparse(url)

        # force http, www, remove trailing slash, anchors
        return urlunparse(['http', 'www.iol.co.za', parts.path.rstrip('/'), parts.params, None, None])

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(IOLCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        doc.title = self.extract_plaintext(soup.select(".article-white h1.article_headers"))
        doc.text = "\n\n".join(p.text for p in soup.select("#article_container p.arcticle_text"))

        parts = self.extract_plaintext(soup.select(".article-white p.byline")).split("By", 1)
        if len(parts) > 1:
            date, author = parts
        else:
            date = parts[0]
            author = None

        doc.published_at = self.parse_timestamp(date)

        if author:
            author = author.strip()
            doc.author = Author.get_or_create(author, AuthorType.journalist())
        else:
            doc.author = Author.unknown()
