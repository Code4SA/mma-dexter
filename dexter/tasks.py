from __future__ import absolute_import

import logging
from datetime import date, timedelta
from dateutil.parser import parse

from dexter.app import celery_app as app
from dexter.processing import DocumentProcessor, DocumentProcessorNT

# force configs for API keys to be set
import dexter.core

# This is a collection of periodic tasks for Dexter, using
# Celery to drive task completion.

log = logging.getLogger(__name__)


@app.task
def back_process_feeds():
    """ Enqueue a task to fetch yesterday's feeds. """

    # if date.today() == date(2021, 4, 5):
    #     d1 = date(2021, 4, 1)
    #     # d2 = date(2020, 12, 31)
    #     days = [d1]
    #
    #     for d in days:
    #         filter_parm = ''
    #         fetch_filtered_daily_feeds.delay(d.isoformat(), filter_parm)

    # if date.today() == date(2021, 2, 17):
    #     d1 = date(2021, 2, 13)
    #     # d2 = date(2020, 12, 31)
    #     days = [d1]
    #
    #     for d in days:
    #         filter_parm = ''
    #         fetch_filtered_daily_feeds.delay(d.isoformat(), filter_parm)

    if date.today() == date(2021, 4, 6):
        d1 = date(2021, 3, 20)
        d2 = date(2021, 4, 5)
        days = [d1 + timedelta(days=x) for x in range((d2 - d1).days + 1)]

        for d in days:
            filter_parm = 'media=theconversationafrica'
            fetch_filtered_daily_feeds.delay(d.isoformat(), filter_parm)

    else:
        print 'Already Done!'


@app.task
def fetch_yesterdays_feeds():
    """ Enqueue a task to fetch yesterday's feeds. """
    yesterday = date.today() - timedelta(days=1)
    fetch_daily_feeds.delay(yesterday.isoformat())


# retry after 60 minutes, retry for up to 7 days
@app.task(bind=True)
def fetch_filtered_daily_feeds(self, day, filter_parm):
    """ Fetch feed of URLs to crawl and queue up a task to grab and process
    each url. """
    try:
        day = parse(day)

        dp = DocumentProcessorNT()
        count = 0
        for item in dp.fetch_filtered_daily_feed_items(day, filter_parm):
            get_feed_item.delay(item)
            count += 1
    except Exception as e:
        log.error("Error processing daily feeds for %s" % day, exc_info=e)
        self.retry(exc=e)


# retry twice daily, retry for up to 1 day
@app.task(bind=True, default_retry_delay=12*60*60, max_retries=2)
def fetch_daily_feeds(self, day):
    """ Fetch feed of URLs to crawl and queue up a task to grab and process
    each url. """
    try:
        day = parse(day)

        dp = DocumentProcessorNT()
        count = 0
        for item in dp.fetch_daily_feed_items(day):
            get_feed_item.delay(item)
            count += 1
    except Exception as e:
        log.error("Error processing daily feeds for %s" % day, exc_info=e)
        self.retry(exc=e)

    if count == 0:
        # nothing to do, retry later
        self.retry()


# retry every minute, for up to 24 hours.
@app.task(bind=True, rate_limit="10/m", default_retry_delay=30, max_retries=2)
def get_feed_item(self, item):
    """ Fetch and process a document feed item. """
    try:
        dp = DocumentProcessorNT()
        dp.process_feed_item(item)
    except Exception as e:
        log.error("Error processing feed item: %s" % item, exc_info=e)
        self.retry()


@app.task
def backfill_taxonomies():
    """ Enqueue a task to backfill taxonomies """
    try:
        dp = DocumentProcessorNT()
        dp.backfill_taxonomies()
    except Exception as e:
        log.error("Error backfilling taxonomies: %s" % e.message, exc_info=e)
