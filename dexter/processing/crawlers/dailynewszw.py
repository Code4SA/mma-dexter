from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests
import logging

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class DailyNewsZWCrawler(BaseCrawler):
    DNZW_RE = re.compile('(www\.)?dailynews.co.zw')
    log = logging.getLogger(__name__)

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.DNZW_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(DailyNewsZWCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select(".wrapper .content > h1"))

        #gather publish date
        date = self.extract_plaintext(soup.select(".wrapper .content .left #article .byline")).replace(u'\xa0', ' ').split(u'\u2022')[1]
        self.log.info(date)
        doc.published_at = self.parse_timestamp(date)
        
        #gather text and summary
        nodes = soup.select(".wrapper .content .left #article p")
        if len(nodes) > 1:
            doc.summary = self.extract_plaintext(nodes[1:2])
        doc.text = "\n\n".join(p.text.strip() for p in nodes[1:])

        # gather author 
        author = date = self.extract_plaintext(soup.select(".wrapper .content .left #article .byline")).replace(u'\xa0', ' ').split(u'\u2022')[0]
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()

