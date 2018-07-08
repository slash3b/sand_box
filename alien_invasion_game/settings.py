class Settings():
    # A class which stores all settings for alien invasion
    def __init__(self):
        # Initialize game settings
        self.bg_color = (50, 50, 50)
        self.screen_height = 1300
        self.screen_width = 2700
        self.caption = "Alien Invasion"

        # Ship settings
        self.speed_factor = 1.5

        #Bullet setting
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (240, 240, 240)
        self.bullet_amount = 4

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.ship_limit = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.3

        # How quickly the alien point values increase over levels
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
        self.alien_points = 50

    def initialize_dynamic_settings(self):
        self.speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

    def increase_speed(self):
        self.speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
