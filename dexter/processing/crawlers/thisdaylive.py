from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class ThisDayLiveCrawler(BaseCrawler):
    TDL_RE = re.compile('(www\.)?thisdaylive.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TDL_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(ThisDayLiveCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('.post .td-post-header .td-post-title .entry-title'))

        #gather publish date
        date = self.extract_plaintext(soup.select('.post .td-post-header .td-post-title time.entry-date'))
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('.post .td-post-content p')
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[:3])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author 
        doc.author = Author.unknown()

        print '========================================================================='
        print 'Title %s' % (doc.title)
        print '-------------------------------------------------------------------------'
        print 'published_at %s' % (doc.published_at)
        print '-------------------------------------------------------------------------'
        print 'summary %s' % (doc.summary)
        print '-------------------------------------------------------------------------'
        print 'text %s' % (doc.text)
        print '-------------------------------------------------------------------------'
        print 'author %s' % (doc.author.name)
        print '========================================================================='
        print '========================================================================='