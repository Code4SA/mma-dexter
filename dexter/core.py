import logging
import os
import sys

from .app import app
from .admin import admin

# load admin interface
from dexter.admin.admin import admin_instance
admin_instance.init_app(app)

import dexter.assets

# setup extraction
from .processing.extractors.alchemy import AlchemyExtractor
from .processing.extractors.calais import CalaisExtractor
AlchemyExtractor.API_KEY = app.config.get('ALCHEMY_API_KEY')
CalaisExtractor.API_KEY = app.config.get('CALAIS_API_KEY')
