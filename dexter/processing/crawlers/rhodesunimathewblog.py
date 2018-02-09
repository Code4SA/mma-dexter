from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class RhodesUniMathewBlogCrawler(BaseCrawler):
    RUMB_RE = re.compile('mathewnyaungwa.blogspot.co.za')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.RUMB_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(RhodesUniMathewBlogCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('.blog-posts .date-posts .post-title'))

        #gather publish date
        date = self.extract_plaintext(soup.select('.blog-posts .date-header span'))
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('.blog-posts .date-posts .post-body span')
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[:1])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author 
        author = self.extract_plaintext(soup.select('.blog-posts .post-footer a.g-profile'))
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
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