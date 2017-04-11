from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests
import logging

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class NewsDayZWCrawler(BaseCrawler):
    NDZW = re.compile('(www\.)?newsday.co.zw')
    log = logging.getLogger(__name__)

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.NDZW.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        # cleaning up the raw_html as is seems unicode 4byte characters are present which will error with DB
        raw_html = raw_html.encode("utf-8")
        raw_html = unicode(raw_html, errors='ignore')

        super(NewsDayZWCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select("#content #main article.post header h1"))

        #gather publish date
        date = self.extract_plaintext(soup.select("#content #main article.post .post-meta .date.published"))
        doc.published_at = self.parse_timestamp(date)
        
        #gather text and summary
        nodes = soup.select("#content #main article.post .entry p")
        if len(nodes) > 1:
            doc.summary = self.extract_plaintext(nodes[0:1])
        doc.text = "\n\n".join(p.text.strip() for p in nodes[2:])

        # gather author 
        author = self.extract_plaintext(nodes[1:2]).replace("BY ", "")
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()

