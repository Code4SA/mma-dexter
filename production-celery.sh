#!/usr/bin/env bash

set -e

source env/bin/activate
source production-settings.sh

export FLASK_ENV=production
export NEW_RELIC_CONFIG_FILE=./dexter/config/newrelic.ini

exec newrelic-admin run-program celery worker \
    --app dexter.tasks\
    --beat\
    --concurrency 1\
    --loglevel info
