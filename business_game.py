from player import Player
from board import Board
from cell import Cell, Treasure, Jail, Hotel

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
            cell = self.board.get_cell_at(new_pos)

            self.handle_turn_logic(curr_player, cell)

            # # for testing - maintaining Log for all turns
            # print(f"Turn: {turn_index + 1} Striker: {curr_player.name} got dice value: {dice_output} landed on cell type:{self.board.get_cell_at(new_pos)}" "\n" 
            #       f"\tMoved from {old_pos} to {new_pos}" )
            
            # for p in self.players:
            #     print(f"{p.name} is at cell number : {p.position} and has {p.cash} money left while total worth is {p.net_worth}.")
            # print("-" * 10)
        
    def display_winner(self):
        # x is a player object in self.players list
        self.players.sort(key=lambda x: x.net_worth, reverse=True)
        for p in self.players:
            print(f"{p.name} has total worth {p.net_worth}")

    def handle_turn_logic(self, player, cell):
        if isinstance(cell, Jail):
            player.cash -= cell.fine
        elif isinstance(cell, Treasure):
            player.cash += cell.value
        elif isinstance(cell, Hotel):
            if cell.owner is None and player.cash >= cell.price:
                # set owner, update player's assets
                player.cash -= cell.price
                cell.owner = player
                player.hotels_owned.append(cell)
            elif cell.owner:
                # transfer money from player to hotel owner
                player.cash -= cell.rent
                cell.owner.cash += cell.rent


if __name__ == "__main__":
    cells = "H,H,J,H,E,T,J,T,J,E,H,J,T,H,E,E,J,H,E,T,J,T,E,E,H,J,T,H,J,H,E,J,H,E,T,J,T,J,E,H,J,T,E,H,E"
    dice = [1,2,4,1,7,8,5,11,10,12,2,3,5,6,7,8,5,11,10,12,2,3,5,6,7,8,5,11,10,12]
    
    game = BusinessGame(cells, dice, n_players=3)
    game.run_game()
    game.display_winner()
    print("-" * 10)

if __name__ == "__main__":
    cells = "E,E,J,H,E,T,J,T,E,E,H,J,T,H,E,E,J,H,E,T,J,T,E,E,H,J,T,H,J,E,E,J,H,E,T,J,T,E,E,H,J,T,E,H,E0"
    dice = [4,4,4,6,7,8,5,11,10,12,2,3,5,6,7,8,5,11,10,12,2,3,5,6,7,8,5,11,10,12]
    
    game = BusinessGame(cells, dice, n_players=3)
    game.run_game()
    game.display_winner()
    print("-" * 10)

if __name__ == "__main__":
    cells = "J,H,J,H,E,T,J,T,J,E,H,J,T,H,E,E,J,H,E,T,J,T,E,E,H,J,T,H,J,H,E,J,H,E,T,J,T,J,E,H,J,T,E,H,E"
    dice = [1,2,4,1,7,8,5,11,10,9,2,6,1,3,7,9,5,11,10,12,2,3,5,6,7,8,5,11,10,12]
    
    game = BusinessGame(cells, dice, n_players=3)
    game.run_game()
    game.display_winner()