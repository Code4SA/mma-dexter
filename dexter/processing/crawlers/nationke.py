from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class NationKECrawler(BaseCrawler):
    NAKE_RE = re.compile('(www\.)?nation.co.ke')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.NAKE_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        
        # need to strip illegal 4 byte characters present on this site like the dot on form submission button: "\xee\x80\x81" ( \uE001 )
        raw_html = raw_html.replace(u"\uE001", "")

        super(NationKECrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)


        doc.title = self.extract_plaintext(soup.select(".container .main .story-view header h1"))
    
        nodes = soup.select(".container .main .story-view .article .body-copy > div > p")
        doc.text = "\n\n".join(p.getText().strip() for p in nodes)

        published_text = self.extract_plaintext(soup.select(".container .main .story-view header h5"))
        doc.published_at = self.parse_timestamp(published_text)

        author_text = soup.select(".container .main .story-view .article .body-copy .author strong")
        author = self.extract_plaintext(author_text).replace("By ", '')
        
        # detect a junk author
        if len(author) > 100 or author.count(' ') > 5:
            author = None

        if author:
            doc.author = Author.get_or_create(author, AuthorType.journalist())
        else:
            doc.author = Author.unknown()
