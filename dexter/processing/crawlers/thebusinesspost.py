from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class TheBusinessPostCrawler(BaseCrawler):
    TBP_RE = re.compile('(www\.)?thebusinesspost.ng')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TBP_RE.match(parts.netloc))

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
        super(TheBusinessPostCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('.article-container article.story .media-heading'))

        nodes = soup.select('.article-container article.story p')
        

        #gather text and summary
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[3:4])
        doc.text = "\n\n".join(p.text.strip() for p in nodes[3:])

        byline = nodes[2].text
        
        # gather author
        author = byline[:byline.index(' | ')]
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()

        #gather publish date
        sub_byline = byline[byline.index(' | ') + 2:]
        date = sub_byline[:sub_byline.index(' | ')].strip()
        doc.published_at = self.parse_timestamp(date)