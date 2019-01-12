import unittest
from cardpackage.deck import Deck

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_deal(self):
        result = self.deck.deal()


if __name__=='__main__':
    unittest.main()
