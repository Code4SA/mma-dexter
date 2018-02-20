from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class SunNewsOnlineCrawler(BaseCrawler):
    SNO_RE = re.compile('sunnewsonline.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.SNO_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(SunNewsOnlineCrawler, self).extract(doc, raw_html)
        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('.post header h4.entry-title'))

        #gather publish date
        date = self.extract_plaintext(soup.select('.post header span.entry-date'))
        doc.published_at = self.parse_timestamp(date[1:].strip())

        #gather text and summary
        nodes = soup.select('.post .elements-box > p')
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[:2])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author 
        doc.author = Author.unknown()

