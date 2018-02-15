from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class NigeriaTodayCrawler(BaseCrawler):
    NT_RE = re.compile('(www\.)?nigeriatoday.ng')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.NT_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(NigeriaTodayCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('.post h1.title'))

        #gather publish date
        meta_info = self.extract_plaintext(soup.select('.post .post-meta p'))
        date = meta_info[meta_info.index(' on') + 3:meta_info.index(' in')].strip()
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('.post > p')
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[:2])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author 
        doc.author = Author.unknown()