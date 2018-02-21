from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class BloombergCrawler(BaseCrawler):
    B_RE = re.compile('(www\.)?bloomberg.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.B_RE.match(parts.netloc))

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
        super(BloombergCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('article .lede-text-only .lede-text-only__content .lede-text-only__hed .lede-text-only__highlight'))

        #gather publish date
        date_node = soup.select('article .lede-text-only .lede-text-only__content time.article-timestamp')
        date = ''
        for node in date_node[0].children:
            if node.name == 'noscript':
                date = node.text.strip()
        doc.published_at = self.parse_timestamp(date)
        


        #gather text and summary
        summary_nodes = soup.select('article .content-well .abstract li')
        doc.summary = "\n\n".join(p.text.strip() for p in summary_nodes)

        nodes = soup.select('article .content-well .body-copy')
        text_list = []
        for node in nodes[0].children:
            if node.name in ['h3','p']:
                text_list = text_list + [node]
        doc.text = "\n\n".join(p.text.strip() for p in text_list)

        # gather author 
        author = []
        author_nodes = soup.select('article .lede-text-only .lede-text-only__content .author')
        for node in author_nodes:
            author += [node.find(text=True).strip()]
        if author:
            doc.author = Author.get_or_create(','.join(author), AuthorType.journalist())
        else:
            doc.author = Author.unknown()
