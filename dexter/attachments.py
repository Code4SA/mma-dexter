import tempfile
import logging

from flask.ext.uploads import patch_request_class

from sqlalchemy_imageattach.context import (pop_store_context, push_store_context)
from sqlalchemy_imageattach.stores.fs import HttpExposedFileSystemStore

log = logging.getLogger(__name__)

pushed = False

def setup_attachments(app):
    # max upload size
    patch_request_class(app, 6 * 1024 * 1024)

    # setup the file storage for image attachments
    # TODO: handle testing
    path = '/tmp/dexter-attachments'
    try:
        os.makedirs(path)
    except:
        pass
    log.info("Storing attachments in %s" % path)
    # TODO: production
    store = HttpExposedFileSystemStore(path, '/static-attachments/')
    app.wsgi_app = store.wsgi_middleware(app.wsgi_app)


    @app.before_request
    def start_implicit_store_context():
        global pushed
        push_store_context(store)
        pushed = True

    @app.teardown_request
    def stop_implicit_store_context(exception=None):
        global pushed
        if pushed:
            pop_store_context()
            pushed = False
