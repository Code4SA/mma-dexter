from celery.schedules import crontab
from datetime import timedelta

BROKER_URL = 'amqp://guest:guest@localhost:5672'

# all our tasks can by retried if the worker fails
CELERY_ACKS_LATE = True
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Africa/Johannesburg'
CELERY_ENABLE_UTC = True

CELERYBEAT_SCHEDULE = {
    'fetch-yesterdays-feeds': {
        'schedule': crontab(hour=3, minute=0),
        'task': 'dexter.tasks.fetch_yesterdays_feeds',
    },
    'backfill-taxonomies': {
        'schedule': crontab(hour=15, minute=0),
        'task': 'dexter.tasks.baxfill_taxonomies',
    },
}
