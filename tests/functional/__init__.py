from flask import url_for
from flask.ext.testing import TestCase
from flask.ext.fillin import FormWrapper

from dexter.core import app
from dexter.app import db
from dexter.models.seeds import seed_db
from dexter.models import User, Role

class UserSessionTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def login(self, email='user@example.com', password='foo'):
        u = User.query.filter(User.email == email).one()
        u.roles = Role.query.all()
        db.session.commit()

        res = self.client.post(url_for('security.login'),
            data={'email': email, 'password': password},
            follow_redirects=True)
        self.assert200(res)

    def logout(self):
        res = self.client.get(url_for('security.logout'), follow_redirects=False)
        self.assertRedirects(res, '/')

    def setUp(self):
        self.db = db
        self.db.session.remove()
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

        self.client.response_wrapper = FormWrapper

    def tearDown(self):
        self.fx.teardown()
        self.db.session.rollback()
        self.db.session.remove()
        self.db.drop_all()
