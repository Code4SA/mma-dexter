from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class ACDIVOCACrawler(BaseCrawler):
    ACDIVO_RE = re.compile('(www\.)?acdivoca.org')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.ACDIVO_RE.match(parts.netloc))

    def fetch(self, url):
        """
        Fetch and return the raw HTML for this url.
        The return content is a unicode string.
        """
        self.log.info("Fetching URL: " + url)

        headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}

        r = requests.get(url, headers=headers, timeout=10)
        # raise an HTTPError on badness
        r.raise_for_status()

        # this decodes r.content using a guessed encoding
        return r.text

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(ACDIVOCACrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('#main #page-title'))

        #gather publish date
        date = self.extract_plaintext(soup.select('#main .meta-top .date'))
        doc.published_at = self.parse_timestamp(date)

        #gather text and summary
        nodes = soup.select('#main .main-content p')
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[:1])
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author 
        author = self.extract_plaintext(soup.select('#main .meta-author h3 a'))
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()
