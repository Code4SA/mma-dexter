from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class GlobalTimesCN(BaseCrawler):
    GTCN_RE = re.compile('(www\.)?globaltimes.cn')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.GTCN_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(GlobalTimesCN, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('#contents #left .article-title h3'))

        #gather publish date
        date = ''
        source_string = self.extract_plaintext(soup.select('#contents #left .article-source .text-left'))
        if 'Published:' in  source_string:
            date = source_string[source_string.index('Published:') + 10:].strip()
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('#contents #left .row-content')
        child_list = []
        for child in nodes[0].descendants:
            if isinstance(child, basestring):
                child_list.append(child)
        doc.summary = "\n".join(p for p in child_list[:1])
        doc.text = "\n".join(p for p in child_list)

        # gather author
        author = ''
        if 'By ' in source_string:
            author = source_string[source_string.index('By ') + 3:source_string.index('Source:')-1].strip()
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()