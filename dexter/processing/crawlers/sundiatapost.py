from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

from datetime import datetime, timedelta
from dateutil.parser import parse

class SundiataPostCrawler(BaseCrawler):
    SP_RE = re.compile('sundiatapost.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.SP_RE.match(parts.netloc))

    def canonicalise_url(self, url):
        """ Strip anchors, etc."""

        # Needed to handle urls being recieved without protocol (http[s]://), check if it can be parsed first, then handle and re parse if there is no netloc found
        if '//' not in url:
            url = '%s%s' % ('https://', url)

        parts = urlparse(url)

        netloc = parts.netloc.strip(':80')

        # force http, strip trailing slash, anchors etc.
        return urlunparse(['https', netloc, parts.path.rstrip('/') or '/', parts.params, parts.query, None])

    def parse_timestamp(self, ts):
        if 'hour' in ts:
            return datetime.now() - timedelta(hours = int(ts[:ts.index('hour') -1].strip()))
        elif 'day' in ts:
            return datetime.now() - timedelta(days = int(ts[:ts.index('day') -1].strip()))
        elif 'week' in ts:
            return datetime.now() - timedelta(weeks = int(ts[:ts.index('week') -1].strip()))
        else:
            return parse(ts)

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(SundiataPostCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('#main-content .post .post-inner .post-title'))

        #gather publish date
        date = self.extract_plaintext(soup.select('#main-content .post .post-inner .post-meta .tie-date'))
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('#main-content .post .post-inner .entry p')
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[:2])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author
        author = ''
        entry_author = nodes[0].text
        if 'By ' in entry_author:
            if '\n' in entry_author:
                author = entry_author[entry_author.index('By ') + 3:entry_author.index('\n')].strip()
            else: 
                author = entry_author[entry_author.index('By ') + 3:].strip()
        else:
            author = self.extract_plaintext(soup.select('#main-content .post .post-inner .post-meta .post-meta-author a'))
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()

