from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from .generic import GenericCrawler
from ...models import Entity, Author, AuthorType

class News24Crawler(BaseCrawler):
    TL_RE = re.compile('(www\.)?news24.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TL_RE.match(parts.netloc))

    def canonicalise_url(self, url):
        """ Strip anchors, etc. """
        parts = urlparse(url)

        # force http, force www
        return urlunparse(['http', 'www.news24.com', parts.path, parts.params, parts.query, None])

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(News24Crawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        tags = soup.select('meta[property="twitter:description"]')
        if tags:
            doc.summary = tags[0].attrs.get('content')

        author = None
        if soup.select("#article_special"):
            # old style of news24 articles
            doc.title = self.extract_plaintext(soup.select(".article h1"))

            text = []
            for p in soup.select(".article > p"):
                for tag in p.children:
                    if not tag.name:
                        text.append(str(tag))
                    elif tag.text:
                        text.append(tag.text)

            doc.text = '\n\n'.join(text)

            doc.published_at = self.parse_timestamp(self.extract_plaintext(soup.select(".page-lead-datetime")))
            author = self.extract_plaintext(soup.select("#_htmlAccreditationName")).strip('- ').strip()

        elif soup.select(".article-content article"):
            # new style of news24 articles (eg. for elections)
            doc.title = self.extract_plaintext(soup.select(".article-content article h1"))
            doc.text = "\n\n".join(p.text for p in soup.select(".article-content article > p"))
            doc.published_at = self.parse_timestamp(self.extract_plaintext(soup.select(".page-lead-datetime")))
            author = self.extract_plaintext(soup.select("#accreditationName")).strip('- ').strip()

        else:
            # fall back to the generic crawler
            self.log.info("Couldn't identify article content, falling back to generic crawler")
            g = GenericCrawler()
            g.crawl(doc)
            return

        if author:
            doc.author = Author.get_or_create(author, AuthorType.journalist())
        else:
            doc.author = Author.unknown()
