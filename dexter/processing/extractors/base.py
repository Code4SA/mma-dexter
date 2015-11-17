import re
import md5

import logging
log = logging.getLogger(__name__)


class BaseExtractor:
    def normalise_name(self, name):
        return re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()

    def hash_url(self, url):
        return md5.md5(url).hexdigest()
