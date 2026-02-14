from player import Player
from enum import Enum

class CellType(Enum):
    NORMAL = 0
    JAIL = -150
    TREASURE = 200
    HOTEL = 200

class Cell:
    def __init__(self, name, cell_type=CellType.NORMAL):
        self.name = name
        self.cell_type = cell_type
        self.impact_value = self.cell_type.value

class Treasure(Cell):
    def __init__(self, name="Treasure"):
        super().__init__(name, CellType.TREASURE)
        self.value = 200

class Jail(Cell):
    def __init__(self, name="Jail"):
        super().__init__(name, CellType.JAIL)
        self.fine = 150

    # def if_not_enough_money(self):
        
class Hotel(Cell):
    def __init__(self, name: str):
        super().__init__(name, CellType.HOTEL)
        self.price = self.cell_type.value
        self.rent = 50

        # flag and owner in one variable
        self.owner = None
    
    # def set_owner(self):

    # def charge_guest(self):
