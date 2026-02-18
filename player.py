class Player:
    """Overall class to manage player and their money."""

    def __init__(self, name):
        """Initialise Player attributes."""
        self.name = name
        self.cash = 1000
        self.hotels_owned = [] # list of hotel objects owned by player
        self.max_turns = 10
        self.position = 0
    
    @property
    def net_worth(self):
        hotels_value = sum(hotel.price for hotel in self.hotels_owned)
        return hotels_value + self.cash
    
    @classmethod
    def create_players(cls, n_players):
        # cls refers to Player class 
        # that is it is a method of the class and not  of a specific player instance
        return [Player(f"Player-{i+1}") for i in range(n_players)] # list of player objects indentified by their name