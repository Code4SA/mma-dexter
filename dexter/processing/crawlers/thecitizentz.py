from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests
import logging

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class TheCitizenTZCrawler(BaseCrawler):
    TCTZ = re.compile('(www\.)?thecitizen.co.tz')
    log = logging.getLogger(__name__)

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TCTZ.match(parts.netloc))


    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(TheCitizenTZCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select("article.main.column .story-view header h1"))

        #gather publish date
        date = self.extract_plaintext(soup.select("article.main.column .story-view header h5"))
        doc.published_at = self.parse_timestamp(date)
        
        #gather text and summary
        nodes = soup.select("article.main.column .story-view .article .body-copy p")
        if len(nodes) > 1:
            doc.summary = self.extract_plaintext(nodes[1:2])
        doc.text = "\n\n".join(p.text.strip() for p in nodes[1:])

        # gather author 
        author = date = self.extract_plaintext(soup.select("article.main.column .story-view .article .author")).replace("By ", '').split('@')[0]
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()

