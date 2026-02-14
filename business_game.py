from board import Board
from player import Player

class BusinessGame:
    def __init__(self, cells_string, dice_output_list, n_players):
        self.dice_output_list = dice_output_list
    
        self.cells_string = cells_string
        # create board
        self.board = Board(self)

        # Create players
        self.n_players = n_players
        self.players = []
        for n in range(self.n_players):
            name = f"Player-{n+1}"
            self.players[n] = Player(name)
            self.players[n].money = 1000

        # Start the game in inactive state
        self.game_active = False

    def run_game(self):
        while True:
            if self.game_active:
                self.update_stats()

    def update_stats(self):
        # Update positions and accounts of players as game progresses.
        # take turns as per dice output
        for turn_index, dice_output in enumerate(self.dice_output_list):
            curr_player = (turn_index + 1) % 3
            position = self.update_position(dice_output, curr_player)
            self.get_cell_at(position)

    def update_position(self, dice_output, curr_player):
        for dice_output in self.dice_output_list:
            position = self.board.move_cell(dice_output, curr_player)
            return position
            
        

    