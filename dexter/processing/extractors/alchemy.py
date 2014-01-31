import re

from .alchemy_api import AlchemyAPI
from ...models import DocumentKeyword, DocumentEntity, Entity, Utterance

import logging
log = logging.getLogger(__name__)

class AlchemyExtractor:
    """ Use the Alchemy API to extract entities and other
    useful goodies from a document.
    """
    API_KEY = None

    def __init__(self):
        self.alchemy = AlchemyAPI(self.API_KEY)

    def extract(self, doc):
        self.extract_entities(doc)
        self.extract_keywords(doc)

    def extract_entities(self, doc):
        log.info("Extracting entities for %s" % doc)

        entities = self.fetch_entities(doc.text) or []

        log.debug("Raw extracted entities: %s" % entities)

        entities_added = 0
        utterances_added = 0

        for entity in entities:
            # entity
            e = Entity()
            e.group = self.normalise_name(entity['type']).encode('utf-8')
            e.name = entity['text'].encode('utf-8')

            de = DocumentEntity()
            de.entity = e
            de.relevance = float(entity['relevance'])
            de.count = int(entity['count'])

            if doc.add_entity(de):
                entities_added += 1

            # utterances
            for quote in entity.get('quotations', []):
                u = Utterance()
                u.quote = quote['quotation'].strip()
                u.entity = e

                if doc.add_utterance(u):
                    utterances_added += 1

        log.info("Added %d entities and %d utterances for %s" % (entities_added, utterances_added, doc))


    def extract_keywords(self, doc):
        log.info("Extracting keywords for %s" % doc)

        entity_names = set(de.entity.name for de in doc.entities)

        keywords_added = 0
        keywords = self.fetch_keywords(doc.text) or []

        log.debug("Raw extracted keywords: %s" % keywords)

        for kw in keywords:
            # skip keywords that are entity names
            if kw['text'] in entity_names:
                continue

            k = DocumentKeyword()
            k.keyword = kw['text']
            k.relevance = float(kw['relevance'])

            if doc.add_keyword(k):
                keywords_added += 1

        log.info("Added %d keywords for %s" % (keywords_added, doc))


    def fetch_entities(self, text):
        res = self.alchemy.entities('text', text.encode('utf-8'), {
            'quotations': 1,
            'linkedData': 0,
            'sentiment': 0,
            })

        if res['status'] == 'ERROR':
            return None
        return res['entities']


    def fetch_keywords(self, text):
        res = self.alchemy.keywords('text', text.encode('utf-8'))

        if res['status'] == 'ERROR':
            return None
        return res['keywords']


    def normalise_name(self, name):
        return re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()

