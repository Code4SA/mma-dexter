import re
import md5
import os
import json
import gzip

import logging
log = logging.getLogger(__name__)

class BaseExtractor:
    def normalise_name(self, name):
        return re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()

    def check_cache(self, url, key):
        """ See if we have a cached response for this URL and this key."""
        fname = self.cache_filename(url, key)
        if not os.path.isfile(fname):
            log.info("Cache miss: %s" % fname)
            return None

        try:
            log.info('Cache hit: %s' % fname)
            with gzip.open(fname) as f:
                return json.load(f)
        except ValueError as e:
            log.warn("Error reading from cache file %s: %s" % (fname, e.message), exc_info=e)
            return None


    def update_cache(self, url, key, value):
        """ Cache a response for this URL and this key. """
        fname = self.cache_filename(url, key)

        dirname = os.path.dirname(fname)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        with gzip.open(fname, 'wb') as f:
            json.dump(value, f)
    
    def cache_filename(self, url, key):
        hashed = '%s.%s.json.gz' % (self.hash_url(url), key)
        return 'cache/extractors/%s/%s' % (hashed[0:2], hashed)

    def hash_url(self, url):
        return md5.md5(url).hexdigest()

