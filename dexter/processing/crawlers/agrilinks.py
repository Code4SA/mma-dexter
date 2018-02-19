from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class AgrilinksCrawler(BaseCrawler):
    A_RE = re.compile('agrilinks.org')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.A_RE.match(parts.netloc))

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
        super(AgrilinksCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('#content-main .node-post .field-name-title .page-header'))

        #gather publish date
        date = self.extract_plaintext(soup.select('#content-main .node-post .group-post-info .field-name-post-date .field-item'))
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('#content-main .node-post .field-name-body .field-item')
        child_list = []
        for child in nodes[0].descendants:
            if isinstance(child, basestring):
                child_list.append(child)
        doc.summary = " ".join(p.strip() for p in child_list[:3])
        doc.text = " ".join(p for p in child_list)

        # gather author 
        author = ''
        author_nodes = soup.select('#content-main .node-post .group-post-info .group-author-name a')
        if author_nodes:
            author = ''.join(a.text.strip() for a in author_nodes)
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()