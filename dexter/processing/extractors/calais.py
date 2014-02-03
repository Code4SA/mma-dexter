import re
import requests

from .base import BaseExtractor
from ...processing import ProcessingError
from ...models import DocumentKeyword, DocumentEntity, Entity, Utterance

import logging
log = logging.getLogger(__name__)

class CalaisExtractor(BaseExtractor):
    """ Use the OpenCalais API to extract entities and other
    useful goodies from a document.
    """
    API_KEY = None

    def __init__(self):
        pass

    def extract(self, doc):
        log.info("Extracting things for %s" % doc)

        calais = self.fetch_data(doc.text).get('extractions', {})

        log.debug("Raw calais extractions: %s" % calais)

        self.extract_entities(doc, calais)
        self.extract_utterances(doc, calais)


    def extract_entities(self, doc, calais):
        entities_added = 0

        for group, group_ents in calais.get('entities', {}).iteritems():
            group = self.normalise_name(group)

            for ent in group_ents.itervalues():
                if not 'name' in ent:
                    continue

                e = Entity()
                e.group = group
                e.name = ent['name']

                de = DocumentEntity()
                de.entity = e
                de.relevance = float(ent['relevance'])
                de.count = len(ent['instances'])

                if doc.add_entity(de):
                    entities_added += 1

        log.info("Added %d entities for %s" % (entities_added, doc))


    def extract_utterances(self, doc, calais):
        utterances_added = 0

        for quote in calais.get('relations', {}).get('Quotation', {}).itervalues():
            u = Utterance()
            u.quote = quote['quote'].strip()

            # uttering entity
            u.entity = Entity()
            u.entity.group = self.normalise_name(quote['person']['_type'])
            u.entity.name = quote['person']['name']

            if doc.add_utterance(u):
                utterances_added += 1

        log.info("Added %d utterances for %s" % (utterances_added, doc))


    def fetch_data(self, text):
        res = requests.post('http://api.opencalais.com/tag/rs/enrich', text.encode('utf-8'),
            headers={
                'x-calais-licenseID': self.API_KEY,
                'content-type': 'text/raw',
                'accept': 'application/json',
                })

        if res.status_code == 200:
            return self.normalise(res.json())
        else:
            res.raise_for_status()


    def normalise(self, js):
        """ Change the JSON OpenCalais gives back into
        a nicer layout, keying extractions by their type.
        """
        # resolve references
        for key, val in js.iteritems():
            if isinstance(val, dict):
                for attr, attr_val in val.iteritems():
                    if isinstance(attr_val, basestring):
                        if attr_val in js:
                            val[attr] = js[attr_val]

        n = {}
        things = {}
        n['extractions'] = things

        # produces:
        #
        # extractions:
        #   entities:
        #     City: [ ... ]
        #     Person: [ ... ]
        #   relations:
        #     Quotation: [ ... ]


        for key, val in js.iteritems():
            grp = val.get('_typeGroup')

            if grp:
                if grp not in things:
                    things[grp] = {}
                grp = things[grp]

                typ = val.get('_type')
                if typ not in grp:
                    grp[typ] = {}

                grp[typ][key] = val
            else:
                n[key] = val

        return n
