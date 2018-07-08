class GameStats():
    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.game_active = False