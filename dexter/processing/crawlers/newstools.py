from urlparse import urlparse
import HTMLParser
import requests
from dateutil.parser import parse
import re
import unidecode
from .base import BaseCrawler
from ...models import Author, AuthorType, Medium, Document


class NewstoolsCrawler(BaseCrawler):
    # ignore URLs that start with these paths
    ignore_paths = [
        # ignore citizen AFP articles
        '/afp_feed_article',
        '/sports/',
        '/sport/',
        # ignore news24, IOL world articles
        '/news/world/',
        '/world/',
        # iol intl business
        '/business/international/',
        # these aren't in English
        '/isolezwe/',
    ]

    def offer(self, url):
        """ Can this crawler process this URL?
        We only allow urls we have a medium for. """
        m = Medium.for_url(url)
        if m is None:
            return False

        parts = urlparse(url.lower())

        if any(parts.path.startswith(p) for p in self.ignore_paths):
            return False

        # ignore citypress non-articles
        if m.domain == 'citypress.co.za':
            for prefix in ['/category/', '/author/', '/entertainment/', '/lifestyle/']:
                if parts.path.startswith(prefix):
                    return False

        return True

    def crawl(self, item):
        """ Create a document from this newstools feed item.
        This doesn't actually fetch the text, we prefer to do that ourselves.
        """
        doc = Document()
        doc.url = item['url']
        doc.title = item['title']
        doc.published_at = parse(item['publishdate'])

        if item['author'] and item['author'].lower() != 'unknown':
            doc.author = Author.get_or_create(item['author'], AuthorType.journalist())
        else:
            doc.author = Author.unknown()

        # medium and country
        self.extract(doc, None)

        return doc

    def fetch_text(self, url):
        r = requests.get(url, verify=False, timeout=60)
        r.raise_for_status()
        return self.unescape(r.text)

    def unescape(self, text):
        html_parser = HTMLParser.HTMLParser()
        return html_parser.unescape(text)


class NewstoolsCrawlerNT(BaseCrawler):
    # New crawler to shift daily feed responsibilities to Newstools (NT)
    # Media-specific crawlers will only be leveraged for manual URL additions

    # ignore URLs that start with these paths
    ignore_paths = [
        # ignore citizen AFP articles
        '/afp_feed_article',
        '/sports/',
        '/sport/',
        '/Sport/'
        # ignore news24, IOL world articles
        '/news/world/',
        '/world/',
        # iol intl business
        '/business/international/',
        # these aren't in English
        '/isolezwe/',
    ]

    def offer(self, url):
        """ Can this crawler process this URL?
        We only allow urls we have a medium for. """
        m = Medium.for_url(url)
        if m is None:
            return False


        parts = urlparse(url.lower())

        if any(parts.path.startswith(p) for p in self.ignore_paths):
            return False

        # ignore citypress non-articles
        if m.domain == 'citypress.co.za':
            for prefix in ['/category/', '/author/', '/entertainment/', '/lifestyle/']:
                if parts.path.startswith(prefix):
                    return False

        return True

    def extract(self, doc, raw_html):
        """ Run extractions on the HTML. Subclasses should override this
        method and call super() in their implementations. """
        doc.medium = self.identify_medium(doc)
        doc.country = doc.medium.country

    def crawl(self, item):
        """ Create a document from this newstools feed item.
        This new crawler now handles all aspects of injection into Dexter, rather than using individual crawlers for
        each medium.
        Individual crawlers are used for processing of manually added URLs.
        """
        doc = Document()
        doc.url = item['url']
        title = str(unidecode.unidecode(HTMLParser.HTMLParser().unescape(item['title'])))
        doc.title = title.replace("aEUR(tm)", "'").replace("aEUR~", "'").replace('aEUR"', '-').replace('aEURs', ',')\
            .replace('aEUR<', '')
        doc.published_at = parse(item['publishdate'])

        if item['author'] and item['author'].lower() != 'unknown':
            doc.author = Author.get_or_create(item['author'], AuthorType.journalist())
        else:
            doc.author = Author.unknown()

        # medium and country
        self.extract(doc, None)

        text_url = item['text_url']
        r_s = requests.get(text_url)
        s = str(unidecode.unidecode(HTMLParser.HTMLParser().unescape(r_s.text)))
        doc.text = re.sub(' +', ' ', s)

        return doc

    def fetch_text(self, url):
        r = requests.get(url, verify=False, timeout=60)
        r.raise_for_status()
        return self.unescape(r.text)

    def unescape(self, text):
        html_parser = HTMLParser.HTMLParser()
        return html_parser.unescape(text)
