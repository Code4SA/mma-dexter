from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class GuardianCrawler(BaseCrawler):
    G_RE = re.compile('guardian.ng')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.G_RE.match(parts.netloc))

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
        super(GuardianCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)
        # gather title
        doc.title = self.extract_plaintext(soup.select('.single-post-header h1.single-article-title'))

        #gather publish date
        date = self.extract_plaintext(soup.select('.page-main .single-article-aside .single-article-datetime'))
        doc.published_at = self.parse_timestamp(date[:date.index('|') - 1].strip() + ' ' + date[date.index('|') + 1:].strip())
        
        #gather text and summary
        summary_list = []
        summary_nodes = soup.select('.page-main .single-article-content article')
        for item in summary_nodes[0].find('br').next_siblings:
            if item != u'\n':
                if isinstance(item, basestring):
                    summary_list.append(item)
                else:
                    summary_list.append(item.text)
        summary = summary_list[0].strip()
        doc.summary = summary
        text_nodes = soup.select('.page-main .single-article-content article p')
        doc.text = summary + "\n\n" + "\n\n".join(p.text.strip() for p in text_nodes[2:])

        # gather author 
        author = self.extract_plaintext(soup.select('.page-main .single-article-aside .single-article-author strong'))
        if author:
            if ',' in author:
                doc.author = Author.get_or_create(author[:author.index(',')].strip(), AuthorType.journalist())
            else:
                doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()
