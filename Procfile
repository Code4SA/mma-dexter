web: newrelic-admin run-program gunicorn --workers 1 --worker-class gevent --timeout 600 --log-file - --access-logfile - app:app
worker: newrelic-admin run-program celery worker --app dexter.tasks --beat --concurrency 1 --loglevel info
