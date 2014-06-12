import unittest

from dexter.attachments import HttpExposedFileSystemStore, S3Store

class TestAttachments(unittest.TestCase):
    def test_s3_path(self):
        store = S3Store('foo', 'a', 'b', prefix='p')

        self.assertEquals(store.get_key("attachment", "1/foo.pdf", 0, 0, 'application/pdf'), "p/attachment/1/foo.pdf")
        self.assertEquals(store.get_key("attachment", 5, 10, 50, 'image/png'), "p/attachment/5/10x50.png")

    def test_fs_path(self):
        store = HttpExposedFileSystemStore('foo', '/prefix')

        self.assertEquals(':'.join(store.get_path("attachment", "1/foo.pdf", 0, 0, 'application/pdf')),
            "attachment:1:0:1.0x0.pdf")
