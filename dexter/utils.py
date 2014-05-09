from __future__ import division

from flask.ext.sqlalchemy import Pagination
from flask import abort

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
    ldist = nltk.edit_distance(first, second)

    if lensum == 0:
        return 0

    return (lensum - ldist) / lensum
