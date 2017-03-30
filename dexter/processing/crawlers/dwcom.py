from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests
import logging

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class DWCrawler(BaseCrawler):
    DW = re.compile('(www\.)?dw.com')
    log = logging.getLogger(__name__)

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.DW.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        raw_html = raw_html.encode("utf-8")
        raw_html = unicode(raw_html, errors='ignore')

        super(DWCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select("#innerFrame #bodyContent .col3 > h1"))

        #gather text and summary
        doc.summary = self.extract_plaintext(soup.select("#innerFrame #bodyContent .col3 .intro"))

        nodes = soup.select("#innerFrame #bodyContent .col3 .group .longText p")
        doc.text = "\n\n".join(p.text.strip() for p in nodes)
        
        #gather publish date
        list_data = soup.select("#innerFrame #bodyContent .col3 > .group > .smallList > li")
        for node in list_data:
            # find Date
            if node.text.find("Date") > -1:
                date = node.text.replace("Date", "")
            # find Author
            if node.text.find("Author") > -1:
                author = node.text.replace("Author", "")

        doc.published_at = self.parse_timestamp(date)

        # gather author 
        author = author.strip()
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()

