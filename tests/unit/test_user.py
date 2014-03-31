import unittest

from dexter.models import User

class TestUser(unittest.TestCase):
    def test_names(self):
        u = User()
        u.email = 'foo@bar.com'

        self.assertEqual('foo@bar.com', u.short_name())
        self.assertEqual('foo@bar.com', u.full_name())

        u.last_name = "Jones"
        self.assertEqual('Jones', u.short_name())
        self.assertEqual('Jones', u.full_name())

        u.first_name = "Bobby"
        self.assertEqual('Bobby J.', u.short_name())
        self.assertEqual('Bobby Jones', u.full_name())

        u.last_name = None
        self.assertEqual('Bobby', u.short_name())
        self.assertEqual('Bobby', u.full_name())
