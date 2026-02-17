
from cell import Cell, Treasure, Jail, Hotel

class Board:
    def __init__(self, cells_string):
        # build list of actual cell objects as per different cell types
        # Values below are classes and not instances
        self.mapping = {'E': Cell, 'J': Jail, 'H': Hotel, 'T': Treasure}
        self.cells_string = cells_string
        self.cells = self.build_board()

    def build_board(self):
        string_to_list = self.cells_string.split(',')
        board_layout = []

        for i, char in enumerate(string_to_list):
            char = char.strip()[0]
            cell_class = self.mapping.get(char, Cell)
            # Create the cell object as per character
            if char == 'H':
                obj = cell_class("Hotel")
            else:
                obj = cell_class()

            board_layout.append(obj)

        return board_layout

    def move_player(self, dice_output, player):
        # calculate new position with wrap around logic once a round trip of board is completed
        # given dice_output and the corresponding player
        # position of palyer is accessed with its attribute
        player.position = (player.position + dice_output) % len(self.cells)
        return player.position

    def get_cell_at(self, position):
        return self.cells[position-1]
    