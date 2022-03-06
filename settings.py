class Settings:
    # A class to store all settings for Alien Invasion.

    def __init__(self):
        # Game settings
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 2

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 4

        # Alien settings
        self.alien_speed = 0.1
        self.fleet_drop_speed = 1
        # Fleet direction 1 represents right, -1 represents left
        self.fleet_direction = 1
