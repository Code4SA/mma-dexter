from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests
import logging

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class ChronicleZWCrawler(BaseCrawler):
    CZW = re.compile('(www\.)?chronicle.co.zw')
    log = logging.getLogger(__name__)

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.CZW.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        # raw_html = raw_html.encode("utf-8")
        # raw_html = unicode(raw_html, errors='ignore')

        super(ChronicleZWCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select("#primary #content .post .entry-header .entry-title"))

        #gather text and summary
        nodes = soup.select("#primary #content .post .entry-content p")
        if len(nodes) > 1:
            doc.summary = self.extract_plaintext(nodes[:1])
        doc.text = "\n\n".join(p.text.strip() for p in nodes[1:])
        
        #gather publish date
        date = self.extract_plaintext(soup.select("#primary #content .post .entry-header .entry-meta .date"))
        doc.published_at = self.parse_timestamp(date)

        # gather author 
        author = self.extract_plaintext(soup.select("#primary #content .post .entry-header .entry-meta .author")).strip()
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()

