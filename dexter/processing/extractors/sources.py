from .base import BaseExtractor
from ...processing import ProcessingError
from ...models import DocumentSource, Gender

import logging
log = logging.getLogger(__name__)

class SourcesExtractor(BaseExtractor):
    """ Run after the other extractors, this uses
    extractions to determine links such as classifying
    quoted sources as a document source.
    """

    def extract(self, doc):
        self.extract_sources(doc)
        self.guess_genders(doc)

    def extract_sources(self, doc):
        """
        Add quoted entities as a source, but only if they
        tie up with an actual person.
        """
        log.info("Extracting sources for %s" % doc)

        sources_added = 0

        for u in doc.utterances:
            if u.entity.person:
                p = u.entity.person

                s = DocumentSource()
                s.person = p
                s.quoted = True
                s.unnamed = False

                if doc.add_source(s):
                    sources_added += 1

        log.info("Added %d sources for %s" % (sources_added, doc))

    def guess_genders(self, doc):
        """ Guess genders based on mentioned people and 'his', 'her' etc. """
        for de in doc.entities:
            person = de.entity.person

            if person and not person.gender:
                mentions = set(doc.text[offset:offset+length].lower() for offset, length in de.offsets())

                if 'he' in mentions or 'his' in mentions:
                   person.gender = Gender.male()
                   self.log.info("Learnt gender for %s" % person)

                elif 'she' in mentions or 'her' in mentions:
                   person.gender = Gender.female()
                   self.log.info("Learnt gender for %s" % person)

