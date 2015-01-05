from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup

from .base import BaseCrawler
from ...models import Author

class ZambiaDailyNationCrawler(BaseCrawler):
    TL_RE = re.compile('(www\.)?zambiadailynation.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TL_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(ZambiaDailyNationCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        doc.title = self.extract_plaintext(soup.select(".post-alt h2 a"))
    
        # there are multiple divs with this id
        nodes = soup.select(".post-alt .entry p")
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        text = self.extract_plaintext(soup.select(".post-alt .post_date"))
        text = text.replace('Posted on ', '').replace('.', '')
        doc.published_at = self.parse_timestamp(text)

        doc.author = Author.unknown()
