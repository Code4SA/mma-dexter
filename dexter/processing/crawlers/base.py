from urlparse import urlparse, urlunparse

import logging
import requests

from dateutil.parser import parse

class BaseCrawler:
    log = logging.getLogger(__name__)

    def offer(self, url):
        """ Can this crawler process this URL? """
        raise NotImplemented()

    def canonicalise_url(self, url):
        """ Strip anchors, etc."""
        parts = urlparse(url)

        # force http, strip trailing slash, anchors etc.
        return urlunparse(['http', parts.netloc, parts.path.rstrip('/'), parts.params, parts.query, None])

    def crawl(self, doc):
        """ Crawl this document. """
        doc.url = self.canonicalise_url(doc.url)
        raw_html = self.fetch(doc.url)
        self.extract(doc, raw_html)

    def fetch(self, url):
        self.log.info("Fetching URL: " + url)

        r = requests.get(url)
        # raise an HTTPError on badness
        r.raise_for_status()

        return r.text.encode('utf8')

    def extract(self, doc, raw_html):
        raise NotImplemented()

    def extract_plaintext(self, lst):
        if len(lst) > 0:
            return lst[0].text.strip()
        return ""


    def parse_timestamp(self, ts):
        return parse(ts, dayfirst=True)
