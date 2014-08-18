from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class NamibianCrawler(BaseCrawler):
    TL_RE = re.compile('(www\.)?namibian.com.na')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TL_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(NamibianCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        doc.title = self.extract_plaintext(soup.select("#story_heading2"))
    
        # there are multiple divs with this id
        nodes = soup.select("#story_text")
        if len(nodes) > 1:
            doc.summary = self.extract_plaintext(nodes[0:1])
            nodes = nodes[1:]
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        if doc.summary:
          doc.text = doc.summary + "\n\n" + doc.text

        # there are multiple divs with this id
        story_cats = soup.select("#story_cat")
        text = self.extract_plaintext(story_cats[0:1])
        doc.published_at = self.parse_timestamp(' '.join(text.split("|")[1:]))

        author = self.extract_plaintext(story_cats[1:]).replace("By ", '')
        # detect a junk author
        if len(author) > 100 or author.count(' ') > 5:
            author = None

        if author:
            doc.author = Author.get_or_create(author, AuthorType.journalist())
        else:
            doc.author = Author.unknown()
