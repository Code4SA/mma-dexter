import logging
import threading

def userIdFilterFactory(**kwargs):
    return UserIdFilter()

class UserIdFilter(logging.Filter):
    _storage = threading.local()

    """
    This filter adds a userid parameter to the logging context.
    """
    def filter(self, record):
        record.userid = 'userid:%s' % getattr(self._storage, 'flask_userid', '-')
        return record

    @classmethod
    def set_userid(cls, userid):
        cls._storage.flask_userid = userid
