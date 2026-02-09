from jail import Jail
from treasure import Treasure
from hotel import hotel

class Board:
    """Class to manage the game board."""

    def __init__(self, b_game):
        """Initialise board attributes."""
        self.b_game = b_game

        self.cells_string = b_game.cells_string
        # Clean and prepare cells
        # Turns "E,E,J..." into ["E", "E", "J", ...]
        self.cells = self.cells_string.split(',')

        self.dice_output = b_game.dice_output

    def move_cell(self):
        """Move position as per dice output, keeping within bounds of the board."""
