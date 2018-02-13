from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class NewTeleOnlineCrawler(BaseCrawler):
    NTO_RE = re.compile('newtelegraphonline.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.NTO_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(NewTeleOnlineCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('#mvp-main-body-wrap h1.mvp-post-title'))

        #gather publish date
        date = self.extract_plaintext(soup.select('#mvp-main-body-wrap .mvp-author-info-date span.mvp-post-date time.post-date'))
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('#mvp-main-body-wrap #mvp-content-main p')
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[:1])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author 
        author = self.extract_plaintext(soup.select('#mvp-main-body-wrap .mvp-author-info-wrap .author-name a'))
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()