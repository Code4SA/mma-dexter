from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class BusinessDailyAfricaCrawler(BaseCrawler):
    BDA_RE = re.compile('(www\.)?businessdailyafrica.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.BDA_RE.match(parts.netloc))

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
        super(BusinessDailyAfricaCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('article.article-story .page-box-inner header .article-title'))

        #gather publish date
        date = self.extract_plaintext(soup.select('article.article-story .page-box-inner header .byline'))
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('article.article-story .page-box-inner p')
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[:2])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author
        author = ''
        byline = self.extract_plaintext(soup.select('article.article-story .page-box-inner header .mobileShow .byline'))
        if 'BY ' in byline:
            author = byline[byline.index('BY ') + 3:]
        else:
            author = byline
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