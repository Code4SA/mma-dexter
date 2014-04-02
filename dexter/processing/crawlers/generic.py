from newspaper import Article
from sqlalchemy.orm.exc import NoResultFound

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType


class GenericCrawler(BaseCrawler):
    def offer(self, url):
        """ Can this crawler process this URL? """

        return True

    def crawl(self, doc):
        """ Crawl this document. """

        # instantiate and download article
        article = Article(url=doc.url, language='en', fetch_images=False, request_timeout=10)
        article.download()

        # extract content
        self.extract(doc, article)


    def extract(self, doc, article):
        """ Extract text and other things from this document. """
        super(GenericCrawler, self).extract(doc, article)

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
