from cell import Cell
from player import Player

class Board:
    """Class to manage the game board."""

    def __init__(self, b_game):
        """Initialise board attributes."""
        super.__init__(b_game)

        self.cells_string = b_game.cells_string
        # Clean and prepare cells
        # Turns "E,E,J..." into ["E", "E", "J", ...]
        self.cells = self.cells_string.split(',')

        self.dice_output = b_game.dice_output

    def move_cell(self, dice_output, old_position):
        """Move position as per dice output, keeping within bounds of the board."""
        next_position = old_position + self.dice_output
        next_position = next_position % len(self.cells)