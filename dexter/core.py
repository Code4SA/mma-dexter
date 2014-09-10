from .app import app

# load admin interface
from dexter.admin.admin import admin_instance
admin_instance.init_app(app)

import dexter.assets
import dexter.routes
