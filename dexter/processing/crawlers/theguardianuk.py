from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class TheGuardianUKCrawler(BaseCrawler):
    TGUK_RE = re.compile('(www\.)?theguardian.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TGUK_RE.match(parts.netloc))

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
        raw_html = raw_html.encode("utf-8")
        raw_html = unicode(raw_html, errors='ignore')

        super(TheGuardianUKCrawler, self).extract(doc, raw_html)
        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('#article .content__article-body .content__head h1.content__headline'))

        #gather publish date
        date = self.extract_plaintext(soup.select('#article .content__article-body .content__head .content__dateline time.content__dateline-wpd'))
        doc.published_at = self.parse_timestamp(date.replace('.', ':'))

        #gather text and summary
        nodes = soup.select('#article .content__article-body > p')
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[:1])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author 
        author = self.extract_plaintext(soup.select('#article .content__article-body .content__head .byline a span'))
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