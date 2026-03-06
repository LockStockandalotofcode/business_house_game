from cell import EmptyCell, Treasure, Jail, Hotel
from dice import Dice

class Board:
    def __init__(self, cells_string, players):
        # build list of actual cell objects as per different cell types
        # Values below are classes and not instances
        self.mapping = {'E': EmptyCell, 'J': Jail, 'H': Hotel, 'T': Treasure}
        self.cells = self.build_board(cells_string)
        self.players = players

    def build_board(self, cells_string):
        string_to_list = cells_string.split(',')
        board_layout = []

        for _, char in enumerate(string_to_list):
            char = char.strip()[0]
            cell_class = self.mapping.get(char, EmptyCell)
            obj = cell_class()
            board_layout.append(obj)

        return board_layout
    
    def take_turn(self, dice_output, turn_index):
            curr_player = self.get_current_player(turn_index)
            # old_pos = curr_player.position
            new_pos = self.move_player(dice_output, curr_player)
            cell = self.get_cell_at(new_pos)
            self.handle_turn_logic(curr_player, cell)

    def get_current_player(self, turn_index):
        n = len(self.players)
        # Determine current player
        player_index = (turn_index) % n
        curr_player = self.players[player_index]

        return curr_player

    def move_player(self, dice_output, curr_player):
        # calculate new position with wrap around logic once a round trip of board is completed
        # given dice_output and the corresponding player
        # position of palyer is accessed with its attribute
        curr_player.position = (curr_player.position + dice_output) % len(self.cells)
        return curr_player.position

    def get_cell_at(self, position):
        return self.cells[position-1]
        
    def handle_turn_logic(self, player, cell):
        cell.apply(player)

    def display_winner(self):
        # x is a player object in self.players list
        self.players.sort(key=lambda x: x.net_worth, reverse=True)
        for p in self.players:
            print(f"{p.name} has total worth {p.net_worth}")
