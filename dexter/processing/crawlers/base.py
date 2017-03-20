from urlparse import urlparse, urlunparse
from dateutil.parser import parse

import logging
import requests

from ...models import Medium

class BaseCrawler(object):
    log = logging.getLogger(__name__)

    def offer(self, url):
        """ Can this crawler process this URL? """
        raise NotImplemented()


    def canonicalise_url(self, url):
        """ Strip anchors, etc."""

        # Needed to handle urls being recieved without protocol (http[s]://), check if it can be parsed first, then handle and re parse if there is no netloc found
        # Also checking for any www. to handle these in particular. otherwise it should still fail (perhaps need to handle other outliers in future)
        if '//' not in url:
            url = '%s%s' % ('http://', url)

        parts = urlparse(url)

        netloc = parts.netloc.strip(':80')

        # force http, strip trailing slash, anchors etc.
        return urlunparse(['http', netloc, parts.path.rstrip('/') or '/', parts.params, parts.query, None])


    def crawl(self, doc):
        """ Crawl this document. """
        doc.url = self.canonicalise_url(doc.url)
        raw_html = self.fetch(doc.url)
        self.extract(doc, raw_html)


    def fetch(self, url):
        """
        Fetch and return the raw HTML for this url.
        The return content is a unicode string.
        """
        self.log.info("Fetching URL: " + url)

        r = requests.get(url, timeout=10)
        # raise an HTTPError on badness
        r.raise_for_status()

        # this decodes r.content using a guessed encoding
        return r.text


    def extract(self, doc, raw_html):
        """ Run extractions on the HTML. Subclasses should override this
        method and call super() in their implementations. """
        doc.raw_html = raw_html
        doc.medium = self.identify_medium(doc)
        doc.country = doc.medium.country


    def extract_plaintext(self, lst):
        if len(lst) > 0:
            return lst[0].text.strip()
        return ""


    def parse_timestamp(self, ts):
        return parse(ts, dayfirst=True)


    def identify_medium(self, doc):
        if doc.url:
            medium = Medium.for_url(doc.url)
        return medium or Medium.query.filter(Medium.name == "Unknown").one()
