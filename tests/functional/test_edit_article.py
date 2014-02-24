from flask.ext.testing import TestCase
from flask.ext.fillin import FormWrapper

from mock import patch, MagicMock

from dexter.core import app
from dexter.models.support import db
from dexter.models import Author
from dexter.models.seeds import seed_db

from tests.fixtures import dbfixture, DocumentData

class TestEditArticle(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.db = db
        self.db.session.remove()
        self.db.drop_all()
        self.db.create_all()
        seed_db(db)

        self.fx = dbfixture.data(DocumentData)
        self.fx.setup()

        self.client.response_wrapper = FormWrapper

    def tearDown(self):
        self.fx.teardown()
        self.db.session.rollback()
        self.db.session.remove()
        self.db.drop_all()
  
    def test_edit_article_new_author(self):
        res = self.client.get('/articles/%s/edit' % self.fx.DocumentData.simple.id)
        self.assert200(res)

        f = res.forms[0]
        f.fields['author-name'] = 'Sue Skosana'
        f.fields['author-person_gender_id'] = '1'
        f.fields['author-person_race_id'] = '1'

        res = f.submit(self.client)
        self.assertRedirects(res, '/articles/%s' % self.fx.DocumentData.simple.id)

        sue = Author.query.filter(Author.name == 'Sue Skosana').one()
        self.assertEqual('Female', sue.person.gender.name)
        self.assertEqual('Black', sue.person.race.name)
