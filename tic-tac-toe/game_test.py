from game import Game
import unittest


class test_game(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_is_board_clear_at_begginnig(self):
        expected_result = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.assertEqual(expected_result, self.game.board)

    def test_place_move_on_board(self):
        position = 1
        symbol = 'X'
        self.game._place_move_on_board(position, symbol)
        self.assertEqual(self.game.board[1], 'X')

    def test_is_position_free(self):
        position = 4
        self.assertTrue(self.game._is_position_free(position + 1))
        self.game._place_move_on_board(position, 'X')
        self.assertFalse(self.game._is_position_free(position + 1))


if __name__ == '__main__':
    unittest.main()
