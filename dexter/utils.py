from __future__ import division
from functools import wraps
from datetime import timedelta, datetime

from flask.ext.sqlalchemy import Pagination
from flask import abort, Response, make_response

import nltk

def paginate(query, page, per_page=20, error_out=True):
    if error_out and page < 1:
        abort(404)
    items = query.limit(per_page).offset((page - 1) * per_page).all()
    if not items and page != 1 and error_out:
        abort(404)

    # No need to count if we're on the first page and there are fewer
    # items than we expected.
    if page == 1 and len(items) < per_page:
        total = len(items)
    else:
        total = query.order_by(None).count()

    return Pagination(query, page, per_page, total, items)


def slice(value, slices, fill_with=None):
    """Slice an iterator and return a list of lists containing
    those items. Useful if you want to create a div containing
    three ul tags that represent columns:
    .. sourcecode:: html+jinja
        <div class="columwrapper">
          {%- for column in items|slice(3) %}
            <ul class="column-{{ loop.index }}">
            {%- for item in column %}
              <li>{{ item }}</li>
            {%- endfor %}
            </ul>
          {%- endfor %}
        </div>
    If you pass it a second argument it's used to fill missing
    values on the last iteration.
    """
    seq = list(value)
    length = len(seq)
    items_per_slice = length // slices
    slices_with_extra = length % slices
    offset = 0
    for slice_number in range(slices):
        start = offset + slice_number * items_per_slice
        if slice_number < slices_with_extra:
            offset += 1
        end = offset + (slice_number + 1) * items_per_slice
        tmp = seq[start:end]
        if fill_with is not None and slice_number >= slices_with_extra:
            tmp.append(fill_with)
        yield tmp


def levenshtein(first, second):
    """
    Return a similarity ratio of two pieces of text. 0 means the strings are not similar at all,
    1.0 means they're identical. This is the Levenshtein ratio:

      (lensum - ldist) / lensum

    where lensum is the sum of the length of the two strings and ldist is the
    Levenshtein distance (edit distance).

    See https://groups.google.com/forum/#!topic/nltk-users/u94RFDWbGyw
    """
    lensum = len(first) + len(second)
    ldist = nltk.edit_distance(first, second, transpositions=True)

    if lensum == 0:
        return 0

    return (lensum - ldist) / lensum


# TODO: use flask-cache or something and do server-side caching too.
def client_cache_for(**duration):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            response = f(*args, **kwargs)
            if not isinstance(response, Response):
                response = make_response(response)

            if response.status_code == 200:
                delta = timedelta(**duration)
                response.cache_control.max_age = int(delta.total_seconds())
                response.expires = datetime.utcnow() + delta

            return response
        return wrapped

    return wrapper
