import unittest
from cardpackage.card import Card

class TestCard(unittest.TestCase):

    def test_card_symbol(self):
        testCard = Card('Spades', 'Jack')
        result = testCard.card_symbol()
        self.assertEqual(result, 'S')

    def test_card_symbol2(self):
        testCard = Card('Hearts', 'Jack')
        result = testCard.card_symbol()
        self.assertEqual(result, 'H')

    def test_card_symbol3(self):
        testCard = Card('Diamonds', 'Jack')
        result = testCard.card_symbol()
        self.assertEqual(result, 'D')

    def test_card_symbol4(self):
        testCard = Card('Clubs', 'Jack')
        result = testCard.card_symbol()
        self.assertEqual(result, 'C')

    def test_card_rank(self):
        testCard = Card('Clubs', 'Jack')
        result = testCard.card_rank()
        self.assertEqual(result, 'J')

if __name__=='__main__':
    unittest.main()
