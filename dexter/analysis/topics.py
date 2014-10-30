from math import sqrt
import collections

from itertools import groupby
from datetime import datetime
from dateutil.parser import parse

from dexter.analysis.base import BaseAnalyser, moving_weighted_avg_zscore
from dexter.models import db, Document, DocumentEntity, Person, Utterance, Entity

from sqlalchemy.sql import func, distinct, or_, desc
from sqlalchemy.orm import subqueryload

class AnalysedMention(object):
    pass


class AnalysedTopic(object):
    pass


class TopicAnalyser(BaseAnalyser):
    """
    Helper that runs analyses on document topics.
    """

    def __init__(self, doc_ids=None, start_date=None, end_date=None):
        super(TopicAnalyser, self).__init__(doc_ids, start_date, end_date)
        self.top_people = None
        self.clustered_topics = None
        self.topic_score_threshold = 0.6

    def find_top_people(self):
        self._load_people_mentions()
        self._analyse_people_mentions()

    def _load_people_mentions(self):
        """
        Load all people mentions data for this period.
        """
        rows = db.session.query(distinct(Entity.person_id))\
                .filter(
                        DocumentEntity.doc_id.in_(self.doc_ids),
                        Entity.person_id != None)\
                .join(DocumentEntity, DocumentEntity.entity_id == Entity.id)\
                .all()
        self.people = self._lookup_people([r[0] for r in rows])

    def _analyse_people_mentions(self):
        """
        Do trend analysis on people mentions.
        """
        mention_counts = self.mention_frequencies(self.people.keys())

        self.analysed_people = {}
        for pid, person in self.people.iteritems():
            topic = AnalysedMention()
            topic.person = person
            topic.mention_counts = mention_counts[pid]
            topic.mention_counts_total = sum(topic.mention_counts)
            self.analysed_people[pid] = topic

        # normalize by total counts per day
        totals = [0] * (self.days+1)

        # first count per-day totals
        for topic in self.analysed_people.itervalues():
            for i, n in enumerate(topic.mention_counts):
                totals[i] += n

        # normalize
        for topic in self.analysed_people.itervalues():
            for i, n in enumerate(topic.mention_counts):
                if totals[i] == 0:
                    topic.mention_counts[i] = 0
                else:
                    topic.mention_counts[i] = 100.0 * n / totals[i]

        # calculate trends
        for topic in self.analysed_people.itervalues():
            topic.mention_counts_trend = moving_weighted_avg_zscore(topic.mention_counts, 0.8)


        # top 20 sources
        self.top_people = sorted(
                self.analysed_people.itervalues(),
                key=lambda s: s.mention_counts_total, reverse=True)[:20]

        # trends
        trending = sorted(
                self.analysed_people.itervalues(),
                key=lambda s: s.mention_counts_trend)

        # top 10 trending up, most trending first
        self.people_trending_up = [s for s in trending[-10:] if s.mention_counts_trend > self.TREND_UP]
        self.people_trending_up.reverse()

        # top 10 trending down, most trending first
        self.people_trending_down = [s for s in trending[:10] if s.mention_counts_trend < self.TREND_DOWN]

    def mention_frequencies(self, ids):
        """
        Return dict from person ID to a list of how frequently each
        person was mentioned per day, over the period.
        """
        rows = db.session.query(
                    Entity.person_id,
                    func.date_format(Document.published_at, '%Y-%m-%d').label('date'),
                    func.count(distinct(DocumentEntity.doc_id)).label('count')
                ) \
                .join(DocumentEntity, Entity.id == DocumentEntity.entity_id) \
                .join(Document, DocumentEntity.doc_id == Document.id) \
                .filter(Entity.person_id.in_(ids))\
                .filter(DocumentEntity.doc_id.in_(self.doc_ids))\
                .group_by(Entity.person_id, 'date')\
                .order_by(Entity.person_id, Document.published_at)\
                .all()

        freqs = {}
        for person_id, group in groupby(rows, lambda r: r[0]):
            freqs[person_id] = [0] * (self.days+1)

            # set day buckets based on date
            for row in group:
                d, n = parse(row[1]).date(), row[2]
                day = (d - self.start_date).days
                freqs[person_id][day] = n

        return freqs

    def find_topics(self):
        """
        Run clustering on these documents and identify common topics.

        We use latent Dirichlet allocation (LDA) to cluster the documents
        into an arbitrary number of clusters. We then find the strongest
        clusters and pull representative documents for each cluster.

        Clustering is based on the people and entities mentioned in the documents,
        rather than raw text. This is based on the assumption that Opencalais and
        AlchemyAPI have already done the work to identify pertinent things
        and concepts in the documents, so rely on those rather than on
        arbitrary words.

        The results are stored in `clustered_topics`.

        See also: https://github.com/ariddell/lda
        """
        from sklearn.feature_extraction import DictVectorizer
        import numpy

        # TODO: factor people into cluster calcs

        self.clustered_topics = []

        # load documents and their entities
        docs = Document.query\
            .options(subqueryload('entities'),
                     subqueryload('medium'))\
            .filter(Document.id.in_(self.doc_ids))\
            .all()

        if not docs:
            return

        # guess at the number of topics, between 1 and 50
        n_topics = max(min(50, len(docs)/5), 1)

        # list of entity maps for each document, from entity name to occurrence count
        entities = [dict(('%s-%s' % (de.entity.group, de.entity.name), de.count or 1)
                         for de in d.entities) for d in docs]
        vec = DictVectorizer(sparse=False)

        # TODO: we should ideally use sparse, but it causes the lda library to fail
        entity_vector = vec.fit_transform(entities)
        features = numpy.array(vec.feature_names_)

        clusters, lda_model = self._run_lda(entity_vector, n_topics)
        del entity_vector
        del vec

        # for normalising histograms
        day_counts = self.date_histogram(d.published_at for d in docs)

        # generate topic info
        for i, cluster in clusters.iteritems():
            # cluster is a list of (doc-index, score) pairs

            # sort each cluster to put top-scoring docs first
            # TODO: this isn't great, because scores for each document
            # for the same cluster can't really be compared. We
            # need a better way of doing this.
            cluster.sort(key=lambda p: p[1], reverse=True)
            cluster_docs = [docs[p[0]] for p in cluster]

            topic = AnalysedTopic()
            topic.documents = cluster_docs
            topic.n_documents = len(cluster)

            # top 8 features for this topic as (feature, weight) pairs
            indexes = numpy.argsort(lda_model.components_[i])[:-8:-1]
            topic.features = zip(features[indexes], lda_model.components_[i][indexes])

            # top 20 of each cluster are used to characterize the cluster
            best = cluster[0:20]
            topic.score = numpy.average([p[1] for p in best])
            # score for this topic as stars, from 0 to 3
            topic.stars = int(round(3.0 * (topic.score - self.topic_score_threshold) / self.topic_score_threshold, 0))

            # media counts
            media = dict(collections.Counter([d.medium for d in cluster_docs]))
            topic.media_counts = sorted(media.items(), key=lambda p: p[1], reverse=True)

            # publication dates
            topic.histogram = self.date_histogram((d.published_at for d in cluster_docs))
            topic.trend = moving_weighted_avg_zscore(topic.histogram)
            topic.histogram = self.normalise_histogram(topic.histogram, day_counts)


            self.clustered_topics.append(topic)

        # sort clusters by size
        self.clustered_topics.sort(key=lambda t: topic.n_documents, reverse=True)

        # keep only the clusters with a score >= self.topic_score_threshold
        self.clustered_topics = [t for t in self.clustered_topics if t.score >= self.topic_score_threshold]

    def _run_lda(self, data, n_topics):
        """
        Run LDA algorithm.

        :param data: sparse vector of document features
        :param n_topics: number of topics we want
        :return: map from topic label (int) to list of (doc-index, score) tuples of documents
                 in that topic cluster.
        """
        import lda

        lda_model = lda.LDA(n_topics=n_topics, n_iter=200, random_state=1)
        lda_model.fit(data)

        clusters = collections.defaultdict(list)
        # doc_topic_ are the per-topic scores for each document
        for i, scores in enumerate(lda_model.doc_topic_):
            label = scores.argmax()
            score = scores[label]
            clusters[label].append((i, score))

        return clusters, lda_model

    def date_histogram(self, dates):
        """
        Bucketize an iterable of datetime instances across the period
        covered by this analysis.

        :param dates: iterable of datetime instances
        :return: a list of counts per day
        """
        histo = [0] * (self.days+1)
        for d in dates:
            day = (d.date() - self.start_date).days
            histo[day] += 1
        return histo

    def normalise_histogram(self, histo, norm):
        for i, n in enumerate(norm):
            if n > 0:
                histo[i] = float(histo[i]) / n
        return histo
