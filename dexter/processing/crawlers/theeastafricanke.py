from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class TheEastAfricanKECrawler(BaseCrawler):
    TEAKE_RE = re.compile('(www\.)?theeastafrican.co.ke')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TEAKE_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(TheEastAfricanKECrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select("#articlebody h1"))

        #gather publish date
        self.log.info(self.extract_plaintext(soup.select("#articlemeta")))
        published_text = self.extract_plaintext(soup.select("#articlemeta")).split("Posted",1)[1].strip("\n").replace(u'\xa0', ' ')
        doc.published_at = self.parse_timestamp(published_text)
        
        #gather text and summary
        nodes = soup.select("#contentwrapper #article_text p")
        if len(nodes) > 1:
            doc.summary = self.extract_plaintext(nodes[0:1])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author 
        author = soup.find(attrs={"property":"og:author"})['content'].rstrip(", ")
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()

