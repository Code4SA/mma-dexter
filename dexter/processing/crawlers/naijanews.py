from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class NaijaNewsCrawler(BaseCrawler):
    NNA_RE = re.compile('naijanewsagency.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.NNA_RE.match(parts.netloc))

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
        super(NaijaNewsCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('.main_container h1.post-tile'))

        #gather publish date
        #date_nodes = soup.select('.container .article_content .article_content_meta .article_content_date span')
        date = self.extract_plaintext(soup.select('.main_container .single-post-meta span time'))
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('.main_container .entry-content')
        text_list = []
        for node in nodes[0].children:
            if node.name in ['h2','h3','p']:
                text_list = text_list + [node]
        print '========================================================================='
        print "All this crap %s" % (text_list)
        print '========================================================================='
        doc.summary = "\n\n".join(p.text.strip() for p in text_list[:2])
        doc.text = "\n\n".join(p.text.strip() for p in text_list)

        # gather author 
        doc.author = Author.unknown()