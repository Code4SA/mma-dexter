from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class CNBCAfricaCrawler(BaseCrawler):
    CBNCA_RE = re.compile('(www\.)?cnbcafrica.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.CBNCA_RE.match(parts.netloc))

    def canonicalise_url(self, url):
        """ Strip anchors, etc."""

        # Needed to handle urls being recieved without protocol (http[s]://), check if it can be parsed first, then handle and re parse if there is no netloc found
        if '//' not in url:
            url = '%s%s' % ('https://', url)

        parts = urlparse(url)

        netloc = parts.netloc.strip(':80')

        # force http, strip trailing slash, anchors etc.
        return urlunparse(['https', netloc, parts.path.rstrip('/') or '/', parts.params, parts.query, None])

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(CNBCAfricaCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('article.post .td-post-header .td-post-title .entry-title'))

        #gather publish date
        date = self.extract_plaintext(soup.select('article.post .td-post-header .td-module-meta-info .td-post-date time.entry-date'))
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('article.post .td-post-content')
        text_list = []
        for node in nodes[0].children:
            if node.name in ['h3','h4','h5','p']:
                text_list = text_list + [node]
        doc.summary = "\n\n".join(p.text.strip() for p in text_list[:3])
        doc.text = "\n\n".join(p.text.strip() for p in text_list)


        # gather author 
        author = self.extract_plaintext(soup.select('article.post .td-post-header .td-module-meta-info .td-post-author-name a'))
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()
