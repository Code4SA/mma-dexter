import unittest
from datetime import datetime

from mock import MagicMock

from dexter.models import Person
from dexter.analysis import SourceAnalyser


class TestSourceAnalyser(unittest.TestCase):
    def setUp(self):
        self.sa = SourceAnalyser(doc_ids=[1], start_date=datetime(2014, 2, 10), end_date=datetime(2014, 2, 14))

    def test_basic_trends(self):
        self.sa.people = {
            1: Person(name='Fred', id=1),
            2: Person(name='Joe', id=2),
            3: Person(name='Sue', id=3)
        }

        self.sa.load_people_sources = MagicMock()
        self.sa.count_utterances = MagicMock(return_value={
            1: 10,
            2: 4,
        })
        self.sa.source_frequencies = MagicMock(return_value={
            1: [0, 0, 0, 1, 2],
            2: [1, 2, 3, 0, 0],
            3: [0, 0, 9, 0, 0],
        })
        self.sa.analyse()

        self.assertEqual(self.sa.analysed_people[1].source_counts, [0, 0, 0, 100.0, 100.0])
        self.assertEqual(self.sa.analysed_people[2].source_counts, [100.0, 100.0, 25.0, 0.0, 0.0])
        self.assertEqual(self.sa.analysed_people[3].source_counts, [0, 0, 75.0, 0.0, 0.0])

        self.assertEqual(self.sa.analysed_people[1].source_counts_trend, 2.0)
        self.assertAlmostEqual(self.sa.analysed_people[2].source_counts_trend, -1.5699, places=3)
        self.assertAlmostEqual(self.sa.analysed_people[3].source_counts_trend, -0.436, places=3)

        self.assertEqual([s.person.id for s in self.sa.top_people], [3, 2, 1])

        self.assertEqual([s.person.id for s in self.sa.people_trending_up], [1])
        self.assertEqual([s.person.id for s in self.sa.people_trending_down], [2])
