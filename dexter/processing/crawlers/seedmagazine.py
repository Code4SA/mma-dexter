from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class SeedMagazineCrawler(BaseCrawler):
    SM_RE = re.compile('(www\.)?seedmagazine.co.ke')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.SM_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(SeedMagazineCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('.content-wrapper h1.page-title'))

        #gather publish date
        date = ''
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('.content-wrapper .page-content > p')
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
            author = self.extract_plaintext(soup.select('.content-wrapper .page-meta-wrapper .author a'))
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()