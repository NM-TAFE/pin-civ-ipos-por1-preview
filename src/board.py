"""Provides a class representing a Tic-Tac-Toe game board and its state"""

from utilities import all_items_in_collection_equal
import math


class Board:
    """A Tic-Tac-Toe game board and its current state"""

    def __init__(self, size=3):
        """
        Initialise the Tic-Tac-Toe game board with the given size (defaults to
        3).
        :param size: The size of the game board on each side (the board is
            always square)
        """
        self.size = size
        self.empty = 0
        self.board = []
        for row_number in range(0, size):
            row = [self.empty] * size
            self.board.append(row)

    def add_player_move(self, player, move):
        """
        Add the given player's chosen move to the board.
        :param player: the player making their move, represented as an integer
        :param move: the player's chosen move, represented as an integer
            between 0 and board size to the power of 2 (i.e. the number of
            cells on the board)
        :returns: True if the move was successful, False if the move is invalid
            based on the board state
        """
        # Check whether the move is outside the maximum bound of the board.
        if move >= self.size * self.size:
            return False

        # The move is provided as an integer from 0 to the total number of
        # cells on the board, so we need to convert it into indices for a
        # 2-dimensional data structure.
        row = math.floor(move / self.size)
        column = move % self.size

        # Check that the selected cell is empty.
        if self.board[row][column] != self.empty:
            return False

        self.board[row][column] = player
        return True

    def find_winner(self):
        """
        Check for all possible win conditions.
        :returns: the number of the winning player as an integer, or 0 if there
            is no winner.
        """
        winner = self.find_horizontal_winner()
        if winner != 0:
            return winner
        winner = self.find_vertical_winner()
        if winner != 0:
            return winner
        winner = self.find_diagonal_winner()
        return winner

    def find_horizontal_winner(self):
        """
        Check for win conditions on the horizontal/in the rows.
        :returns: the number of the winning player as an integer, or 0 if there
            is no winner.
        """
        for row in self.board:
            if row[0] != 0 and all_items_in_collection_equal(row):
                return True
        return False

    def find_vertical_winner(self):
        """
        Check for win conditions on the vertical/in the columns.
        :returns: the number of the winning player as an integer, or 0 if there
            is no winner.
        """
        for column in range(0, self.size):
            column_data = []
            for row in range(0, self.size):
                column_data.append(self.board[row][column])
            if all_items_in_collection_equal(column_data):
                return column_data[0]
        return 0

    def find_diagonal_winner(self):
        """
        Check for win conditions on the two longest diagonals (passing through
        the centre of the board).
        :returns: the number of the winning player as an integer, or 0 if there
            is no winner.
        """
        diagonal_data = []
        for row_and_column in range(0, self.size):
            diagonal_data.append(self.board[row_and_column][row_and_column])
        if all_items_in_collection_equal(diagonal_data):
            return diagonal_data[0]

        diagonal_data = []
        column = self.size - 1
        for row in range(0, self.size):
            diagonal_data.append(self.board[row][column])
            column -= 1
        if all_items_in_collection_equal(diagonal_data):
            return diagonal_data[0]
        return 0
