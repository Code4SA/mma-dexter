from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
    )

import logging
log = logging.getLogger(__name__)

from flask.ext.login import UserMixin

from passlib.hash import sha256_crypt

from .support import db
from wtforms import StringField, validators, PasswordField
from wtforms.fields.html5 import EmailField
from ..forms import Form

class User(db.Model, UserMixin):
    """
    A user who can login and work with Dexter.
    """
    __tablename__ = "users"

    id          = Column(Integer, primary_key=True)
    email       = Column(String(50), index=True, nullable=False, unique=True)
    admin       = Column(Boolean, default=False)
    encrypted_password = Column(String(100))

    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    def get_password(self):
        return None

    def set_password(self, password):
        self.encrypted_password = sha256_crypt.encrypt(password)

    password = property(get_password, set_password)


    @classmethod
    def get_and_authenticate(cls, email, password):
        user = cls.query.filter(User.email == email).first()
        if user and sha256_crypt.verify(password, user.encrypted_password):
            return user

        return None


class LoginForm(Form):
    email       = EmailField('Email', [validators.Required()])
    password    = PasswordField('Password', [validators.Required()])
