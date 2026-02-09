from board import Board

from money import Money
from players import Players

class BusinessGame:
    """ Overall class to manage the game assets and behaviour"""

    def __init__(self, cells_string, dice_output, n_players):
        """Initialise the game and create game resources."""
        self.dice_output = dice_output
        self.cells_string = cells_string
        # Preapre board
        self.board = Board(self, self.cells_string)

    def display_result(self):
        """Display each palyer's total worth."""
        