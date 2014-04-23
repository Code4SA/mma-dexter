from __future__ import division

from itertools import groupby

class BiasCalculator:
    """
    Helper class for running bias calculations across
    documents.
    """

    def calculate_bias_scores(self, docs, key):
        """
        Return a list of BiasScore instances for +docs+, where groups are calculated
        by grouping by the +key+ function.
        """
        docs.sort(key=key)
        return [self.calculate_bias(k, list(group), docs) for k, group in groupby(docs, key)]


    def calculate_bias(self, key, docs, universe):
        """
        Calculate the bias for +docs+, where +universe+ is the
        universe of all documents being considered.
        """
        score = BiasScore()
        score.key = key

        score.count = len(docs)

        # fraction of docs that are fair
        score.fair = sum(1 if d.is_fair() else 0 for d in docs)/score.count

        # how many items (dis)favoured?
        for d in docs:
            for df in d.fairness:
                if df.bias_favour:
                    score.favour += 1
                if df.bias_oppose:
                    score.oppose += 1

        score.parties = self.entropy(docs, universe)

        return score


    def entropy(self, docs, universe):
        # XXX TODO
        return 0


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
            "score": self.score,
            "record_count": self.count,
            "indicators": {
                "parties"     : self.parties,
                "fair"        : self.fair,
                "discrepancy" : self.discrepancy,
                "favour"      : self.favour,
                "oppose"      : self.oppose,
            }
        }

