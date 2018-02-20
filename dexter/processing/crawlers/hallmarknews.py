from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class HallmarkNewsCrawler(BaseCrawler):
    HN_RE = re.compile('hallmarknews.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.HN_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(HallmarkNewsCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('#content .post h1.posttitle'))

        #gather publish date
        meta_date = self.extract_plaintext(soup.select('#content #datemeta #datemeta_l'))
        date = meta_date[meta_date.index('Published On:') + 13:].strip()
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('#content .post .entry > p')
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[:2])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author 
        author_nodes = soup.select('#content #datemeta #datemeta_r a')
        author = author_nodes[-1].text
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()
