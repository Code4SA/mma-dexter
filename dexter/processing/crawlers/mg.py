from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests
import logging

from dateutil.parser import parse
from dateutil.tz import tzutc

class MGCrawler:
    MG_RE = re.compile('(www\.)?mg.co.za')
    log = logging.getLogger(__name__)

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.MG_RE.match(parts.netloc))

    def canonicalise_url(self, url):
        """ Strip anchors, etc. """
        parts = urlparse(url)

        # force http, strip www, strip trailing slash
        return urlunparse(['http', 'mg.co.za', parts.path.rstrip('/'), parts.params, parts.query, None])

    def crawl(self, doc):
        """ Crawl this document. """
        doc.url = self.canonicalise_url(doc.url)
        raw_html = self.fetch(doc.url)
        self.extract(doc, raw_html)

    def fetch(self, url):
        url = url.replace("article", "print")

        self.log.info("Fetching URL: " + url)

        r = requests.get(url)
        # raise an HTTPError on badness
        r.status_for_status()

        return r.text.encode('utf8')

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """

        soup = BeautifulSoup(raw_html)

        doc.title = self.extract_plaintext(soup.select(".headline_printable"))
        doc.blurb = self.extract_plaintext(soup.select(".blurb_printable"))
        doc.text = "\n\n".join(p.text for p in soup.select(".body_printable p"))

        doc.published_at = self.parse_timestamp(self.extract_plaintext(soup.select(".content_place_line")))
        # TODO
        # doc.author = extract_plaintext(soup.select(".content_place_line_author"))


    def extract_plaintext(self, lst):
        if len(lst) > 0:
            return lst[0].text.strip()
        return ""


    def parse_timestamp(self, ts):
        return parse(ts)
