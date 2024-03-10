"""Provides a class representing a Tic-Tac-Toe game board and its state"""


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
        row = [self.empty] * size
        self.board = [row] * size