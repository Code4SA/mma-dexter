import re
import logging

from .base import BaseExtractor
from ...models import DocumentSource, Person
from ...utils import levenshtein


class SourcesExtractor(BaseExtractor):
    """ Run after the other extractors, this uses
    extractions to determine links such as classifying
    quoted sources as a document source.
    """

    log = logging.getLogger(__name__)
    NAME_DIRTY_RE = re.compile(r'\s*\b(Chief|Justice|Deputy|Judge|President|Minister)\b\s*', re.I)

    def extract(self, doc):
        self.discover_people(doc)
        self.extract_sources(doc)
        self.guess_genders(doc)

    def discover_people(self, doc):
        """
        If we have entities that are very similar to a person's
        name but isn't already linked, then auto link it.
        """
        self.log.info("Matching entities to people")
        count = 0

        tomatch = set(u.entity for u in doc.utterances if not u.entity.person)
        if tomatch:
            people = Person.query.all()
            people_by_name = {p.name: p for p in people}

            # we could already have found matching people during this loop,
            # so protect against it
            for entity in (e for e in tomatch if not e.person):
                name = self.clean_name(entity.name)
                self.log.info("Trying to match entity '%s' to a person as '%s'" % (entity.name, name))

                match = None
                entity_name_len = len(name)

                if name in people_by_name:
                    # exact match
                    match = people_by_name[name]

                else:
                    # calculate distance to all other names
                    # as a small optimisation, don't test an entity if the
                    # length of the names is too different
                    candidates = (
                        (p, levenshtein(p.name, name))
                        for p in people
                        if abs(len(p.name) - entity_name_len) <= 2)

                    # limit to only the good ones
                    candidates = [(p, x) for p, x in candidates if x >= 0.95]
                    if candidates:
                        match = max(candidates, key=lambda p: p[1])[0]

                if match:
                    count += 1
                    self.log.info("Matched entity %s to person %s" % (entity, match))
                    entity.person = match

        self.log.info("Matched %s entities to people" % count)

    def clean_name(self, name):
        return self.NAME_DIRTY_RE.sub('', name)

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
