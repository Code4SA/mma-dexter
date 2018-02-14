from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class NationalDailyNgCrawler(BaseCrawler):
    NDN_RE = re.compile('(www\.)?nationaldailyng.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.NDN_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(NationalDailyNgCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('.td-main-content .td-post-header .td-post-title h1.entry-title'))

        #gather publish date
        date = self.extract_plaintext(soup.select('.td-main-content .td-post-header .td-post-title .td-post-date time'))
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('.td-main-content .td-post-content')
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[:1])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author 
        author = self.extract_plaintext(soup.select('.td-main-content .td-post-header .td-post-title .td-post-author-name a'))
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()
