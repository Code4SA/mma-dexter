import logging
import os
import sys

from .app import app

import dexter.assets
import dexter.routes

# setup extraction
from .processing.extractors.alchemy import AlchemyExtractor
AlchemyExtractor.API_KEY = app.config.get('ALCHEMY_API_KEY')
