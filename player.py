class Player:
    """Overall class to manage player and their money."""

    def __init__(self, name, initial_money, max_turns=10):
        """Initialise Player attributes."""
        self.name = name
        self.money = initial_money
        self.max_turns = max_turns
        self.position = 0

    def current_position(self, position):
        """Updates current position of player, as game progresses."""

    def add_money(self, amount):
        """MEthod to add money into a player's account."""
        self.money += amount

    def spend_money(self, amount):
        """Method to debit money from a player's account."""
        if self.money >= amount:
            self.money -= amount
        else:
            print("Not enough money")