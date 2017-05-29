from celery.schedules import crontab


# uses AWS creds from the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY env variables
BROKER_URL = 'sqs://'
BROKER_TRANSPORT_OPTIONS = {
    'region': 'eu-west-1',
    'polling_interval': 60 * 1,
    'queue_name_prefix': 'mma-dexter-',
    'visibility_timeout': 3600,
}


# all our tasks can by retried if the worker fails
CELERY_ACKS_LATE = True
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'Africa/Johannesburg'
CELERY_ENABLE_UTC = True

CELERYBEAT_SCHEDULE = {
    'fetch-yesterdays-feeds': {
        'schedule': crontab(hour=3, minute=0),
        'task': 'dexter.tasks.fetch_yesterdays_feeds',
    },
    'backfill-taxonomies': {
        'schedule': crontab(hour=15, minute=0),
        'task': 'dexter.tasks.backfill_taxonomies',
    },
}
