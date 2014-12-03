from __future__ import division

from collections import defaultdict
import logging
import math

logger = logging.getLogger(__name__)

def calculate_entropy(table):
    """ Calculate entropy across +table+, which is a map
    representing a table: the keys are the columns and the
    values are dicts whose keys in turn are the rows.

    The entropy is a measure of how different each column
    is to the other columns in the table.

    Returns a map from column labels to entropy values.
    """
    global logger
    logger.debug("Calculating entropy")

    col_labels = table.keys()
    row_labels = set()
    for d in table.itervalues():
        row_labels.update(d.keys())
    row_labels = list(row_labels)

    col_sums = {}
    row_sums = defaultdict(int)
    total = 0

    # sum across all directions
    for col in col_labels:
        # sum down column
        col_sums[col] = sum(table[col].itervalues())

        # sum across row
        for row, n in table[col].iteritems():
            row_sums[row] += n
            total += n

    # calculate entropy per column
    entropy = {}
    for col in col_labels:
        col_total = col_sums[col]
        if col_total == 0:
            entropy[col] = 0
            continue

        row_coverage = defaultdict(int)
        col_coverage = 0
        for row in row_labels:
            # how much does this row contribute to the total
            row_fraction = row_sums[row] / total

            if row_fraction > 0:
                # the fraction this row contributes to the column,
                # as a fraction of the total row
                row_coverage[row] = table[col].get(row, 0) / col_total / row_fraction
            else:
                row_coverage[row] = 0

            col_coverage += row_coverage[row]

        k = 1 / col_coverage

        total_p = 0
        for row in row_labels:
            p = k * row_coverage[row]
            if p > 0:
                p = p * math.log(p)
            total_p += p

        if len(row_labels) == 1:
            # avoid 1/0
            log = 1
        else:
            log = 1 / math.log(len(row_labels))

        entropy[col] = -log * total_p

    logger.debug("Done")

    return entropy
