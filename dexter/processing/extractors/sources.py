from .base import BaseExtractor
from ...processing import ProcessingError
from ...models import DocumentSource, Gender, Person
from ...utils import levenshtein

import logging

class SourcesExtractor(BaseExtractor):
    """ Run after the other extractors, this uses
    extractions to determine links such as classifying
    quoted sources as a document source.
    """

    log = logging.getLogger(__name__)

    def extract(self, doc):
        self.discover_people(doc)
        self.extract_sources(doc)
        self.guess_genders(doc)


    def discover_people(self, doc):
        """
        If we have entities that are very similar to a person's
        name but isn't already linked, then auto link it.
        """
        tomatch = [u.entity for u in doc.utterances if not u.entity.person]
        if tomatch:
            people = Person.query.all()

            # we could already have found matching people during this loop,
            # so protect against it
            for entity in (e for e in tomatch if not e.person):
                # calculate distance to all other names
                candidates = ((p, levenshtein(p.name, entity.name)) for p in people)
                # limit to only the good ones
                candidates = [(p, x) for p, x in candidates if x >= 0.95]

                if candidates:
                    best = max(candidates, key=lambda p: p[1])
                    self.log.info("Matched entity %s to person %s" % (entity, best[0]))
                    entity.person = best[0]


    def extract_sources(self, doc):
        """
        Add quoted entities as a source, but only if they
        tie up with an actual person.
        """
        self.log.info("Extracting sources for %s" % doc)

        sources_added = 0

        for u in doc.utterances:
            if u.entity.person:
                p = u.entity.person

                s = DocumentSource()
                s.person = p
                s.affiliation = p.affiliation
                s.quoted = True
                s.unnamed = False

                if doc.add_source(s):
                    sources_added += 1

        self.log.info("Added %d sources for %s" % (sources_added, doc))

    def guess_genders(self, doc):
        """ Guess genders based on mentioned people and 'his', 'her' etc. """
        for de in doc.entities:
            if de.entity.person and not de.entity.person.gender:
                de.entity.person.guess_gender_from_doc(doc)
