from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Medium, Author, AuthorType

class MGCrawler(BaseCrawler):
    MG_RE = re.compile('(www\.)?mg.co.za')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.MG_RE.match(parts.netloc))

    def canonicalise_url(self, url):
        """ Strip anchors, etc. """
        parts = urlparse(url)

        # force http, strip www, strip trailing slash
        return urlunparse(['http', 'mg.co.za', parts.path.rstrip('/'), parts.params, parts.query, None])

    def fetch(self, url):
        url = url.replace("article", "print")

        self.log.info("Fetching URL: " + url)

        r = requests.get(url)
        # raise an HTTPError on badness
        r.raise_for_status()

        return r.text.encode('utf8')

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """

        doc.medium = Medium.query.filter(Medium.name == 'Mail and Guardian').one()

        soup = BeautifulSoup(raw_html)

        doc.title = self.extract_plaintext(soup.select(".headline_printable"))
        doc.summary = self.extract_plaintext(soup.select(".blurb_printable"))
        doc.text = "\n\n".join(p.text for p in soup.select(".body_printable p"))

        doc.published_at = self.parse_timestamp(self.extract_plaintext(soup.select(".content_place_line")))

        author = self.extract_plaintext(soup.select(".content_place_line_author"))
        if author:
            doc.author = Author.get_or_create(author, AuthorType.journalist())
        else:
            doc.author = Author.unknown()
