from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class ClassicFMCrawler(BaseCrawler):
    CFM_RE = re.compile('www.classic97.net')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.CFM_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(ClassicFMCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('#maincontent #page-title'))

        #gather publish date
        date = doc.url[-10:]
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('#maincontent .field-item p')
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[:1])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author 
        doc.author = Author.unknown()