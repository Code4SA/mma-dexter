from urlparse import urlparse, urlunparse
import re
import HTMLParser

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Author, AuthorType


def unescape(html):
    if html is None:
        return None
    return HTMLParser.HTMLParser().unescape(html)


class IOLCrawler(BaseCrawler):
    # The IOL crawler uses the IOL news feed JSON API and needs
    # an article ID at the end of the URL
    TL_RE = re.compile('(www\.)?iol.co.za/.*\.\d+$')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TL_RE.match(parts.netloc))

    def canonicalise_url(self, url):
        """ Strip anchors, etc. """
        url = super(IOLCrawler, self).canonicalise_url(url)
        parts = urlparse(url)

        # force http, www, remove trailing slash, anchors
        return urlunparse(['http', 'www.iol.co.za', parts.path.rstrip('/'), parts.params, None, None])

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(IOLCrawler, self).extract(doc, raw_html)

        iol_id = doc.url.split('.')[-1]
        info = self.fetch_json_info(iol_id)

        doc.title = unescape(info['title'])
        doc.summary = unescape(info.get('description'))

        doc.text = '\n\n'.join(BeautifulSoup(p).text.strip() for p in info['paragraphs'])
        doc.published_at = self.parse_timestamp(info['published'])
        doc.author = Author.get_or_create(info['byline'], AuthorType.journalist())

    def fetch_json_info(self, iol_id):
        """ Fetch document data in JSON from the IOL API """
        url = 'http://beta.iol.co.za/feed/a/' + iol_id
        self.log.info("Fetching URL: " + url)
        r = requests.get(url, timeout=10)
        # raise an HTTPError on badness
        r.raise_for_status()
        return r.json
