class Players:
    """Overall class to manage players."""

    def __init__(self, b_game):
        """Initialise Player attributes."""
        self.b_game = b_game
        self.n_players = b_game.n_players
        self.max_turns = 10