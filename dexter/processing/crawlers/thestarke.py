from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class TheStarKECrawler(BaseCrawler):
    TSKE_RE = re.compile('(www\.)?standardmedia.co.ke')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TSKE_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(StandardMediaCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select(".l-region--title .pane-page-title h1"))

        #gather publish date
        published_text = soup.find(attrs={"property":"og:updated_time"})['content']
        doc.published_at = self.parse_timestamp(published_text)
        
        #gather text and summary
        nodes = soup.select(".l-region--content .panel-pane .pane-node-content .field p")
        if len(nodes) > 1:
            doc.summary = self.extract_plaintext(nodes[0:1])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author
        author = self.extract_plaintext(soup.select(".pane-node-field-converge-byline .field--name-field-converge-byline .field__item")).replace("By ", '').split('@')[0]
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()

