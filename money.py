class Money:
    """Overall class to manage money of the players in game."""

    def __init__(self, b_game):
        """Initialise attributes."""
        self.n_players = b_game.n_players

        self.initial_money = 1000