#!/usr/bin/env bash

set -e

APP_HOME=$HOME/mma-dexter
cd $APP_HOME

source env/bin/activate
source production-settings.sh

export FLASK_ENV=production

GUNICORN_SOCKET=/tmp/dexter-gunicorn.sock
GUNICORN_WORKERS=4

exec gunicorn \
    -w $GUNICORN_WORKERS \
    -b unix:$GUNICORN_SOCKET \
    dexter.app:app
    2>&1