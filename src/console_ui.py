"""
A console UI for a Tic-Tac-Toe game.
Author: Emily Boegheim
"""

class ConsoleUI:
    """A console UI for a Tic-Tac-Toe game."""
    def __init__(self, player_map: dict):
        """
        Initialise the UI by recording the mapping between player number and
        symbol/piece, to use when displaying the board or printing messages.
        This should also include the representation of an empty space.
        :param player_map: a dictionary with the keys 0 through the maximum
            number of players and values containing the characters to use as
            representations of each player. 0 is a special value representing
            an empty space.
        """
        self.player_map = player_map

    def announce_winner(self, winner: int):
        """
        Announce the winner of the Tic-Tac-Toe game.
        :param winner: the winning player, represented as an integer.
        """
        print(f"Player {self.player_map[winner]} wins!")

    def announce_tie(self):
        """Announce that the game has ended in a tie."""
        print("It's a tie!")

    def invalid_move_error(self):
        """Inform the player that their selected move is invalid."""
        print("Invalid move, try again.")
