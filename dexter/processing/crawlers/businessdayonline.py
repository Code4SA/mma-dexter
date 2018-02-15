from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class BusinessDayOnlineCrawler(BaseCrawler):
    BDO_RE = re.compile('(www\.)?businessdayonline.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.BDO_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(BusinessDayOnlineCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('.container article h1 a'))

        #gather publish date
        date = self.extract_plaintext(soup.select('.container article .date'))
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('.container article p')
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[:2])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author 
        author = self.extract_plaintext(soup.select('.container article .author a'))
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()