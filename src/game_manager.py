"""
Tic-Tac-Toe game manager. This provides a GameManager class which contains the
basic program flow and gameplay loop for a game of Tic-Tac-Toe.
"""

from board import Board
from console_ui import ConsoleUI


class GameManager:
    """
    Tic-Tac-Toe game manager class. This provides the basic program flow and
    gameplay loop for a game of Tic-Tac-Toe.
    """

    def __init__(self):
        """Initialise the Tic-Tac-Toe game"""
        self.player_map = {
            0: ' ',
            1: 'X',
            2: 'O',
        }
        self.current_player = 1
        self.board = Board()
        self.ui = ConsoleUI(self.player_map)

    def main(self):
        """The main gameplay loop for the Tic-Tac-Toe game"""
        # Game loop
        while True:
            # Print board
            print(self.board.board[0][0], "|", self.board.board[0][1], "|", self.board.board[0][2])
            print("---------")
            print(self.board.board[1][0], "|", self.board.board[1][1], "|", self.board.board[1][2])
            print("---------")
            print(self.board.board[2][0], "|", self.board.board[2][1], "|", self.board.board[2][2])
            print()

            # Check for win
            winner = self.board.find_winner()
            if winner:
                self.ui.announce_winner(winner)
                return

            # Check for tie
            if self.board.is_board_full():
                self.ui.announce_tie()
                return

            # Get next move
            while True:
                player = self.player_map[self.current_player]
                move = input("Next move for player " + player + " (0-8): ")
                if move.isdigit() and 0 <= int(move) and self.board.add_player_move(self.current_player, int(move)):
                    break
                else:
                    self.ui.invalid_move_error()

            # Switch players
            if self.current_player == len(self.player_map) - 1:
                self.current_player = 1
            else:
                self.current_player += 1


if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.main()