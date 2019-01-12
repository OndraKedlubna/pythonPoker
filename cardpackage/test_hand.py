import unittest
from cardpackage.hand import Hand
from cardpackage.card import Card

class TestHand(unittest.TestCase):

    def setUp(self):
        self.hand = Hand()

    def test_add_card(self):
        self.hand.add_card(Card("Hearts", "Two"))
        self.hand.add_card(Card("Clubs", "Six"))
        self.hand.add_card(Card("Clubs", "Nine"))
        self.hand.add_card(Card("Clubs", "Queen"))
        self.hand.add_card(Card("Diamonds", "Ace"))
        self.assertEqual(self.hand.cards, [Card("Hearts", "Two"), Card("Clubs", "Six"), Card("Clubs", "Nine"), Card("Clubs", "Queen"), Card("Diamonds", "Ace")])

    def test_remove_card(self):
        self.hand.add_card(Card("Hearts", "Two"))
        self.hand.add_card(Card("Clubs", "Six"))
        self.hand.add_card(Card("Clubs", "Nine"))
        self.hand.add_card(Card("Clubs", "Queen"))
        self.hand.add_card(Card("Diamonds", "Ace"))
        self.hand._Hand__remove_card(2)
        self.hand._Hand__remove_card(4)
        #print(Card("Diamonds", "Ace") == Card("Diamonds", "Ace"))
        self.assertEqual(self.hand.cards, [Card("Hearts", "Two"), None, Card("Clubs", "Nine"), None, Card("Diamonds", "Ace")])

    def test_change_card(self):
        self.hand.add_card(Card("Hearts", "Two"))
        self.hand.add_card(Card("Clubs", "Six"))
        self.hand.add_card(Card("Clubs", "Nine"))
        self.hand.add_card(Card("Clubs", "Queen"))
        self.hand.add_card(Card("Diamonds", "Ace"))
        self.hand.change_card(2, Card("Clubs", "Jack"))
        self.hand.change_card(4, Card("Diamonds", "King"))
        #print(Card("Diamonds", "Ace") == Card("Diamonds", "Ace"))
        self.assertEqual(self.hand.cards, [Card("Hearts", "Two"), Card("Clubs", "Jack"), Card("Clubs", "Nine"), Card("Diamonds", "King"), Card("Diamonds", "Ace")])

    def test_combination_value(self):
        self.hand.add_card(Card("Hearts", "Two"))
        self.hand.add_card(Card("Clubs", "Six"))
        self.hand.add_card(Card("Clubs", "Nine"))
        self.hand.add_card(Card("Clubs", "Queen"))
        self.hand.add_card(Card("Diamonds", "Ace"))
        result = self.hand.combination_value()
        self.assertEqual(result, 0)

    def test_combination_value_exception(self):
        self.hand.add_card(Card("Hearts", "Two"))
        self.hand.add_card(Card("Diamonds", "Ace"))
        with self.assertRaises(ValueError):
            self.hand.combination_value()

    def test_values_list(self):
        self.hand.add_card(Card("Hearts", "Nine"))
        self.hand.add_card(Card("Clubs", "Six"))
        self.hand.add_card(Card("Clubs", "Nine"))
        self.hand.add_card(Card("Clubs", "Queen"))
        self.hand.add_card(Card("Diamonds", "Ace"))
        result =self.hand._Hand__values_list()
        self.assertEqual(result, [0,0,0,0,1,0,0,2,0,0,1,0,1])

    def test_values_royal(self):
        self.hand.add_card(Card("Clubs", "Nine"))
        self.hand.add_card(Card("Clubs", "Eight"))
        self.hand.add_card(Card("Clubs", "Seven"))
        self.hand.add_card(Card("Clubs", "Ten"))
        self.hand.add_card(Card("Clubs", "Jack"))
        result = self.hand.combination_value()
        self.assertEqual(result, 8)

    def test_values_four(self):
        self.hand.add_card(Card("Hearts", "Nine"))
        self.hand.add_card(Card("Clubs", "Six"))
        self.hand.add_card(Card("Clubs", "Nine"))
        self.hand.add_card(Card("Spades", "Nine"))
        self.hand.add_card(Card("Diamonds", "Nine"))
        result = self.hand.combination_value()
        self.assertEqual(result, 7)

    def test_values_full(self):
        self.hand.add_card(Card("Hearts", "Six"))
        self.hand.add_card(Card("Clubs", "Six"))
        self.hand.add_card(Card("Clubs", "Nine"))
        self.hand.add_card(Card("Spades", "Nine"))
        self.hand.add_card(Card("Diamonds", "Nine"))
        result = self.hand.combination_value()
        self.assertEqual(result, 6)

    def test_values_flush(self):
        self.hand.add_card(Card("Hearts", "Two"))
        self.hand.add_card(Card("Hearts", "Six"))
        self.hand.add_card(Card("Hearts", "Jack"))
        self.hand.add_card(Card("Hearts", "Nine"))
        self.hand.add_card(Card("Hearts", "Queen"))
        result = self.hand.combination_value()
        self.assertEqual(result, 5)

    def test_values_straight(self):
        self.hand.add_card(Card("Hearts", "Eight"))
        self.hand.add_card(Card("Diamonds", "Ten"))
        self.hand.add_card(Card("Spades", "Jack"))
        self.hand.add_card(Card("Diamonds", "Nine"))
        self.hand.add_card(Card("Hearts", "Queen"))
        result = self.hand.combination_value()
        self.assertEqual(result, 4)

    def test_values_straight_ace(self):
        self.hand.add_card(Card("Hearts", "Two"))
        self.hand.add_card(Card("Diamonds", "Ace"))
        self.hand.add_card(Card("Spades", "Four"))
        self.hand.add_card(Card("Hearts", "Three"))
        self.hand.add_card(Card("Hearts", "Five"))
        result = self.hand.combination_value()
        self.assertEqual(result, 4)

    def test_values_three(self):
        self.hand.add_card(Card("Hearts", "Two"))
        self.hand.add_card(Card("Clubs", "Six"))
        self.hand.add_card(Card("Clubs", "Nine"))
        self.hand.add_card(Card("Spades", "Nine"))
        self.hand.add_card(Card("Diamonds", "Nine"))
        result = self.hand.combination_value()
        self.assertEqual(result, 3)

    def test_values_two_pairs(self):
        self.hand.add_card(Card("Hearts", "Two"))
        self.hand.add_card(Card("Clubs", "Six"))
        self.hand.add_card(Card("Clubs", "Two"))
        self.hand.add_card(Card("Spades", "Nine"))
        self.hand.add_card(Card("Diamonds", "Nine"))
        result = self.hand.combination_value()
        self.assertEqual(result, 2)

    def test_values_pair(self):
        self.hand.add_card(Card("Hearts", "Two"))
        self.hand.add_card(Card("Clubs", "Six"))
        self.hand.add_card(Card("Clubs", "Jack"))
        self.hand.add_card(Card("Spades", "Nine"))
        self.hand.add_card(Card("Diamonds", "Nine"))
        result = self.hand.combination_value()
        self.assertEqual(result, 1)

    def temp(self):
        self.hand.test_hand()

if __name__=='__main__':
    unittest.main()
