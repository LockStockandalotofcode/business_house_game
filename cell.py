from player import Player
from enum import Enum

class CellType(Enum):
    NORMAL = 0
    JAIL = -150
    TREASURE = 200
    HOTEL = 200

class Cell:
    def __init__(self, name, cell_type: CellType):
        """Basic class for all cells."""
        self.name = name
        self.cell_type = cell_type
        self.impact_value = self.cell_type.value

class Jail:
    """Overall class to manage the cell type J - Jail"""

    def __init__(self):
        """Initialise attributes of this class."""
        self.fine = 150

    def if_not_enough_money(self):
        """Skip player's turn if not enough money for fine"""
        
class Hotel(Cell):
    """Overall class to manage Hotels cell type."""

    def __init__(self, name: str):
        """Initialise Hotel attributes."""
        super().__init__(name, self.cell_type.HOTEL)
        self.price = self.cell_type.value
        self.rent = 50

        # flag and owner in one variable
        self.owner = None
    
    def make_owner(self):
        """Designate owner to hotel, charge him for buying the hotel."""


    def charge_guest(self):
        """Charge guest for a pre-owned hotel."""
