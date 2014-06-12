import re
import logging
from cStringIO import StringIO

from flask.ext.uploads import patch_request_class

from sqlalchemy_imageattach.context import (pop_store_context, push_store_context)
from sqlalchemy_imageattach.stores.fs import HttpExposedFileSystemStore as BaseHttpExposedFileSystemStore
from sqlalchemy_imageattach.stores.s3 import S3Store as BaseS3Store, DEFAULT_MAX_AGE

from boto.s3.connection import S3Connection, Key, Bucket, S3ResponseError

log = logging.getLogger(__name__)

pushed = False
store = None

def setup_attachments(app):
    # max upload size
    patch_request_class(app, 6 * 1024 * 1024)

    # attachment store
    global store
    store = setup_store(app)

    # set for the current thread, useful for debugging
    push_store_context(store)

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
    push_store_context(store)


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


class S3Store(BaseS3Store):
    NON_IMAGE_RE = re.compile('/0x0\.[a-z0-9]{3,4}$', re.IGNORECASE)

    """
    An attachment store backed by S3, using the boto library.
    This fixes some issues with the original :class:`~sqlalchemy_imageattach.store.s3.S3Store` 
    such as not being able to set the S3 region, controlling ACLs, and following
    redirects.
    """

    #: default seconds a URL is valid for
    DEFAULT_URL_VALIDITY_SECS = 60 * 60 * 24

    def __init__(self, bucket, access_key=None, secret_key=None,
                 max_age=DEFAULT_MAX_AGE, prefix='',
                 acl=None, url_validity_secs=DEFAULT_URL_VALIDITY_SECS,
                 *args, **kwargs):
        super(S3Store, self).__init__(bucket, access_key, secret_key, max_age, prefix, *args, **kwargs)

        self.acl = acl
        self.conn = S3Connection(access_key, secret_key)
        self.bucket = Bucket(self.conn, bucket)
        self.url_validity_secs = url_validity_secs

    def put_file(self, file, object_type, object_id, width, height, mimetype, reproducible):
        key = self.get_key_obj(object_type, object_id, width, height, mimetype)
        self.upload_file(key, file, mimetype, rrs=reproducible)

    def get_file(self, *args, **kwargs):
        fp = StringIO()
        self.get_key_obj(*args, **kwargs).get_contents_to_file(fp)
        fp.seek(0)
        return fp

    def get_url(self, *args, **kwargs):
        key = self.get_key_obj(*args, **kwargs)
        return key.generate_url(self.url_validity_secs)

    def delete_file(self, *args, **kwargs):
        key = self.get_key_obj(*args, **kwargs)
        try:
            key.delete()
        except S3ResponseError as e:
            self.logger.warn("Error deleting %s from S3" % key, exc_info=e)

    def upload_file(self, key, data, content_type, rrs):
        headers = {
            'Cache-Control': 'max-age=' + str(self.max_age),
            'Content-Type': content_type,
        }
        if self.acl:
            headers['x-amz-acl'] = self.acl

        try:
            key.set_contents_from_file(
                    data,
                    headers,
                    reduced_redundancy=rrs)
        except Exception as e:
            self.logger.debug(e)
            raise

    # we override this method so we can hack in support for non-file images
    # eg. foo/bar.pdf/0x0.pdf -> foo/bar.pdf
    def get_key(self, *args, **kwargs):
        key = super(S3Store, self).get_key(*args, **kwargs)

        match = self.NON_IMAGE_RE.search(key)
        if match:
            key = key[:match.start()]

        return key

    def get_key_obj(self, *args, **kwargs):
        return Key(self.bucket, self.get_key(*args, **kwargs))


class HttpExposedFileSystemStore(BaseHttpExposedFileSystemStore):
    # we override this method so we can hack in support for non-file images
    def get_path(self, object_type, object_id, *args, **kwargs):
        if isinstance(object_id, basestring):
            if '/' in object_id:
                object_id = int(object_id.split('/')[0])

        return super(HttpExposedFileSystemStore, self).get_path(object_type, object_id, *args, **kwargs)
