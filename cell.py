from abc import ABC, abstractmethod

class Cell(ABC):
    @abstractmethod
    def apply(self, player):
        pass

# child classes
class EmptyCell(Cell):
    def apply(self, player):
        pass

class Jail(Cell):
    def __init__(self, fine=150):
        self.fine = fine
    
    def apply(self, player):
        player.cash -= self.fine

class Treasure(Cell):
    def __init__(self, value=200):
        self.value = value
    
    def apply(self, player):
        player.cash += self.value

class Hotel(Cell):
    def __init__(self, price=200, rent=50):
        self.price = price
        self.rent = rent
        self.owner = None

    def apply(self, player):
        if self.owner is None and player.cash >= self.price:
            player.buy_hotel(self)
        elif self.owner != player:
            player.pay_rent(self.owner, self.rent)