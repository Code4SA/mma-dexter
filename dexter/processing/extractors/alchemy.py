import re

from .base import BaseExtractor
from .alchemy_api import AlchemyAPI
from ...processing import ProcessingError
from ...models import DocumentKeyword, DocumentEntity, Entity, Utterance

import logging
log = logging.getLogger(__name__)

class AlchemyExtractor(BaseExtractor):
    """ Use the Alchemy API to extract entities and other
    useful goodies from a document.
    """
    API_KEY = None

    def __init__(self):
        # NOTE: set the ENV variable ALCHEMY_API_KEY before running the process
        if not self.API_KEY:
            raise ValueError('%s.%s.API_KEY must be defined.' % (self.__module__, self.__class__.__name__))
        self.alchemy = AlchemyAPI(self.API_KEY)

    def extract(self, doc):
        if doc.text:
            try:
                self.fetch_extract_entities(doc)
                self.fetch_extract_keywords(doc)
            except ProcessingError as e:
                if e.message == 'unsupported-text-language':
                    log.info('Ignoring processing error: %s' % e.message)
                else:
                    raise e

    def fetch_extract_entities(self, doc):
        log.info("Extracting entities for %s" % doc)
        self.extract_entities(doc, self.fetch_entities(doc) or [])


    def extract_entities(self, doc, entities):
        log.debug("Raw extracted entities: %s" % entities)

        entities_added = 0
        utterances_added = 0

        for entity in entities:
            # ignore short names
            if len(entity['text']) < 2:
                continue

            # entity
            e = Entity.get_or_create(self.normalise_name(entity['type']), entity['text'])

            de = DocumentEntity()
            de.entity = e
            de.relevance = float(entity['relevance'])
            de.count = int(entity['count'])

            # do our best to guess occurrences
            de.offset_list = self.all_offsets(doc.text, e.name)[:100]

            if doc.add_entity(de):
                entities_added += 1

            # utterances
            for quote in entity.get('quotations', []):
                u = Utterance()
                u.quote = quote['quotation'].strip()
                u.entity = e
                
                # lame effort to find quote offset - alchemy often puts ... at the end
                needle = u.quote.strip(' .')
                offset = doc.text.find(needle)
                if offset > -1:
                    u.offset = offset
                    u.length = len(needle)

                if doc.add_utterance(u):
                    utterances_added += 1

        log.info("Added %d entities and %d utterances for %s" % (entities_added, utterances_added, doc))


    def fetch_extract_keywords(self, doc):
        log.info("Extracting keywords for %s" % doc)
        self.extract_keywords(doc, self.fetch_keywords(doc) or [])


    def extract_keywords(self, doc, keywords):
        entity_names = set(de.entity.name for de in doc.entities)
        keywords_added = 0

        log.debug("Raw extracted keywords: %s" % keywords)

        for kw in keywords:
            # skip keywords that are entity names
            if kw['text'] in entity_names:
                continue

            k = DocumentKeyword()
            k.keyword = kw['text'][0:100]
            k.relevance = float(kw['relevance'])
            k.offset_list = self.all_offsets(doc.text, k.keyword)

            if doc.add_keyword(k):
                keywords_added += 1

        log.info("Added %d keywords for %s" % (keywords_added, doc))


    def fetch_entities(self, doc):
        res = self.check_cache(doc.url, 'alchemy-entities')

        if not res:
            res = self.alchemy.entities('text', doc.text.encode('utf-8'), {
                'quotations': 1,
                'linkedData': 0,
                'sentiment': 0,
                })
            if res['status'] == 'ERROR':
                raise ProcessingError(res['statusInfo'])
            self.update_cache(doc.url, 'alchemy-entities', res)

        return res['entities']


    def fetch_keywords(self, doc):
        res = self.check_cache(doc.url, 'alchemy-keywords')

        if not res:
            res = self.alchemy.keywords('text', doc.text.encode('utf-8'))
            if res['status'] == 'ERROR':
                raise ProcessingError(res['statusInfo'])
            self.update_cache(doc.url, 'alchemy-keywords', res)

        return res['keywords']

    def all_offsets(self, text, needle):
        needle_len = len(needle)
        start = 0
        offsets = []

        while True:
            start = text.find(needle, start)
            if start == -1:
                break
            offsets.append((start, needle_len))
            start += needle_len

        return ' '.join('%d:%d' % p for p in offsets)

