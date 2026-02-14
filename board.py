from cell import Cell
from player import Player

class Board:
    def __init__(self, b_game):
        super.__init__(b_game)

        self.cells_string = b_game.cells_string
        # Clean and prepare cells
        # Turns "E,E,J..." into ["E", "E", "J", ...]
        self.cells = self.cells_string.split(',')
        self.players = b_game.players

        self.dice_output_list = b_game.dice_output_list

    def move_cell(self, dice_output, curr_player):
        curr_position = curr_player.position
        curr_position += dice_output
        curr_position %= len(self.cells)
        curr_player.position = curr_position
        return curr_position
    
    def get_cell_at(self, position):
        return self.cells[position]