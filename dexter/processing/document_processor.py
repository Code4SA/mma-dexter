from itertools import chain

from ..models import Document, Entity, db, Gender, Person
from ..processing import ProcessingError

from .crawlers import MGCrawler, GenericCrawler
from .extractors import AlchemyExtractor, CalaisExtractor, SourcesExtractor

from requests.exceptions import HTTPError
import logging

class DocumentProcessor:
    log = logging.getLogger(__name__)

    def __init__(self):
        self.crawlers = [MGCrawler(), GenericCrawler()]
        self.extractors = [AlchemyExtractor(), CalaisExtractor(), SourcesExtractor()]


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
        self.extract(doc)
        self.discover_people(doc)

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


    def get_or_set_entity(self, entities, entity):
        key = (entity.group.lower(), entity.name.lower())
        if key in entities:
            return entities[key]

        entities[key] = entity
        return entity

    
    def discover_people(self, doc):
        """
        Use this document to create People entries in the database for people that
        don't already exist.

        There is a fair amount of noise in the extracted 'person' entities. So instead
        of trusting those, we only trust the author entity and quoted people.

        The new person instances are bound to their matching entity instances.
        """
        # for each name, a (person, entity) tuple
        people = {}

        for u in (u for u in doc.utterances if u.entity.group == 'person' and not u.entity.person):
            if u.entity.name in people:
                continue
            p = Person()
            p.name = u.entity.name
            people[p.name] = (p, u.entity)

            # guess the gender
            de = doc.mentioned_entity(u.entity)
            if de:
                mentions = set(doc.text[offset:offset+length].lower() for offset, length in de.offsets())
                if 'he' in mentions or 'his' in mentions:
                    p.gender = Gender.male()
                elif 'she' in mentions or 'her' in mentions:
                    p.gender = Gender.female()

        if doc.author and doc.author.group == 'person' and not doc.author.person:
            if doc.author.name not in people:
                p = Person()
                p.name = doc.author.name
                people[p.name] = (p, doc.author)

        # now only keep those that are new
        if people:
            for existing in Person.query.filter(Person.name.in_(people.keys())).all():
                person, entity = people[existing.name]

                if not existing.gender and person.gender:
                    # we've learnt a gender!
                    self.log.info("Learnt gender %s for %s" % (person.gender, existing))
                    existing.gender = person.gender

                # since we only process entities that don't already have a linked Person,
                # at this point we have learnt a new link between an entity and a person
                self.log.info("Linking existing entity %s with existing person %s" % (entity, existing))
                entity.person = existing

                # throw away the new person
                del people[existing.name]

        # all the items in +people+ now need to be added, we do that by linking
        # them to their source entity
        for person, entity in people.itervalues():
            entity.person = person

        self.log.info("Found %d people" % len(people))

        return [p for p, _ in people.itervalues()]
