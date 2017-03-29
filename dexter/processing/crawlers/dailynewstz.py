from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class DilyNewsTZCrawler(BaseCrawler):
    DNTZ_RE = re.compile('(www\.)?dailynews.co.tz')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.DNTZ_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(DilyNewsTZCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        # gather title
        doc.title = self.extract_plaintext(soup.select(".article-main .article-header .article-title"))

        #gather publish date
        date = self.extract_plaintext(soup.select(".article-main .article-aside .published time"))
        doc.published_at = self.parse_timestamp(date)
        
        #gather text and summary
        doc.summary = self.extract_plaintext(soup.select(".article-main .article-full .article-content-main .article-intro p"))
        nodes = soup.select(".article-main .article-full .article-content-main .article-content p")
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        # gather author 
        author = self.extract_plaintext(soup.select(".article-main .article-aside .createdby span:first-child"))
        if author:
            doc.author = Author.get_or_create(author.strip(), AuthorType.journalist())
        else:
            doc.author = Author.unknown()

