class GameStats:
    """Track statistics about the game."""
    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        #add high score
        self.highscore = 0
    def reset_stats(self):
        """initialize statistics that can change during the game"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1