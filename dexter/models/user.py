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

from flask.ext.security import UserMixin, RoleMixin

from ..app import db, app
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
    password    = Column(String(100), default='')

    default_analysis_nature_id = Column(Integer, ForeignKey('analysis_natures.id'), default=1, nullable=False)

    country_id  = Column(Integer, ForeignKey('countries.id'), nullable=False)

    created_at   = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at   = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # associations
    default_analysis_nature = relationship("AnalysisNature")
    country     = relationship("Country")
    roles       = db.relationship('Role', secondary='roles_users', backref=db.backref('users', lazy='dynamic'))

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


    def __repr__(self):
        return "<User email=%s>" % (self.email,)

    # Flask-Security requires an active attribute
    @property
    def active(self):
        return not self.disabled

    @active.setter
    def active(self, value):
        self.disabled = not value

    @classmethod
    def create_defaults(self):
        from . import Country
        from flask_security.utils import encrypt_password

        admin_user = User()
        admin_user.first_name = "Admin"
        admin_user.last_name = "Admin"
        admin_user.admin = True
        admin_user.email = "admin@code4sa.org"
        admin_user.country = Country.query.filter(Country.name == 'South Africa').one()
        admin_user.password = encrypt_password('admin')

        return [admin_user]


class Role(db.Model, RoleMixin):

    __tablename__ = "roles"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __unicode__(self):
        return unicode(self.name)

    @classmethod
    def create_defaults(self):
        return [
                Role(name='monitor', description='user can add and edit documents'),
                Role(name='miner', description='user can use the Dexter Mine feature'),
                ]


roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE')),
        db.Column('role_id', db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE')))


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


# user authentication
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask.ext.mako import render_template
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
app.extensions['security'].render_template = render_template
