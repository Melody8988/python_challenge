import unittest
from python_challenge import MarketSegment

class TestUniqueSegmentAccounts(unittest.TestCase):
    def test_account(self):
        # Test if incoming account currently exists in the segment's array
        self.isInstance(add_account(acc1, MarketSegment('Consumer Goods', [acc1, acc2])))
        