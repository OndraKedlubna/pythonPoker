import unittest
from mock import patch
from cardpackage.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_validate_input_to_many_card(self):
        result = self.game._Game__validate_input('1234', 3, 5)
        self.assertEqual(result, False)

    def test_validate_input_bad_character(self):
        result = self.game._Game__validate_input('12k', 3, 5)
        self.assertEqual(result, False)

    def test_validate_input_bad_number(self):
        result = self.game._Game__validate_input('126', 3, 5)
        self.assertEqual(result, False)

    def test_validate_duplicity(self):
        result = self.game._Game__validate_input('11', 3, 5)
        self.assertEqual(result, False)

    def test_validate_good(self):
        result = self.game._Game__validate_input('142', 3, 5)
        self.assertEqual(result, True)

    def test_init(self):
        self.assertEqual(5, len(self.game.hand))
        self.assertEqual(47, len(self.game.deck))

    @patch('cardpackage.game.get_input', return_value='143')
    def test_test(self, input):
        self.game.change_card()



if __name__=='__main__':
    unittest.main()
