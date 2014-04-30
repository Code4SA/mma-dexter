from __future__ import division
from collections import defaultdict
from itertools import groupby
import math
import logging

from sqlalchemy.orm import joinedload, lazyload

from ..models import Document

class BiasCalculator:
    """
    Helper class for running bias calculations across
    documents.
    """
    log = logging.getLogger(__name__)

    def get_query(self):
        return Document.query\
            .options(
                joinedload(Document.sources),
                joinedload(Document.fairness),
                joinedload(Document.medium),
                lazyload('sources.person'),
                lazyload('sources.unnamed_gender'),
                lazyload('sources.unnamed_race'))


    def calculate_bias_scores(self, docs, key):
        """
        Return a list of BiasScore instances for +docs+, where groups are calculated
        by grouping by the +key+ function.
        """
        docs.sort(key=key)
        entropy = self.calculate_entropy(self.count_sources(docs, key))

        return [self.calculate_bias(k, list(group), entropy) for k, group in groupby(docs, key)]


    def calculate_bias(self, group, docs, entropy):
        """
        Calculate the bias for +docs+.
        """
        score = BiasScore()
        score.group = group
        score.count = len(docs)

        score.parties = entropy.get(group, 0)

        # fraction of docs that are fair
        score.fair = sum(1 if d.is_fair() else 0 for d in docs)/score.count

        # how many items (dis)favoured?
        for d in docs:
            for df in d.fairness:
                if df.bias_favour:
                    score.favour += 1
                if df.bias_oppose:
                    score.oppose += 1

        return score


    def count_sources(self, docs, key):
        """ Group docs by +key+ function and count the
        source affiliations. Returns a map from keys
        to counts by affiliation. """
        counts = defaultdict(lambda: defaultdict(int))

        self.log.debug("Counting sources for %d docs" % len(docs))

        for doc in docs:
            for source in doc.sources:
                # 4. are the political parties
                if source.affiliation and source.affiliation.code.startswith('4.'):
                    k = key(doc)
                    counts[key(doc)][source.affiliation.name] += 1

        self.log.debug("Done")

        return counts


    def calculate_entropy(self, table):
        """ Calculate entropy across +table+, which is a map
        representing a table: the keys are the columns and the
        values are dicts whose keys in turn are the rows.

        The entropy is a measure of how different each column
        is to the other columns in the table.

        Returns a map from column labels to entropy values.
        """
        self.log.debug("Calculating entropy")

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

            entropy[col] = -(1 / math.log(len(row_labels))) * total_p

        self.log.debug("Done")

        return entropy


class BiasScore:
    parties     = 0
    fair        = 0
    count       = 0
    favour      = 0
    oppose      = 0

    @property
    def score(self):
        return (0.345 * self.parties +
                0.547 * self.fair +
                0.109 * self.discrepancy)

    @property
    def discrepancy(self):
        total = self.favour + self.oppose
        if total == 0:
            return 1
        else:
            return 1 - abs(self.favour - self.oppose)/total

    def asdict(self):
        return {
            "bias": self.score,
            "record_count": self.count,
            "indicators": {
                "parties"     : self.parties,
                "fair"        : self.fair,
                "discrepancy" : self.discrepancy,
                "favour"      : self.favour,
                "oppose"      : self.oppose,
            }
        }

