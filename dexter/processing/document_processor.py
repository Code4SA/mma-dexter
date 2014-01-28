from ..models import Document

from .crawlers import MGCrawler

class DocumentProcessor:
    def __init__(self):
        self.crawlers = [MGCrawler()]
        self.extractors = [] #[AlchemyExtractor()]


    def valid_url(self, url):
        """ Is this a URL we can process? """
        return any(c.offer(url) for c in self.crawlers)


    def canonicalise_url(self, url):
        """ Try to canonicalise this url. Strip anchors, etc. """
        for crawler in self.crawlers:
            if crawler.offer(url):
                return crawler.canonicalise_url(url)

        return url


    def process(self, url):
        """ Downloand and process an article at +url+ and return
        a Document instance. """
        doc = Document()
        doc.url = url

        self.crawl(doc)
        self.extract(doc)

        return doc

    def crawl(self, doc):
        """ Run crawlers against a document's URL to fetch its
        content, updating any existing content. """
        for crawler in self.crawlers:
            if crawler.offer(doc.url):
                crawler.crawl(doc)


    def extract(self, doc):
        """ Run extraction routines on a document. """
