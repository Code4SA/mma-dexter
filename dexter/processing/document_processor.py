from ..models import Document, DBSession
from ..models.entity import EntityFactory

from .crawlers import MGCrawler
from .extractors import AlchemyExtractor

import logging

class DocumentProcessor:
    log = logging.getLogger(__name__)

    def __init__(self):
        self.crawlers = [MGCrawler()]
        self.extractors = [AlchemyExtractor()]
        self.entity_factory = EntityFactory()


    def valid_url(self, url):
        """ Is this a URL we can process? """
        return any(c.offer(url) for c in self.crawlers)


    def canonicalise_url(self, url):
        """ Try to canonicalise this url. Strip anchors, etc. """
        for crawler in self.crawlers:
            if crawler.offer(url):
                return crawler.canonicalise_url(url)

        return url


    def process(self, url):
        """ Downloand and process an article at +url+ and return
        a Document instance. """
        doc = Document()
        doc.url = url

        self.crawl(doc)
        self.extract(doc)

        return doc

    def crawl(self, doc):
        """ Run crawlers against a document's URL to fetch its
        content, updating any existing content. """
        for crawler in self.crawlers:
            if crawler.offer(doc.url):
                crawler.crawl(doc)


    def extract(self, doc):
        """ Run extraction routines on a document. """
        for extractor in self.extractors:
            extractor.extract(doc)


    def persist(self, doc):
        """
        Write this document, and all its entities, to the database.

        If the document or any related entity has already been written,
        those objects are untouched (and changes will be written naturally.)

        Entities are only written if they aren't already in the database. This
        means a document can be created (or updated) with entities added
        naively by their group and name, and this method will sort out what
        needs to be written and what doesn't.

        Note: if an entity is new and another processor creates it at the same
        time, there is a race condition. The database is left intact and correct,
        but one processor will get a key violation exception.
        """
        # ensure all these entities exist
        for de in document.entities:
            de.entity = self.entity_factory.get_or_create(de.entity)
        for utterance in document.utterances:
            utterance.entity = self.entity_factory.get_or_create(utterance.entity)

        DBSession.add(doc)
