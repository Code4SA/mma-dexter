import logging
import os
import sys

from .app import app

import dexter.assets
import dexter.routes

# setup extraction
from .processing.extractors.alchemy import AlchemyExtractor
from .processing.extractors.calais import CalaisExtractor
AlchemyExtractor.API_KEY = app.config.get('ALCHEMY_API_KEY')
CalaisExtractor.API_KEY = app.config.get('CALAIS_API_KEY')
