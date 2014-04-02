from urlparse import urlparse, urlunparse
from dateutil.parser import parse

import logging
import requests

from tld import get_tld

from ...models import Medium

class BaseCrawler(object):
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
        """ Run extractions on the HTML. Subclasses should override this
        method and call super() in their implementations. """
        doc.medium = self.identify_medium(doc)

    def extract_plaintext(self, lst):
        if len(lst) > 0:
            return lst[0].text.strip()
        return ""


    def parse_timestamp(self, ts):
        return parse(ts, dayfirst=True)

    def identify_medium(self, doc):
        if doc.url:
            domain = get_tld(doc.url)
            parts = urlparse(doc.url)

            # iol.co.za/isolezwe
            domain = domain + parts.path

            # find the medium with the longest matching domain
            for medium in sorted(Medium.query.all(), key=lambda m: len(m.domain or ''), reverse=True):
                if medium.domain and domain.startswith(medium.domain):
                    return medium

        return Medium.query.filter(Medium.name == "Unknown").one()
