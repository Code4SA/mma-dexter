from newspaper import Article
import logging

from dateutil.parser import parse

from ...models import Entity, Medium

class GenericCrawler:
    log = logging.getLogger(__name__)

    def offer(self, url):
        """ Can this crawler process this URL? """

        return True

    def canonicalise_url(self, url):
        """ Just return the URL. DocumentProcessor expects this method to be in place.  """
        return url

    def crawl(self, doc):
        """ Crawl this document. """
        article = Article(url=doc.url)
        article.download()
        self.extract(doc, article)
        return

    def extract(self, doc, article):
        """ Extract text and other things from the raw_html for this document. """

        # todo: find medium from known list, os set to unknown
        # doc.medium = Medium.query.filter(Medium.name == 'Mail and Guardian').one()

        article.parse()
        doc.title = article.title
        doc.summary = article.summary
        doc.text = article.text

        # todo: handle multiple authors
        authors = article.authors
        if authors:
            doc.author = Entity.get_or_create('person', authors[0])

        doc.published_at = self.parse_timestamp(article.published_date)

    def parse_timestamp(self, ts):
        return parse(ts)
