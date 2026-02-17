from player import Player

class BusinessGame:
    def __init__(self, cells_string, dice_output_list, n_players):
        self.dice_output_list = dice_output_list
        # create board
        self.board = Board(cells_string)
        # create players
        self.n_players = n_players
        self.players = [Player(f"Player-{i+1}") for i in range(n_players)] # list of player objects indentified by their name

    def run_game(self):
        print(f"Starting game with {self.n_players} players:")
        for turn_index, dice_output in enumerate(self.dice_output_list):
            # Determine current player
            player_index = (turn_index) % self.n_players
            curr_player = self.players[player_index]

            # Move the player
            old_pos = curr_player.position
            new_pos = self.board.move_player(dice_output, curr_player)

            # maintaining Log for all turns
            print(f"Turn: {turn_index + 1} Striker: {curr_player.name} got dice value: {dice_output} landed on cell type:{self.board.get_cell_at(new_pos)}" "\n"
                  f"\tMoved from {old_pos} to {new_pos}")

class Board:
    def __init__(self, cells_string):
        self.cells = [c.strip() for c in cells_string.split(',')]

    def move_player(self, dice_output, player):
        # calculate new position with wrap around logic once a round trip of board is completed
        # given dice_output and the corresponding player
        # position of palyer is accessed with its attribute
        player.position = (player.position + dice_output) % len(self.cells)
        return player.position

    def get_cell_at(self, position):
        return self.cells[position-1]
    
if __name__ == "__main__":
    cells = "E,E,J,H,E,T,J,T,E,E,H,J,T,H,E,E,J,H,E,T,J,T,E,E,H,J,T,H,J,E,E,J,H,E,T,J,T,E,E,H,J,T,E,H,E0"
    dice = [4,4,4,6,7,8,5,11,10,12,2,3,5,6,7,8,5,11,10,12,2,3,5,6,7,8,5,11,10,12]
    
    game = BusinessGame(cells, dice, n_players=3)
    game.run_game()