from .base import BaseExtractor
from ...processing import ProcessingError
from ...models import Place, DocumentPlace

import logging

class PlacesExtractor(BaseExtractor):
    """ Run after the other extractors, this uses
    extractions to find links to places.
    """

    log = logging.getLogger(__name__)

    def extract(self, doc):
        self.extract_places(doc)

    def extract_places(self, doc):
        """
        Go through document entities and see if they match
        a place in South Africa. If it does, link them.
        """
        if doc.country.code != 'za':
            self.log.info("Not extracting places for %s" % doc.country)
            return

        self.log.info("Extracting places for %s" % doc)

        places_added = 0

        for de in doc.entities:
            # don't look for a place if we know it's a person
            if de.entity.person:
                continue

            place = Place.find(de.entity.name)

            if place:
                dp = DocumentPlace()
                dp.place = place
                dp.relevance = de.relevance
                dp.offset_list = de.offset_list

                if doc.add_place(dp):
                    places_added += 1

        if places_added:
            # work out which places we consider relevant, based
            # on their relevance scores
            threshold = doc.places_relevance_threshold()
            for dp in doc.places:
                if dp.relevance >= threshold:
                    dp.relevant = True

        self.log.info("Added %d places for %s" % (places_added, doc))
