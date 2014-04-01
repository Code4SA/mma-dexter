from urlparse import urlparse, urlunparse

import logging

from dateutil.parser import parse

class BaseCrawler:
    log = logging.getLogger(__name__)

    def offer(self, url):
        """ Can this crawler process this URL? """
        raise NotImplemented()

    def canonicalise_url(self, url):
        """ Strip anchors, etc."""

        parts = urlparse(url)
        # force http, strip trailing slash
        return urlunparse(['http', parts.netloc, parts.path.rstrip('/'), parts.params, parts.query, None])

    def crawl(self, doc):
        """ Crawl this document. """
        raise NotImplemented()



    def extract_plaintext(self, lst):
        if len(lst) > 0:
            return lst[0].text.strip()
        return ""


    def parse_timestamp(self, ts):
        return parse(ts, dayfirst=True)
