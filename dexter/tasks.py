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

    if date.today() == date(2021, 1, 25):
        d1 = date(2020, 12, 8)
        d2 = date(2020, 12, 15)
        days = [d1 + timedelta(days=x) for x in range((d2 - d1).days + 1)]

        for d in days:
            for newsroom in ['bhekisisa', 'nigeriahealthwatch', 'premiumtimes', 'newhumanitarian']:
                filter_parm = 'media=%s' % newsroom
                fetch_filtered_daily_feeds.delay(d.isoformat(), filter_parm)

    elif date.today() == date(2021, 1, 26):
        d1 = date(2019, 8, 13)
        d2 = date(2020, 12, 15)
        days = [d1 + timedelta(days=x) for x in range((d2 - d1).days + 1)]

        for d in days:
            filter_parm = 'media=punchng'
            fetch_filtered_daily_feeds.delay(d.isoformat(), filter_parm)

    # elif date.today() == date(2020, 11, 27):
    #     d1 = date(2020, 11, 11)
    #     days = [d1]
    #
    #     filter_parm = ''
    #
    #     for d in days:
    #         fetch_filtered_daily_feeds.delay(d.isoformat(), filter_parm)

    # elif date.today() == date(2020, 6, 6):
    #     d1 = date(2020, 5, 30)
    #     # d2 = date(2020, 4, 21)
    #     # days = [d1 + timedelta(days=x) for x in range((d2 - d1).days + 1)]
    #     days = [d1]
    #
    # elif date.today() == date(2020, 6, 7):
    #     d1 = date(2020, 6, 1)
    #     # d2 = date(2020, 4, 21)
    #     # days = [d1 + timedelta(days=x) for x in range((d2 - d1).days + 1)]
    #     days = [d1]
    #
    #     filter_parm = ''
    #
    #     for d in days:
    #         fetch_filtered_daily_feeds.delay(d.isoformat(), filter_parm)

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


# retry after 60 minutes, retry for up to 7 days
@app.task(bind=True, default_retry_delay=6*60*60, max_retries=7*4)
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
