from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class DestinyConnectCrawler(BaseCrawler):
    DC_RE = re.compile('(www\.)?destinyconnect.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.DC_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(DestinyConnectCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('article.post .entry-header .entry-title'))

        #gather publish date
        date = self.extract_plaintext(soup.select('article.post .entry-header .entry-meta time.entry-date'))
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('article.post .entry-content > p')
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[:2])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author 
        author = self.extract_plaintext(soup.select('article.post .entry-header .entry-meta .byline .author'))
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()
