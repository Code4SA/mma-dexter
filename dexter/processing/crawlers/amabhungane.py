from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class AmaBhunganeCrawler(BaseCrawler):
    AB_RE = re.compile('amabhungane.co.za')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.AB_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        raw_html = raw_html.encode("utf-8")
        raw_html = unicode(raw_html, errors='ignore')

        super(AmaBhunganeCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('.large-12 .orbit-caption h5'))

        #gather text and summary
        article_nodes = soup.select('.large-8 > .row')
        body_nodes = article_nodes[1].select('.large-12 > p')
        doc.summary = "\n\n".join(p.text.strip() for p in body_nodes[:2])
        doc.text = "\n\n".join(p.text.strip() for p in body_nodes)
        
        date_author = self.extract_plaintext(soup.select('.large-12 .orbit-caption time'))
        #gather publish date
        date = date_author[:date_author.index('-') - 1].strip()
        doc.published_at = self.parse_timestamp(date)

        # gather author 
        author = date_author[date_author.index('-') + 1:]
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()
