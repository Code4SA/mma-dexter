from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup

from .base import BaseCrawler
from ...models import Author, AuthorType

class ZambiaDailyNationCrawler(BaseCrawler):
    TL_RE = re.compile('(www\.)?zambiadailynation.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TL_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(ZambiaDailyNationCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        doc.title = self.extract_plaintext(soup.select(".post-alt h2 a"))
    
        # there are multiple divs with this id
        nodes = soup.select(".post-alt .entry p")
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        text = self.extract_plaintext(soup.select(".post-alt .post_date"))
        text = text.replace('Posted on ', '').replace('.', '')
        doc.published_at = self.parse_timestamp(text)

        doc.author = Author.unknown()


class TimesZambiaCrawler(BaseCrawler):
    TL_RE = re.compile('(www\.)?times.co.zm')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TL_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(TimesZambiaCrawler, self).extract(doc, raw_html)

        # TODO


class LusakaTimesCrawler(BaseCrawler):
    TL_RE = re.compile('(www\.)?lusakatimes.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TL_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(LusakaTimesCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        doc.title = self.extract_plaintext(soup.select("article.post .entry-title"))
    
        # there are multiple divs with this id
        nodes = soup.select("article.post .entry-content p")
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        doc.published_at = self.parse_timestamp(soup.select("article.post time.entry-published")[0]['datetime']).date()

        doc.author = Author.unknown()


class ZambianWatchdogCrawler(BaseCrawler):
    TL_RE = re.compile('(www\.)?zambianwatchdog.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TL_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(ZambianWatchdogCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        doc.title = self.extract_plaintext(soup.select(".post-lead .post-title"))
    
        # there are multiple divs with this id
        nodes = soup.select("article.post p")
        # ignore p tags with weird parents
        nodes = [p for p in nodes if not p.find_parents('div', id='comments')]
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        doc.published_at = self.parse_timestamp(soup.select('meta[property="article:published_time"]')[0]['content']).date()

        doc.author = Author.unknown()


class ZambiaDailyMailCrawler(BaseCrawler):
    TL_RE = re.compile('(www\.)?daily-mail.co.zm')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TL_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(ZambiaDailyMailCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        doc.title = soup.select('meta[property="og:title"]')[0]['content'].replace(' - Zambia Daily Mail', '')
    
        # there are multiple divs with this id
        nodes = soup.select("article.post .entry-content p")
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        doc.published_at = self.parse_timestamp(soup.select('meta[property="article:published_time"]')[0]['content']).date()

        doc.author = Author.unknown()


class PostZambiaCrawler(BaseCrawler):
    TL_RE = re.compile('(www\.)?postzambia.com')

    def offer(self, url):
        """ Can this crawler process this URL? """
        parts = urlparse(url)
        return bool(self.TL_RE.match(parts.netloc))

    def extract(self, doc, raw_html):
        """ Extract text and other things from the raw_html for this document. """
        super(PostZambiaCrawler, self).extract(doc, raw_html)

        soup = BeautifulSoup(raw_html)

        doc.title = self.extract_plaintext(soup.select('td[height=52]'))
    
        # there are multiple divs with this id
        nodes = soup.select(".newsbody p")
        doc.text = "\n\n".join(p.text.strip() for p in nodes)

        text = self.extract_plaintext(soup.select('td[height=30]'))
        text = ' '.join(text.split("pdated:", 1)[1].split("|")[0].split(",", 2)[0:2])
        doc.published_at = self.parse_timestamp(text)

        author = self.extract_plaintext(soup.select('td[height=30] strong')).strip()
        if author:
            doc.author = Author.get_or_create(author, AuthorType.journalist())
        else:
            doc.author = Author.unknown()
