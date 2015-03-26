from mock import patch, MagicMock

from . import UserSessionTestCase

from dexter.core import app
from dexter.models import Author, Document, db
from dexter.authn import AnonymousUser

from tests.fixtures import dbfixture, DocumentData, UserData

class TestEditArticle(UserSessionTestCase):
    def setUp(self):
        super(TestEditArticle, self).setUp()

        self.fx = dbfixture.data(DocumentData, UserData)
        self.fx.setup()

        self.login()

    def test_edit_article_new_author(self):
        res = self.client.get('/articles/%s/edit' % self.fx.DocumentData.simple.id)
        self.assert200(res)

        f = res.forms[1]
        f.fields['author-name'] = 'Sue Skosana'
        f.fields['author-person_gender_id'] = '1'
        f.fields['author-person_race_id'] = '1'

        res = f.submit(self.client)
        self.assertRedirects(res, '/articles/%s' % self.fx.DocumentData.simple.id)

        sue = Author.query.filter(Author.name == 'Sue Skosana').one()
        self.assertEqual('Female', sue.person.gender.name)
        self.assertEqual('Black', sue.person.race.name)
  
    def test_delete_article_success(self):
        AnonymousUser.admin = MagicMock(return_value=True)
        res = self.client.get('/articles/%s/edit' % self.fx.DocumentData.simple.id)
        self.assert200(res)

        res = self.client.post('/articles/%s/delete' % self.fx.DocumentData.simple.id)
        self.assertRedirects(res, '/dashboard')

        doc = Document.query.get(self.fx.DocumentData.simple.id)
        self.assertIsNone(doc)

    def test_delete_article_no_perms(self):
        self.logout()
        self.login(email='joe@example.com')

        res = self.client.post('/articles/%s/delete' % self.fx.DocumentData.simple.id)
        self.assertRedirects(res, '/articles/%s' % self.fx.DocumentData.simple.id)

        doc = Document.query.get(self.fx.DocumentData.simple.id)
        self.assertIsNotNone(doc)
