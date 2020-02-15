web: gunicorn --workers 4 --worker-class gevent --timeout 600 --log-file - --access-logfile - app:app
worker: celery worker --app dexter.tasks --beat --concurrency 1 --loglevel info
