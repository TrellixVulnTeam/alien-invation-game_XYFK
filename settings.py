class Settings:

    def __init__(self):
        """
        Initialize the setting of game and this block
        will execute first time after the object initilized
        """

        # screen setting
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)  # RGB CODE

        # ship setting
        self.ship_speed = 1.5
        self.ship_limit = 3

        # bullet setting
        self.bullet_speed = 1.0
        self.bulled_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # RGB CODE
        self.bullet_allowed = 10

        # alien setting
        self.alien_speed = 0.2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 => right; -1 left;
