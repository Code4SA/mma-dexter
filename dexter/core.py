from .app import app

# load admin interface
from dexter.admin.admin import admin_instance
admin_instance.init_app(app)

import dexter.assets
import dexter.routes


# setup extraction
from .processing.extractors.alchemy import AlchemyExtractor
from .processing.extractors.calais import CalaisExtractor
AlchemyExtractor.API_KEY = app.config.get('ALCHEMY_API_KEY')
CalaisExtractor.API_KEY = app.config.get('CALAIS_API_KEY')


# setup crawlers
from .processing import DocumentProcessorNT
DocumentProcessorNT.FEED_PASSWORD = app.config.get('NEWSTOOLS_FEED_PASSWORD')
