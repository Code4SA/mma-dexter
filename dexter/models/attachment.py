import datetime
import io
from cStringIO import StringIO

from sqlalchemy import (
    Table,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
    Index,
    )
from sqlalchemy.orm import relationship, backref
from sqlalchemy_imageattach.entity import Image, image_attachment
from werkzeug.utils import secure_filename
from wand.image import Image as WandImage

from .support import db


import logging

# mimetypes we accept
MIMETYPES = set("image/png image/jpeg image/gif application/pdf".split())


class DocumentAttachment(db.Model):
    """
    An attachment for a document.

    Some attachments might not be associated with a document. This happens when a new
    document is being added and we don't yet have a document id. When the document is
    fully created the attachment ids will be included in the request and linked to the
    document.
    
    We'll clean up stranded attachments periodically.
    """
    __tablename__ = "attachments"
    log = logging.getLogger(__name__)

    id        = Column(Integer, primary_key=True)

    filename  = Column(String(256), nullable=False)
    document_id = Column(Integer, ForeignKey('documents.id'), index=True)

    created_by_user_id = Column(Integer, ForeignKey('users.id'), index=True)

    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # Associations
    document    = relationship("Document")
    created_by  = relationship("User", foreign_keys=[created_by_user_id])
    image       = image_attachment("AttachmentImage")


    THUMBNAIL_WIDTH = 100

    def generate_thumbnails(self):
        self.image.generate_thumbnail(width=self.THUMBNAIL_WIDTH)

    @classmethod
    def is_acceptable(cls, upload):
        """
        Is this `werkzeug.FileStorage` object a valid upload?
        """
        return upload.mimetype in MIMETYPES

    @classmethod
    def from_upload(cls, upload, user=None, document=None):
        """
        Create a new attachment from an uploaded file, a `werkzeug.FileStorage` object.
        """

        attachment = DocumentAttachment()
        attachment.document = document
        attachment.filename = secure_filename(upload.filename)
        if user and user.is_authenticated():
            attachment.created_by = user

        if upload.mimetype == "application/pdf":
            # TODO: save pdf to s3

            # convert to an image
            with WandImage(file=upload, resolution=300) as img:
                img.format = 'png'
                upload = StringIO()
                img.save(file=upload)
                upload.seek(0)

        # store attachment and thumbnails
        attachment.image.from_file(upload)
        attachment.generate_thumbnails()

        return attachment
        

class AttachmentImage(db.Model, Image):
    __tablename__ = "attachment_images"

    id            = Column(Integer, primary_key=True)
    width         = Column('width', Integer)
    height        = Column('height', Integer)
    attachment_id = Column(Integer, ForeignKey('attachments.id'), index=True)

Index('attachment_images_w_h_id_ix', AttachmentImage.width, AttachmentImage.height, AttachmentImage.attachment_id, unique=True)
