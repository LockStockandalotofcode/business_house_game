from player import PlayerCreator
from board import Board
from dice import Dice

class BusinessGame:
    def __init__(self, cells_string, dice_output_list, n_players):
        self.board = Board(cells_string)
        self.dice = Dice(dice_output_list)
        self.players = PlayerCreator.create_players(n_players)

    def run_game(self):        
        print(f"Starting game with {len(self.players)} players:")

        for turn_index, roll in enumerate(self.dice.dice_output_list):
            # determine current player
            player = self.players[(turn_index) % len(self.players)]
            # tell board to process the turn for this player
            if roll is not None:
                self.board.process_turn(player, roll)

        self._display_winner()

    def _display_winner(self):
        # x is a player object in self.players list
        players.sort(key=lambda x: x.net_worth, reverse=True)
        for p in self.players:
            print(f"{p.name} has total worth {p.net_worth}")























if __name__ == "__main__":
    cells = "H,H,J,H,E,T,J,T,J,E,H,J,T,H,E,E,J,H,E,T,J,T,E,E,H,J,T,H,J,H,E,J,H,E,T,J,T,J,E,H,J,T,E,H,E"
    dice = [1,2,4,1,7,8,5,11,10,12,2,3,5,6,7,8,5,11,10,12,2,3,5,6,7,8,5,11,10,12]
    
    game = BusinessGame(cells, dice, n_players=3)
    game.run_game()
    print("-" * 10)

if __name__ == "__main__":
    cells = "E,E,J,H,E,T,J,T,E,E,H,J,T,H,E,E,J,H,E,T,J,T,E,E,H,J,T,H,J,E,E,J,H,E,T,J,T,E,E,H,J,T,E,H,E0"
    dice = [4,4,4,6,7,8,5,11,10,12,2,3,5,6,7,8,5,11,10,12,2,3,5,6,7,8,5,11,10,12]
    
    game = BusinessGame(cells, dice, n_players=3)
    game.run_game()
    print("-" * 10)

if __name__ == "__main__":
    cells = "J,H,J,H,E,T,J,T,J,E,H,J,T,H,E,E,J,H,E,T,J,T,E,E,H,J,T,H,J,H,E,J,H,E,T,J,T,J,E,H,J,T,E,H,E"
    dice = [1,2,4,1,7,8,5,11,10,9,2,6,1,3,7,9,5,11,10,12,2,3,5,6,7,8,5,11,10,12]
    
    game = BusinessGame(cells, dice, n_players=3)
    game.run_game()