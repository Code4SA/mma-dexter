from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class StandardMediaKTNCrawler(BaseCrawler):
    BDO_RE = re.compile('(www\.)?standardmedia.co.ke/ktnnews')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        paths = parts.path.split('/')
        return bool(self.BDO_RE.match(parts.netloc + '/' + paths[1]))

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
        super(StandardMediaKTNCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('.container .card .card-block .card-title'))

        #gather publish date
        date = self.extract_plaintext(soup.select('.container .card .card-block .card-text'))
        doc.published_at = self.parse_timestamp(date[date.index('|') + 1:].strip())

        #gather text and summary
        nodes = soup.select('.container .card .card-block p')
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[:1])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author 
        author = self.extract_plaintext(soup.select('.container .card .card-text a'))
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()