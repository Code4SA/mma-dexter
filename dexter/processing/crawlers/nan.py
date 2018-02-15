from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class NANCrawler(BaseCrawler):
    NAN_RE = re.compile('(www\.)?nan.ng')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.NAN_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(NANCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('.post .article-header .xt-post-title'))

        #gather publish date
        date = soup.select('.post article time')[0]['datetime']
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('.post .article-content .post-body p')
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[:2])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author 
        doc.author = Author.unknown()