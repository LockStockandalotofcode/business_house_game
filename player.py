class Player:
    """Overall class to manage player and their money."""

    def __init__(self, name, initial_money=1000):
        """Initialise Player attributes."""
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
    
    @classmethod
    def create_players(cls, n_players):
        # cls refers to Player class 
        # that is it is a method of the class and not  of a specific player instance
        return [Player(f"Player-{i+1}") for i in range(n_players)] # list of player objects indentified by their name