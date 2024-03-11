"""
Tic-Tac-Toe game manager. This provides a GameManager class which contains the
basic program flow and gameplay loop for a game of Tic-Tac-Toe.
"""

from board import Board


class GameManager:
    """
    Tic-Tac-Toe game manager class. This provides the basic program flow and
    gameplay loop for a game of Tic-Tac-Toe.
    """

    def __init__(self):
        """Initialise the Tic-Tac-Toe game"""
        self.players = {
            1: 'X',
            2: 'Y',
        }
        self.current_player = 1
        self.board = Board()

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
                print(f"Player {winner} wins!")
                return

            # Check for tie
            if self.board.is_board_full():
                print("It's a tie!")
                return

            # Get next move
            while True:
                player = self.players[self.current_player]
                move = input("Next move for player " + player + " (0-8): ")
                if move.isdigit() and 0 <= int(move) and self.board.add_player_move(self.current_player, int(move)):
                    break
                else:
                    print("Invalid move, try again.")

            # Switch players
            if self.current_player == len(self.players):
                self.current_player = 1
            else:
                self.current_player += 1


if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.main()