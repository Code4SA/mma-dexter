from urlparse import urlparse, urlunparse
import re

from bs4 import BeautifulSoup
import requests

from .base import BaseCrawler
from ...models import Entity, Author, AuthorType

class NationalMirrorCrawler(BaseCrawler):
	NM_RE = re.compile('(www\.)?nationalmirroronline.net')

	def offer(self, url):
		""" Can this crawler process this URL? """
		parts = urlparse(url)
		return bool(self.NM_RE.match(parts.netloc))

	def canonicalise_url(self, url):
		""" Strip anchors, etc."""

		# Needed to handle urls being recieved without protocol (http[s]://), check if it can be parsed first, then handle and re parse if there is no netloc found
		if '//' not in url:
			url = '%s%s' % ('https://', url)

		parts = urlparse(url)

		netloc = parts.netloc.strip(':80')

		# force http, strip trailing slash, anchors etc.
		return urlunparse(['https', netloc, parts.path.rstrip('/') or '/', parts.params, parts.query, None])

	def extract(self, doc, raw_html):
		""" Extract text and other things from the raw_html for this document. """
		super(NationalMirrorCrawler, self).extract(doc, raw_html)

		soup = BeautifulSoup(raw_html)

		# gather title
		doc.title = self.extract_plaintext(soup.select('#primary .post .entry-header .entry-title'))

		#gather publish date
		date = self.extract_plaintext(soup.select('#primary .post .entry-header .entry-meta .entry-date'))
		doc.published_at = self.parse_timestamp(date)

		#gather text and summary
		nodes = soup.select('#primary .post .entry-content p')
		doc.summary = "\n\n".join(p.text.strip() for p in nodes[:1])
		doc.text = "\n\n".join(p.text.strip() for p in nodes)

		# gather author 
		doc.author = Author.unknown()