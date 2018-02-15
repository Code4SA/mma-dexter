import time
import logging

import requests
from requests.exceptions import HTTPError
from sqlalchemy.sql import desc

from ..models import Document, db, DocumentType, DocumentFairness, Fairness, AnalysisNature, DocumentTaxonomy
from ..processing import ProcessingError

from .crawlers import *  # noqa
from .extractors import AlchemyExtractor, CalaisExtractor, SourcesExtractor, PlacesExtractor


class DocumentProcessor:
    log = logging.getLogger(__name__)

    # FEED_URL = 'https://www.newstools.co.za/newstoolspider/index.php/dexter/articles/%s'
    FEED_URL = 'http://newstools.co.za/dexter/articles/%s'
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
            TimesZambiaCrawler(),
            NationKECrawler(),
            StandardMediaCrawler(),
            TheStarKECrawler(),
            TheEastAfricanKECrawler(),
            DailyNewsTZCrawler(),
            DailyNewsZWCrawler(),
            TheCitizenTZCrawler(),
            NewsDayZWCrawler(),
            DWCrawler(),
            ChronicleZWCrawler(),
            BBCCrawler(),
            HowWeMadeItInAfricaCrawler(),
            SAVCACrawler(),
            RhodesUniMathewBlogCrawler(),
            WorldStageCrawler(),
            ClassicFMCrawler(),
            AFPCrawler(),
            NaijaNewsCrawler(),
            DailyTrustNPCrawler(),
            NewTeleOnlineCrawler(),
            ThePointCrawler(),
            DailyTimesCrawler(),
            TheNationCrawler(),
            MediaMaxNetCrawler(),
            LeadershipCrawler(),
            TheInterviewCrawler(),
            RSAParliamentCrawler(),
            GuardianCrawler(),
            NationalDailyNgCrawler(),
            NTACrawler(),
            ACDIVOCACrawler(),
            ThisDayLiveCrawler(),
            ChannelAfricaCrawler(),
            NANCrawler(),
            NigeriaTodayCrawler(),
            BusinessDayOnlineCrawler(),
            # must come last
            GenericCrawler()]
        self.extractors = [
            # AlchemyExtractor(),
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
            if not url:
                self.log.info("URL could not be parsed, ignoring: %s" % url)
                return None

            existing = Document.query.filter(Document.url == url).first()
            if existing:
                self.log.info("URL has already been processed, ignoring: %s" % url)
                return None

            if not self.newstools_crawler.offer(url):
                self.log.info("No medium for URL, ignoring: %s" % url)
                return

            # this sets up basic info
            doc = self.newstools_crawler.crawl(item)
            try:
                # get the raw details
                self.crawl(doc)
            except HTTPError as e:
                self.log.error("Error fetching document: %s" % e, exc_info=e)
                raise ProcessingError("Error fetching document: %s" % (e,))

            # is it sane?
            # TODO: this breaks for isolezwe and other non-english media'
            if not doc.text or 'the' not in doc.text:
                self.log.info("Document %s doesn't have reasonable-looking text, ignoring: %s..." % (url, doc.text[0:100]))
                db.session.rollback()
                return None

            doc.analysis_nature = AnalysisNature.lookup(AnalysisNature.ANCHOR)
            self.process_document(doc)

            # only add a document if it has sources or utterances
            if doc.sources or doc.utterances:
                db.session.add(doc)
                db.session.commit()
                self.log.info("Successfully processed feed item: %s as document %d" % (url, doc.id))
                return doc
            else:
                db.session.rollback()
                self.log.info("Document has no sources or utterances, ignoring: %s" % url)
                return None

        except:
            db.session.rollback()
            raise

    def fetch_daily_feeds(self, day):
        """ Fetch the feed for +day+ and returns an ElementTree instance. """
        # import xml.etree.ElementTree as ET

        from xml.etree import ElementTree
        from htmlentitydefs import name2codepoint

        if self.FEED_PASSWORD is None:
            raise ValueError("%s.FEED_PASSWORD must be set." % self.__class__.__name__)

        # r = requests.get(self.FEED_URL % day.strftime('%d-%m-%Y'),
        #                  auth=(self.FEED_USER, self.FEED_PASSWORD),
        #                  verify=False,
        #                  timeout=60)

        payload = {'PHP_AUTH_USER': self.FEED_USER, 'PHP_AUTH_PW': self.FEED_PASSWORD}

        r = requests.get(self.FEED_URL % day.strftime('%d-%m-%Y'),
                         headers=payload,
                         verify=False,
                         timeout=60)

        r.raise_for_status()

        parser = ElementTree.XMLParser()
        parser.parser.UseForeignDTD(True)
        parser.entity.update((x, unichr(i)) for x, i in name2codepoint.iteritems())
        etree = ElementTree

        return etree.fromstring(r.text.encode('utf-8'), parser=parser)

    def backfill_taxonomies(self):
        """ Backfill taxonomies for articles.
        """
        doc_ids = (db.session
                   .query(Document.id)
                   .join(DocumentTaxonomy, isouter=True)
                   .filter(DocumentTaxonomy.doc_id == None)
                   .filter(Document.raw_calais == None)
                   .filter(Document.text != None, Document.text != '')
                   .order_by(desc(Document.published_at))
                   .all()
        )  # noqa

        count = 0
        self.log.info("Starting taxonomy backfill for %s documents" % len(doc_ids))

        try:
            for doc_id in doc_ids:
                doc = Document.query.get(doc_id)
                if not doc.text.strip():
                    continue

                try:
                    self.backfill_taxonomies_for_document(doc)
                    count += 1
                except HTTPError as e:
                    if 'requests per day' in e.response.text:
                        # we're done for the day
                        self.log.info("Exceeded OpenCalais quota for the day, stopping: %s" % e.message)
                        break

                    elif e.response.status_code == 429:
                        # per-minute quota exceeded, try again later
                        self.log.info("Temporary failure for %s: %s" % (doc, e.message))
                        time.sleep(60)

                    else:
                        self.log.info("Error backfilling for %s: %s" % (doc, e.message), exc_info=e)

        finally:
            self.log.info("Backfilled %d documents" % count)

    def backfill_taxonomies_for_document(self, doc):
        from dexter.app import app
        self.log.info("Backfilling taxonomies for %s" % doc)

        cx = CalaisExtractor()
        cx.API_KEY = app.config['CALAIS_API_KEY2']
        calais = cx.fetch_data(doc)
        cx.extract_topics(doc, calais)

        db.session.commit()


class DocumentProcessorNT:
    log = logging.getLogger(__name__)

    FEED_URL = 'http://newstools.co.za/dexter/articles/%s'
    FEED_USER = 'dexter'
    FEED_PASSWORD = None

    def __init__(self):
        self.newstools_crawler = NewstoolsCrawlerNT()

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
            TimesZambiaCrawler(),
            NationKECrawler(),
            StandardMediaCrawler(),
            TheStarKECrawler(),
            TheEastAfricanKECrawler(),
            DailyNewsTZCrawler(),
            DailyNewsZWCrawler(),
            TheCitizenTZCrawler(),
            NewsDayZWCrawler(),
            DWCrawler(),
            ChronicleZWCrawler(),
            BBCCrawler(),
            HowWeMadeItInAfricaCrawler(),
            SAVCACrawler(),
            RhodesUniMathewBlogCrawler(),
            WorldStageCrawler(),
            ClassicFMCrawler(),
            AFPCrawler(),
            NaijaNewsCrawler(),
            DailyTrustNPCrawler(),
            NewTeleOnlineCrawler(),
            ThePointCrawler(),
            DailyTimesCrawler(),
            TheNationCrawler(),
            MediaMaxNetCrawler(),
            LeadershipCrawler(),
            TheInterviewCrawler(),
            RSAParliamentCrawler(),
            GuardianCrawler(),
            NationalDailyNgCrawler(),
            NTACrawler(),
            ACDIVOCACrawler(),
            ThisDayLiveCrawler(),
            ChannelAfricaCrawler(),
            NANCrawler(),
            NigeriaTodayCrawler(),
            BusinessDayOnlineCrawler(),
            # must come last
            GenericCrawler()]

        self.extractors = [
            AlchemyExtractor(),
            CalaisExtractor(),
            SourcesExtractor(),
            PlacesExtractor()]

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

    def canonicalise_url(self, url):
        """ Try to canonicalise this url. Strip anchors, etc. """
        for crawler in self.crawlers:
            if crawler.offer(url):
                return crawler.canonicalise_url(url)

        return url

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
        NewstoolsCrawlerNT.crawl(self.newstools_crawler, doc)
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
            if not url:
                self.log.info("URL could not be parsed, ignoring: %s" % url)
                return None

            existing = Document.query.filter(Document.url == url).first()
            if existing:
                self.log.info("URL has already been processed, ignoring: %s" % url)
                return None

            if not self.newstools_crawler.offer(url):
                self.log.info("No medium for URL, ignoring: %s" % url)
                return

            # this sets up basic info
            try:
                doc = self.newstools_crawler.crawl(item)
            except Exception as e:
                self.log.error("Error fetching document: %s" % e, exc_info=e)
                raise ProcessingError("Error fetching document: %s" % (e,))

            # try:
            #     # get the raw details
            #     self.crawl(doc)
            # except HTTPError as e:
            #     self.log.error("Error fetching document: %s" % e, exc_info=e)
            #     raise ProcessingError("Error fetching document: %s" % (e,))

            # is it sane?
            # TODO: this breaks for isolezwe and other non-english media
            if not doc.text or 'the' not in doc.text:
                self.log.info("Document %s doesn't have reasonable-looking text, ignoring: %s..." % (url, doc.text[0:100]))
                db.session.rollback()
                return None

            doc.analysis_nature = AnalysisNature.lookup(AnalysisNature.ANCHOR)
            self.process_document(doc)

            # only add a document if it has sources or utterances
            if doc.sources or doc.utterances:
                db.session.add(doc)
                db.session.commit()
                self.log.info("Successfully processed feed item: %s as document %d" % (url, doc.id))
                return doc
            else:
                db.session.rollback()
                self.log.info("Document has no sources or utterances, ignoring: %s" % url)
                return None

        except:
            db.session.rollback()
            raise

    def fetch_daily_feeds(self, day):
        """ Fetch the feed for +day+ and returns an ElementTree instance. """
        # import xml.etree.ElementTree as ET

        from xml.etree import ElementTree
        from htmlentitydefs import name2codepoint

        if self.FEED_PASSWORD is None:
            raise ValueError("%s.FEED_PASSWORD must be set." % self.__class__.__name__)

        r = requests.get(self.FEED_URL % day.strftime('%d-%m-%Y'),
                         auth=(self.FEED_USER, self.FEED_PASSWORD),
                         verify=False,
                         timeout=60)

        r.raise_for_status()

        parser = ElementTree.XMLParser()
        parser.parser.UseForeignDTD(True)
        parser.entity.update((x, unichr(i)) for x, i in name2codepoint.iteritems())
        etree = ElementTree

        return etree.fromstring(r.text.encode('utf-8'), parser=parser)

    def backfill_taxonomies(self):
        """ Backfill taxonomies for articles.
        """
        doc_ids = (db.session
                   .query(Document.id)
                   .join(DocumentTaxonomy, isouter=True)
                   .filter(DocumentTaxonomy.doc_id == None)
                   .filter(Document.raw_calais == None)
                   .filter(Document.text != None, Document.text != '')
                   .order_by(desc(Document.published_at))
                   .all()
        )  # noqa

        count = 0
        self.log.info("Starting taxonomy backfill for %s documents" % len(doc_ids))

        try:
            for doc_id in doc_ids:
                doc = Document.query.get(doc_id)
                if not doc.text.strip():
                    continue

                try:
                    self.backfill_taxonomies_for_document(doc)
                    count += 1
                except HTTPError as e:
                    if 'requests per day' in e.response.text:
                        # we're done for the day
                        self.log.info("Exceeded OpenCalais quota for the day, stopping: %s" % e.message)
                        break

                    elif e.response.status_code == 429:
                        # per-minute quota exceeded, try again later
                        self.log.info("Temporary failure for %s: %s" % (doc, e.message))
                        time.sleep(60)

                    else:
                        self.log.info("Error backfilling for %s: %s" % (doc, e.message), exc_info=e)

        finally:
            self.log.info("Backfilled %d documents" % count)

    def backfill_taxonomies_for_document(self, doc):
        from dexter.app import app
        self.log.info("Backfilling taxonomies for %s" % doc)

        cx = CalaisExtractor()
        cx.API_KEY = app.config['CALAIS_API_KEY2']
        calais = cx.fetch_data(doc)
        cx.extract_topics(doc, calais)

        db.session.commit()

