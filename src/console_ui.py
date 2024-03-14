"""
A console UI for a Tic-Tac-Toe game.
Author: Emily Boegheim
"""

from utilities import get_int_from_input


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
        self.invalid_move_error = "Invalid move, try again."

    def display_2d_board(self, board_data, horizontal_separator=" | ",
                         vertical_separator="-"):
        """
        Display a 2-dimensional data structure as a game grid, using the
        player_map dictionary to represent the data appropriately.
        :param board_data: a 2-dimensional data structure containing the game
            board data.
        :param horizontal_separator: the separator to use between columns.
        :param vertical_separator: the separator to use between rows. This will
            be repeated to fill the full board width, so it should be a single
            character.
        """
        board_height = len(board_data)
        board_width = len(board_data[0])
        for row_index in range(0, board_height):
            # Print a row of the board.
            for column_index in range(0, board_width):
                cell_data = board_data[row_index][column_index]
                cell_content = self.player_map[cell_data]
                if column_index < board_width - 1:
                    print(f"{cell_content}{horizontal_separator}", end='')
                else:
                    print(cell_content)
            # Print a row separator.
            if row_index < board_height - 1:
                separator_width = (len(horizontal_separator))
                board_visual_width = (board_width*(separator_width + 1) -
                                      separator_width)
                print(vertical_separator * board_visual_width)
        print()

    def get_current_player_move(self, current_player, max_move):
        """
        Prompt the current player for their move and return the input as an
        integer.
        :param current_player: The current player, represented as an integer.
        :param max_move: The highest move allowable on the board.
        :returns: The player's selected move as an integer.
        """
        player_icon = self.player_map[current_player]
        prompt = f"Next move for player {player_icon} (0-{max_move}): "
        error = self.invalid_move_error
        return get_int_from_input(prompt, error)

    def announce_winner(self, winner: int):
        """
        Announce the winner of the Tic-Tac-Toe game.
        :param winner: the winning player, represented as an integer.
        """
        print(f"Player {self.player_map[winner]} wins!")

    def announce_tie(self):
        """Announce that the game has ended in a tie."""
        print("It's a tie!")

    def show_invalid_move_error(self):
        """Inform the player that their selected move is invalid."""
        print(self.invalid_move_error)
