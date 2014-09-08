from __future__ import absolute_import

from celery import Celery

celery_app = Celery('dexter', include=['dexter.tasks'])
celery_app.config_from_object('dexter.config.celeryconfig')

if __name__ == '__main__':
    celery_app.start()
