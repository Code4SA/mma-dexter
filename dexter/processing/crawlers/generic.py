from urlparse import urlparse, urlunparse
from newspaper import Article
import logging
from tld import get_tld
from sqlalchemy.orm.exc import NoResultFound

from dateutil.parser import parse

from ...models import Entity, Medium, Author, AuthorType


class GenericCrawler:
    log = logging.getLogger(__name__)

    def offer(self, url):
        """ Can this crawler process this URL? """

        return True

    def canonicalise_url(self, url):
        """ Strip anchors, etc."""

        parts = urlparse(url)
        # force http, strip trailing slash
        return urlunparse(['http', parts.netloc, parts.path.rstrip('/'), parts.params, parts.query, None])

    def crawl(self, doc):
        """ Crawl this document. """

        # instantiate and download article
        article = Article(url=doc.url, language='en', fetch_images=False, request_timeout=10)
        article.download()

        # associate with Medium instance
        domain = get_tld(doc.url)
        try:
            medium = Medium.query.filter(Medium.domain == domain).one()
        except NoResultFound as e:
            medium = Medium.query.filter(Medium.name == "Unknown").one()
        doc.medium = medium

        # extract content
        self.extract(doc, article)
        return

    def extract(self, doc, article):
        """ Extract text and other things from this document. """

        article.parse()
        doc.title = article.title
        doc.text = article.text

        # todo: handle multiple authors
        authors = article.authors
        if authors:
            author = authors[0]
            doc.author = Author.get_or_create(author, AuthorType.journalist())
        else:
            doc.author = Author.unknown()

        doc.published_at = self.parse_timestamp(article.published_date)

    def parse_timestamp(self, ts):
        return parse(ts)
