import re

from .alchemy_api import AlchemyAPI
from ...models import DocumentKeyword, DocumentEntity, Entity, Utterance

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
        entities = self.fetch_entities(doc.text) or []

        for entity in entities:
            # entity
            e = Entity()
            e.group = self.normalise_name(entity['type'])
            e.name = entity['text']

            de = DocumentEntity()
            de.entity = e
            de.relevance = float(entity['relevance'])
            de.count = int(entity['count'])
            doc.add_entity(de)

            # utterances
            for quote in entity.get('quotations', []):
                u = Utterance()
                u.quote = quote['quotation'].strip()
                u.entity = e
                doc.add_utterance(u)


    def extract_keywords(self, doc):
        entity_names = set(de.entity.name for de in doc.entities)

        keywords = self.fetch_keywords(doc.text) or []
        for kw in keywords:
            # skip keywords that are entity names
            if kw['text'] in entity_names:
                continue

            k = DocumentKeyword()
            k.keyword = kw['text']
            k.relevance = float(kw['relevance'])

            doc.add_keyword(k)


    def fetch_entities(self, text):
        res = self.alchemy.entities('text', text, {
            'quotations': 1,
            'linkedData': 0,
            'sentiment': 0,
            })

        if res['status'] == 'ERROR':
            return None
        return res['entities']


    def fetch_keywords(self, text):
        res = self.alchemy.keywords('text', text)

        if res['status'] == 'ERROR':
            return None
        return res['keywords']


    def normalise_name(self, name):
        return re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()

