from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class PlanIntlCrawler(BaseCrawler):
    PI_RE = re.compile('plan-international.org')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.PI_RE.match(parts.netloc))

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
        super(PlanIntlCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('#main-content .header-breadcrumb .page-title'))

        #gather publish date
        date = self.extract_plaintext(soup.select('#main-content .content-middle .date-display-single'))
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('#main-content .core-content')
        text_list = []
        doc.summary = ''
        for node in nodes:
            for child in node.descendants:
                if child.name in ['h3','p','li']:
                    text_list = text_list + [child]
                if len(doc.summary) < 200:
                    doc.summary = "\n\n".join(p.text.strip() for p in text_list).strip()
            doc.text = "\n\n".join(p.text.strip() for p in text_list).strip()

        # gather author
        author_type_A = self.extract_plaintext(soup.select('#main-content .content-middle .article-meta .field-guest-authors .field-guest-author'))
        author_type_B = self.extract_plaintext(soup.select('#main-content .content-middle .author-bio h2'))
        author = author_type_A + author_type_B
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()