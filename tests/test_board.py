from board import Board
import unittest


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

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