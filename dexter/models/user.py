from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
    )
from sqlalchemy.orm import relationship

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
    first_name  = Column(String(50), nullable=False)
    last_name   = Column(String(50), nullable=False)
    admin       = Column(Boolean, default=False)
    disabled    = Column(Boolean, default=False)
    encrypted_password = Column(String(100))

    default_analysis_nature_id = Column(Integer, ForeignKey('analysis_natures.id'), default=1)

    country_id  = Column(Integer, ForeignKey('countries.id'), nullable=False)

    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # associations
    default_analysis_nature = relationship("AnalysisNature")
    country     = relationship("Country")

    def get_password(self):
        return None

    def set_password(self, password):
        if password:
            self.encrypted_password = sha256_crypt.encrypt(password)


    def short_name(self):
        s = ""
        if self.first_name:
            s += self.first_name
        
        if self.last_name:
            if s:
                s += " " + self.last_name[0] + "."
            else:
                s = self.last_name

        if not s:
            s = self.email

        return s

    def full_name(self):
        s = '%s %s' % (self.first_name or '', self.last_name or '')
        s = s.strip()

        if not s:
            s = self.email

        return s


    password = property(get_password, set_password)

    def __repr__(self):
        return "<User email=%s>" % (self.email,)

    @classmethod
    def get_and_authenticate(cls, email, password):
        user = cls.query.filter(User.email == email).first()
        if user and not user.disabled and sha256_crypt.verify(password, user.encrypted_password):
            return user

        return None

    @classmethod
    def create_defaults(self):
        from . import Country

        admin_user = User()
        admin_user.first_name = "Admin"
        admin_user.last_name = "Admin"
        admin_user.admin = True
        admin_user.email = "admin@code4sa.org"
        admin_user.country = Country.query.filter(Country.name == 'South Africa').one()
        admin_user.encrypted_password = sha256_crypt.encrypt('admin')

        return [admin_user]


class LoginForm(Form):
    email       = EmailField('Email', [validators.Required()])
    password    = PasswordField('Password', [validators.Required()])


def default_analysis_nature_id():
    from flask.ext.login import current_user

    if current_user.is_authenticated() and current_user.default_analysis_nature_id:
        return current_user.default_analysis_nature_id

    return 1

def default_country_id():
    from flask.ext.login import current_user

    if current_user.is_authenticated() and current_user.country_id is not None:
        return current_user.country_id

    return None
