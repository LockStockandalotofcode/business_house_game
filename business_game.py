from player import Player
from board import Board

class BusinessGame:
    def __init__(self, cells_string, dice_output_list, n_players):
        self.dice_output_list = dice_output_list
        # create players
        self.players = Player.create_players(n_players)
        # create board
        self.board = Board(cells_string, self.players)

    def run_game(self):
        print(f"Starting game with {len(self.players)} players:")
        for turn_index, dice_output in enumerate(self.dice_output_list):
            self.board.take_turn(dice_output, turn_index, self.players)

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