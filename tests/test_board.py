from board import Board
import unittest


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def set_up_draw(self):
        """Set up a board with a tied position."""
        self.board.add_player_move(1, 8)
        self.board.add_player_move(2, 5)
        self.board.add_player_move(1, 7)
        self.board.add_player_move(2, 6)
        self.board.add_player_move(1, 2)
        self.board.add_player_move(2, 0)
        self.board.add_player_move(1, 3)
        self.board.add_player_move(2, 4)
        self.board.add_player_move(1, 1)

    def test_default_board_has_3_rows(self):
        self.assertEqual(3, len(self.board.board))

    def test_default_board_has_3_columns(self):
        self.assertEqual(3, len(self.board.board[2]))

    def test_new_board_has_given_number_of_rows(self):
        size = 4
        board = Board(size)
        self.assertEqual(size, len(board.board))

    def test_new_board_given_given_number_of_columns(self):
        size = 4
        board = Board(size)
        self.assertEqual(size, len(board.board[3]))

    def test_move_added_to_correct_cell(self):
        self.board.add_player_move(1, 7)
        self.assertEqual(1, self.board.board[2][1])

    def test_move_not_added_to_incorrect_row(self):
        self.board.add_player_move(1, 0)
        self.assertEqual(0, self.board.board[1][0])

    def test_move_higher_than_last_cell_number_fails(self):
        result = self.board.add_player_move(1, 9)
        self.assertFalse(result)

    def test_move_fails_if_cell_already_filled(self):
        self.board.add_player_move(1, 0)
        result = self.board.add_player_move(2, 0)
        self.assertFalse(result)

    def test_horizontal_winner_found_in_first_row(self):
        self.board.add_player_move(1, 0)
        self.board.add_player_move(2, 3)
        self.board.add_player_move(1, 1)
        self.board.add_player_move(2, 4)
        self.board.add_player_move(1, 2)
        self.assertEqual(1, self.board.find_horizontal_winner())

    def test_horizontal_winner_found_in_last_row(self):
        self.board.add_player_move(1, 6)
        self.board.add_player_move(2, 3)
        self.board.add_player_move(1, 7)
        self.board.add_player_move(2, 4)
        self.board.add_player_move(1, 8)
        self.assertEqual(1, self.board.find_horizontal_winner())

    def test_no_horizontal_winner_found_in_empty_board(self):
        self.assertEqual(0, self.board.find_horizontal_winner())

    def test_no_horizontal_winner_found_in_draw(self):
        self.set_up_draw()
        self.assertEqual(0, self.board.find_horizontal_winner())