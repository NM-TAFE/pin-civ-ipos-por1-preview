"""
Tic-Tac-Toe game manager. This provides a GameManager class which contains the
basic program flow and gameplay loop for a game of Tic-Tac-Toe.
"""


class GameManager:
    """
    Tic-Tac-Toe game manager class. This provides the basic program flow and
    gameplay loop for a game of Tic-Tac-Toe.
    """

    def __init__(self):
        """Initialise the Tic-Tac-Toe game"""
        self.p1 = "X"
        self.p2 = "O"
        self.empty = " "
        self.board = [self.empty] * 9

    def main(self):
        """The main gameplay loop for the Tic-Tac-Toe game"""
        # Game loop
        while True:
            # Print board
            print(self.board[0], "|", self.board[1], "|", self.board[2])
            print("---------")
            print(self.board[3], "|", self.board[4], "|", self.board[5])
            print("---------")
            print(self.board[6], "|", self.board[7], "|", self.board[8])
            print()

            # Check for win
            win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
            for wc in win_conditions:
                if self.board[wc[0]] == self.board[wc[1]] == self.board[wc[2]] != self.empty:
                    print("Player", self.board[wc[0]], "wins!")
                    exit(0)

            # Check for tie
            if self.empty not in self.board:
                print("It's a tie!")
                exit(0)

            # Get next move
            while True:
                player = self.p1 if self.board.count(self.empty) % 2 == 1 else self.p2
                move = input("Next move for player " + player + " (0-8): ")
                if move.isdigit() and 0 <= int(move) <= 8 and self.board[int(move)] == self.empty:
                    self.board[int(move)] = player
                    break
                else:
                    print("Invalid move, try again.")


if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.main()