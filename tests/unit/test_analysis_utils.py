import unittest

from dexter.analysis.utils import calculate_entropy

class TestUser(unittest.TestCase):
    def test_entropy_none(self):
        table = {}
        self.assertEqual(
                calculate_entropy(table),
                {})

    def test_entropy_all_zeros(self):
        table = {
            'The Star': {
                'AMP': 0,
                'ACDP': 0,
                'ANC': 0,
            },
            'Beeld': {
                'ANC': 0,
            },
        }

        entropies = calculate_entropy(table)

        self.assertAlmostEqual(0, entropies['The Star'], 2)
        self.assertAlmostEqual(0, entropies['Beeld'], 2)

    def test_entropy_simple(self):
        table = {
            'The Star': {
                'AMP': 6,
                'ACDP': 6,
                'ANC': 200,
            },
            'Beeld': {
                'ANC': 14,
            },
            'Sowetan': {
                'Foo': 6,
                'AMP': 4,
                'ACDP': 5,
                'ANC': 252,
            },
            'BD': {
                'Foo': 81,
                'ACDP': 10,
                'ANC': 610,
            },
            'Citizen': {
                'Foo': 11,
                'AMP': 5, 
                'ACDP': 2,
                'ANC': 301,
            },
        }

        entropies = calculate_entropy(table)

        self.assertAlmostEqual(0.74, entropies['The Star'], 2)
        self.assertAlmostEqual(0.0, entropies['Beeld'], 2)
        self.assertAlmostEqual(0.93, entropies['Sowetan'], 2)
        self.assertAlmostEqual(0.76, entropies['BD'], 2)
        self.assertAlmostEqual(0.9, entropies['Citizen'], 2)
