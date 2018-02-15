from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class ChannelAfricaCrawler(BaseCrawler):
    CA_RE = re.compile('(www\.)?channelafrica.co.za')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.CA_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(ChannelAfricaCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('.MainContentInner .inPageHeader'))

        #gather publish date
        date = self.extract_plaintext(soup.select('.MainContentInner .datesContainer .dates'))
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        summary = self.extract_plaintext(soup.select('.MainContentInner .ArticleInner .excerpt p'))
        doc.summary = summary
        nodes = soup.select('.MainContentInner .ArticleInner .articleBody p')
        doc.text = summary + '\n\n' + "\n\n".join(p.text.strip() for p in nodes)

        # gather author 
        doc.author = Author.unknown()