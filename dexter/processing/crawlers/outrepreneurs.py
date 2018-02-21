from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class OutrepreneursCrawler(BaseCrawler):
    O_RE = re.compile('outrepreneurs.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.O_RE.match(parts.netloc))

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
        super(OutrepreneursCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('.block-content .single-post-box .title-post h1'))

        byline = soup.select('.block-content .single-post-box .title-post .post-tags li')
        
        #gather publish date
        date = byline[0].text.strip()
        doc.published_at = self.parse_timestamp(date)

        # gather author 
        author = self.extract_plaintext(byline[1].select('a'))
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()

        #gather text and summary
        nodes = soup.select('.block-content .single-post-box .the-content > p')
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[:1])
        doc.text = "\n\n".join(p.text.strip() for p in nodes[:-1])

