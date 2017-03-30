from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests
import logging

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class BBCCrawler(BaseCrawler):
    BBC = re.compile('(www\.)?bbc.com')
    log = logging.getLogger(__name__)

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.BBC.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        # raw_html = raw_html.encode("utf-8")
        # raw_html = unicode(raw_html, errors='ignore')

        super(BBCCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select("#page .story-body .story-body__h1 "))

        #gather text and summary
        nodes = soup.select("#page .story-body .story-body__inner p")
        if len(nodes) > 1:
            doc.summary = self.extract_plaintext(nodes[:1])
        doc.text = "\n\n".join(p.text.strip() for p in nodes[1:])
        
        #gather publish date
        date = self.extract_plaintext(soup.select("#page .story-body .story-body__mini-info-list-and-share .date"))
        doc.published_at = self.parse_timestamp(date)

        # gather author 
        # no authors on pages
        doc.author = Author.unknown()

