from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class RSAParliamentCrawler(BaseCrawler):
    RSAP_RE = re.compile('(www\.)?parliament.gov.za')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.RSAP_RE.match(parts.netloc))

    def canonicalise_url(self, url):
        """ Strip anchors, etc."""

        # Needed to handle urls being recieved without protocol (http[s]://), check if it can be parsed first, then handle and re parse if there is no netloc found
        if '//' not in url:
            url = '%s%s' % ('https://', url)

        parts = urlparse(url)

        netloc = parts.netloc.strip(':80')

        # force http, strip trailing slash, anchors etc.
        return urlunparse(['https', netloc, parts.path.rstrip('/') or '/', parts.params, parts.query, None])

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(RSAParliamentCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select('.page .page-header h4'))


        #gather text and summary
        nodes = soup.select('.page #content .page-content p')
        doc.summary = "\n\n".join(p.text.strip() for p in nodes[:1])
        doc.text = "\n\n".join(p.text.strip() for p in nodes[:-1])

        #gather publish date
        date_pattern = re.compile('(?:\s|\w){1}(\d{1,2} (?:January|February|March|April|May|June|July|August|September|October|November|December) \d{4})(?:[\s\w]|$)')
        if re.search(date_pattern, nodes[0].text) != None:
            date = re.search(date_pattern, nodes[0].text).group(0)
        if re.search(date_pattern, nodes[-1].text) != None: 
            date = re.search(date_pattern, nodes[-1].text).group(0)
        doc.published_at = self.parse_timestamp(date.strip())    
        
        #gather author 
        author_pattern = re.compile('(?:By )?([\w ]*)\s*(?:\d{1,2} (?:January|February|March|April|May|June|July|August|September|October|November|December) \d{4})(?:\s|$)|(?:Name: )([\w ]+)')
        reg_result = re.search(author_pattern, nodes[-1].text)
        if reg_result != None:
            author = reg_result.group(1) if reg_result.group(1) else reg_result.group(2)
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()
