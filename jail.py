class Jail:
    """Overall class to manage the cell type J - Jail"""

    def __init__(self):
        """Initialise attributes of this class."""
        self.fine = 150

    def if_not_enough_money(self):
        """Skip player's turn if not enough money for fine"""
        