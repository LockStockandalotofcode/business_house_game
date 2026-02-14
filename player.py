class Player:
    """Overall class to manage player and their money."""

    def __init__(self, name):
        """Initialise Player attributes."""
        self.name = name
        self.money = 1000
        self.max_turns = 10
        self.position = 0
    
        
    # def current_position(self, position):

    # def add_money(self, amount):
    #     self.money += amount

    # def spend_money(self, amount):
    #     if self.money >= amount:
    #         self.money -= amount
    #     else:
    #         print("Not enough money")