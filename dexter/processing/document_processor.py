from itertools import chain

from ..models import Document, Entity, db, Gender, Person, DocumentType, DocumentFairness, Fairness, AnalysisNature
from ..processing import ProcessingError

from .crawlers import *
from .extractors import AlchemyExtractor, CalaisExtractor, SourcesExtractor, PlacesExtractor

import requests
from requests.exceptions import HTTPError
import logging

class DocumentProcessor:
    log = logging.getLogger(__name__)

    FEED_URL = 'https://www.newstools.co.za/newstoolspider/index.php/dexter/articles/%s'
    FEED_USER = 'dexter'
    FEED_PASSWORD = None

    def __init__(self):
        self.newstools_crawler = NewstoolsCrawler()

        self.crawlers = [
                MGCrawler(),
                TimesLiveCrawler(),
                CitizenCrawler(),
                DailysunCrawler(),
                News24Crawler(),
                IOLCrawler(),
                NamibianCrawler(),
                ZambiaDailyNationCrawler(),
                LusakaTimesCrawler(),
                ZambianWatchdogCrawler(),
                ZambiaDailyMailCrawler(),
                PostZambiaCrawler(),
                # must come last
                GenericCrawler()]
        self.extractors = [
                AlchemyExtractor(),
                CalaisExtractor(),
                SourcesExtractor(),
                PlacesExtractor()]


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
        except HTTPError as e:
            self.log.warn("Error fetching %s: %s" % (url, e), exc_info=e)
            raise ProcessingError("Error fetching document %s: %s" % (url, e))

        try:
            self.process_document(doc)
        except HTTPError as e:
            self.log.warn("Error processing %s: %s" % (url, e), exc_info=e)
            raise ProcessingError("Error processing document %s: %s" % (url, e))

        return doc


    def process_document(self, doc):
        """ Process an existing document. """
        self.normalise(doc)
        self.extract(doc)


    def normalise(self, doc):
        """ Run some normalisations on the document. """
        doc.normalise_text()

        if not doc.document_type:
            doc.document_type = DocumentType.query.filter(DocumentType.name == 'News story').one()

        if not doc.fairness:
            df = DocumentFairness()
            df.fairness = Fairness.query.filter(Fairness.name == 'Fair').one()
            doc.fairness.append(df)


    def crawl(self, doc):
        """ Run crawlers against a document's URL to fetch its
        content, updating any existing content. """
        for crawler in self.crawlers:
            if crawler.offer(doc.url):
                crawler.crawl(doc)
                return


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


    def fetch_daily_feed_items(self, day):
        """ Fetch the feed for +day+ and yields the items. """
        tree = self.fetch_daily_feeds(day)

        items = tree.findall('channel/item')
        self.log.info("Got %d items from feeds for %s" % (len(items), day))

        for item in items:
            # <item>
            #    <url>http://citizen.co.za/afp_feed_article/yankees-pay-tribute-to-retiring-captain-jeter</url>
            #    <publisher>Citizen</publisher>
            #    <contenttype>news</contenttype>
            #    <contenttypeverified>false</contenttypeverified>
            #    <publishdate>2014-09-07 23:51:00</publishdate>
            #    <crawldate>2014-09-08 00:03:47</crawldate>
            #    <title>Yankees pay tribute to retiring captain Jeter</title>
            #    <author>Unknown</author>
            #    <text>https://www.newstools.co.za/data/texts/SFM-7IVZ63RG1MZ2XZF4OTTC.txt</text>
            # </item>

            item = {
                    'url': item.find('url').text,
                    'publishdate': item.find('publishdate').text,
                    'title': item.find('title').text,
                    'author': item.find('author').text,
                    'text_url': item.find('text').text,
            }
            yield item


    def process_feed_item(self, item):
        """ Process an item pulled from an RSS feed.

        This checks to see if the document's URL already exists in the database.
        If not, download the text for the URL and run processing on it, then
        store it in the database. This commits the current transaction.

        Returns the resulting document or None if the document already exists.
        """
        try:
            self.log.info("Processing feed item: %s" % item)
            url = item['url'] = self.canonicalise_url(item['url'])

            existing = Document.query.filter(Document.url == url).first()
            if existing:
                self.log.info("URL has already been processed, ignoring: %s" % url)
                return None

            if not self.newstools_crawler.offer(url):
                self.log.info("No medium for URL, ignoring: %s" % url)
                return

            try:
                doc = self.newstools_crawler.crawl(item)
            except HTTPError as e:
                self.log.error("Error fetching document: %s" % e, exc_info=e)
                raise ProcessingError("Error fetching document: %s" % (e,))

            # is it sane?
            if not doc.text or not 'the' in doc.text:
                self.log.info("Document %s doesn't have reasonable-looking text, ignoring: %s..." % (url, doc.text[0:100]))
                db.session.rollback()
                return None

            doc.analysis_nature = AnalysisNature.query.get(AnalysisNature.ANCHOR)
            self.process_document(doc)

            # only add a document if it has sources or utterances
            if doc.sources or doc.utterances:
                db.session.add(doc)
            else:
                self.log.info("Document has no sources or utterances, ignoring: %s" % url)

            db.session.commit()
            self.log.info("Successfully processed feed item: %s" % url)
            return doc
        except:
            db.session.rollback()
            raise


    def fetch_daily_feeds(self, day):
        """ Fetch the feed for +day+ and returns an ElementTree instance. """
        import xml.etree.ElementTree as ET

        if self.FEED_PASSWORD is None:
            raise ValueError("%s.FEED_PASSWORD must be set." % self.__class__.__name__)

        r =  requests.get(self.FEED_URL % day.strftime('%d-%m-%Y'),
                          auth=(self.FEED_USER, self.FEED_PASSWORD),
                          verify=False,
                          timeout=60)
        r.raise_for_status()

        return ET.fromstring(r.text)
