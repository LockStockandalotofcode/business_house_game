class Player:

    def __init__(self, name, initial_money=1000):
        self.name = name
        self.cash = initial_money
        self.hotels = [] # list of hotel objects owned by player
        self.max_turns = 10
        self.position = 0
    
    @property
    def net_worth(self):
        return self.cash + sum(hotel.price for hotel in self.hotels)
    
    def buy_hotel(self, hotel):
        self.cash -= hotel.price
        self.hotels.append(hotel)
        hotel.owner = self

    def pay_rent(self, owner, rent_amount):
        self.cash -= rent_amount
        owner.cash += rent_amount
    
class PlayerCreator:
    @staticmethod
    def create_players(n_players):
        return [Player(f"Player-{i+1}") for i in range(n_players)] # list of player objects indentified by their name