from .base import BaseExtractor
from ...processing import ProcessingError
from ...models import DocumentSource

import logging
log = logging.getLogger(__name__)

class SourcesExtractor(BaseExtractor):
    """ Run after the other extractors, this uses
    extractions to determine links such as classifying
    quoted sources as a document source.
    """

    def extract(self, doc):
        self.extract_sources(doc)


    def extract_sources(self, doc):
        """
        Add quoted entities as a source.
        """
        log.info("Extracting sources for %s" % doc)

        sources_added = 0

        for u in doc.utterances:
            s = DocumentSource()
            s.entity = u.entity
            s.quoted = True

            if doc.add_source(s):
                sources_added += 1

        log.info("Added %d sources for %s" % (sources_added, doc))
