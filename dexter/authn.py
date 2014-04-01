from flask.ext.login import AnonymousUserMixin

class AnonymousUser(AnonymousUserMixin):
    @property
    def admin(self):
        return False
