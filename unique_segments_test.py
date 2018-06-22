import unittest
from python_challenge import add_segment

class TestUniqueAccountSegments(unittest.TestCase):
    def test_segment(self):
        # Test if incoming segment matches a segment currently in Account's array
        self.assertAlmostEqual(add_segment())