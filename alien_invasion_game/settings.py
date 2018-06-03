class Settings():
    # A class which stores all settings for alien invasion
    def __init__(self):
        # Initialize game settings
        self.bg_color = (50, 50, 50)
        self.screen_height = 1200
        self.screen_width = 800
        self.caption = "Alien Invasion"

        # Ship settings
        self.speed_factor = 1.5

        #Bullet setting
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (240, 240, 240)
        self.bullet_amount = 4

