from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class ThePointCrawler(BaseCrawler):
    TP_RE = re.compile('(www\.)?thepointng.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TP_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(ThePointCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('.td-main-content .td-post-header h1.entry-title'))

        #gather publish date
        date = self.extract_plaintext(soup.select('.td-main-content .td-post-header .td-post-date time.entry-date'))
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('.td-main-content .td-post-content p')
        if len(nodes) <= 1:
            doc.summary = ''.join(nodes[0].find('br').previous_siblings)
        else:
            doc.summary = "\n\n".join(p.text.strip() for p in nodes[:2])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author 
        author = self.extract_plaintext(soup.select('.td-main-content .td-post-header .td-post-author-name a'))
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()