import tempfile
import logging

from flask.ext.uploads import patch_request_class

from sqlalchemy_imageattach.context import (pop_store_context, push_store_context)
from sqlalchemy_imageattach.stores.fs import HttpExposedFileSystemStore
from sqlalchemy_imageattach.stores.s3 import S3Store

log = logging.getLogger(__name__)

pushed = False

def setup_attachments(app):
    # max upload size
    patch_request_class(app, 6 * 1024 * 1024)

    # attachment store
    store = setup_store(app)

    # link attachment store implicitly to the request chain
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

def setup_store(app):
    # setup the file storage for image attachments
    store_type = app.config.get('ATTACHMENT_STORE', 'disk')

    if store_type == "s3":
        # use S3
        bucket = app.config['ATTACHMENT_S3_BUCKET']
        prefix = app.config.get('ATTACHMENT_S3_PREFIX', '')

        log.info("Storing attachments in S3 at %s/%s" % (bucket, prefix))

        store = S3Store(bucket,
                app.config['AWS_S3_ACCESS_KEY'],
                app.config['AWS_S3_SECRET_KEY'],
                prefix=prefix)

    elif store_type == "disk":
        # TODO: handle testing
        path = '/tmp/dexter-attachments'
        try:
            os.makedirs(path)
        except:
            pass
        log.info("Storing attachments in %s" % path)
        store = HttpExposedFileSystemStore(path, '/static-attachments/')
        app.wsgi_app = store.wsgi_middleware(app.wsgi_app)

    else:
      raise ValueError("Attachment store type should be one of 'disk' or 's3', not '%s'" % store_type)

    return store
