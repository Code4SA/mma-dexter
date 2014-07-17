from itertools import chain

from ..models import Document, Entity, db, Gender, Person, DocumentType, DocumentFairness, Fairness
from ..processing import ProcessingError

from .crawlers import MGCrawler, TimesLiveCrawler, IOLCrawler, CitizenCrawler, DailysunCrawler, News24Crawler, NamibianCrawler, GenericCrawler
from .extractors import AlchemyExtractor, CalaisExtractor, SourcesExtractor, PlacesExtractor

from requests.exceptions import HTTPError
import logging

class DocumentProcessor:
    log = logging.getLogger(__name__)

    def __init__(self):
        self.crawlers = [
                MGCrawler(),
                TimesLiveCrawler(),
                CitizenCrawler(),
                DailysunCrawler(),
                News24Crawler(),
                IOLCrawler(),
                NamibianCrawler(),
                # must come last
                GenericCrawler()]
        self.extractors = [
                AlchemyExtractor(),
                CalaisExtractor(),
                SourcesExtractor(),
                PlacesExtractor()]


    def valid_url(self, url):
        """ Is this a URL we can process? """
        return any(c.offer(url) for c in self.crawlers)


    def canonicalise_url(self, url):
        """ Try to canonicalise this url. Strip anchors, etc. """
        for crawler in self.crawlers:
            if crawler.offer(url):
                return crawler.canonicalise_url(url)

        return url


    def process_url(self, url):
        """ Download and process an article at +url+ and return
        a Document instance. """
        doc = Document()
        doc.url = url

        try:
            self.crawl(doc)
            self.process_document(doc)
        except HTTPError as e:
            raise ProcessingError("Error fetching document: %s" % (e,))

        return doc


    def process_document(self, doc):
        """ Process an existing document. """
        self.normalise(doc)
        self.extract(doc)


    def normalise(self, doc):
        """ Run some normalisations on the document. """
        doc.normalise_text()

        if not doc.document_type:
            doc.document_type = DocumentType.query.filter(DocumentType.name == 'News story').one()

        if not doc.fairness:
            df = DocumentFairness()
            df.fairness = Fairness.query.filter(Fairness.name == 'Fair').one()
            doc.fairness.append(df)


    def crawl(self, doc):
        """ Run crawlers against a document's URL to fetch its
        content, updating any existing content. """
        for crawler in self.crawlers:
            if crawler.offer(doc.url):
                crawler.crawl(doc)
                return


    def extract(self, doc):
        """ Run extraction routines on a document. """
        for extractor in self.extractors:
            extractor.extract(doc)


    def get_or_set_entity(self, entities, entity):
        key = (entity.group.lower(), entity.name.lower())
        if key in entities:
            return entities[key]

        entities[key] = entity
        return entity
