from __future__ import absolute_import
from datetime import date, timedelta
from dateutil.parser import parse

from dexter.app import celery_app as app
from dexter.processing import DocumentProcessor

# This is a collection of periodic tasks for Dexter, using
# Celery to drive task completion.

@app.task
def fetch_yesterdays_feeds():
    """ Enqueue a task to fetch yesterday's feeds. """
    yesterday = date.today() - timedelta(days=1)
    fetch_daily_feeds.delay(yesterday.isoformat())


# retry after 30 minutes, retry for up to 7 days
@app.task(bind=True, default_retry_delay=30*60, max_retries=7*24*2)
def fetch_daily_feeds(self, day):
    """ Fetch feed of URLs to crawl and queue up a task to grab and process
    each url. """
    day = parse(day)

    dp = DocumentProcessor()
    count = 0
    for item in dp.fetch_daily_feed_items(day):
        get_feed_item.delay(item)
        count += 1

    if count == 0:
        # nothing to do, retry later
        self.retry()


# retry every minute, for up to 24 hours.
@app.task(rate_limit="10/m", default_retry_delay=60, max_retries=24*60)
def get_feed_item(item):
    """ Fetch and process a document feed item. """
    dp = DocumentProcessor()
    dp.process_feed_item(item)
