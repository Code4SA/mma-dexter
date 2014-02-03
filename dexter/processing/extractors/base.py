import re

class BaseExtractor:
    def normalise_name(self, name):
        return re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()
