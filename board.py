from cell import CellCreator

class Board:
    def __init__(self, cells_string):
        self.cells_layout = self.build_board(cells_string)

    def build_board(self, cells_string):
        string_to_list = cells_string.split(',')
        return [CellCreator.create_cell(char) for char in string_to_list]
    
    def process_turn(self, player, dice_output):
        landed_cell = self._move_player(dice_output, player)
        landed_cell.apply(player)

    def _move_player(self, dice_output, player):
        # helper method: calculate new position and return cell object
        # calculate new position with wrap around logic once a round trip of board is completed
        player.position = (player.position + dice_output) % len(self.cells_layout)
        return self.cells_layout[player.position - 1]
