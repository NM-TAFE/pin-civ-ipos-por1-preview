from player import Player

class BoardError(Exception):
    """Base class for all board errors
    """
    
class InvalidPositionError(BoardError):
    """Called when a position requested is out of bounds
    """

class PositionOccupiedError(BoardError):
    """Called when a position requested is already occupied
    """

    
    
class Board:
    def __init__(self, size = 3) -> None:
        self.size = size
        self.grid = self._create_2d_grid()
        
    def _create_2d_grid(self) -> None:
        ...
        
    def is_full(self) -> bool:
        ...
        
        
    def is_position_occupied(self, row, col) -> bool:
        return self.grid[row][col] is not None
    
    def make_move(self, row, col, player) -> None:
        if 0 > row > self.size or 0 > col > self.size:
            raise InvalidPositionError("Invalid position")
        if self.is_position_occupied(row, col):
            raise PositionOccupiedError("Position already occupied")
            
        self.grid[row][col] = player
    
    def get_winner(self) -> None | Player :
        return self._has_horizontal_winner() or self._has_vertical_winner() or self._has_diagonal_winner()

    
    def _has_horizontal_winner(self) -> None | Player:
       ...

    def _has_vertical_winner(self) -> None | Player:
        ...
    
    def _has_diagonal_winner(self) -> None | Player:
        ...
    
    def __str__(self) -> str:
        return "\n".join([str(row) for row in self.grid])