import unittest
import datetime

from werkzeug.datastructures import FileStorage

from dexter.attachments import HttpExposedFileSystemStore, S3Store
from dexter.models import Document, DocumentAttachment, AttachmentImage

from dexter.models.support import db
from dexter.models.seeds import seed_db


class TestAttachments(unittest.TestCase):
    def setUp(self):
        self.db = db
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_s3_path(self):
        store = S3Store('foo', 'a', 'b', prefix='p')

        self.assertEquals(store.get_key("attachment", "1/foo.pdf", 0, 0, 'application/pdf'), "p/attachment/1/foo.pdf")
        self.assertEquals(store.get_key("attachment", 5, 10, 50, 'image/png'), "p/attachment/5/10x50.png")

    def test_fs_path(self):
        store = HttpExposedFileSystemStore('foo', '/prefix')

        self.assertEquals(':'.join(store.get_path("attachment", "1/foo.pdf", 0, 0, 'application/pdf')),
            "attachment:1:0:1.0x0.pdf")

    def test_delete_attachments(self):
        doc = Document()
        doc.url = "url"
        doc.published_at = datetime.datetime.now()
        db.session.add(doc)
        db.session.commit()

        with open("tests/fixtures/smiley.png") as f:
            upload = FileStorage(f, 'smiley.png', name='file', content_type='image/png')
            attachment = DocumentAttachment.from_upload(upload, None)
            attachment.document = doc
            db.session.commit()
            self.assertEqual('image/png', attachment.image.original.mimetype)

        doc = Document.query.get(doc.id)
        x = list(doc.attachments)
        for att in x:
          for y in att.image:
            print 1
          #print [1 for t in att.image]
          pass

        self.assertEqual(1, len(doc.attachments))
        doc.attachments = []

        db.session.commit()

        self.assertEqual(0, len(doc.attachments))
