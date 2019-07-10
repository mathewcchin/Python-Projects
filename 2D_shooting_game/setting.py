class Settings:
    """a class to store all settings for the game"""

    def __init__(self):
        """initialize game seeting attributes"""
        # screen settings
        self.caption = "2D Shooting Game: Alien Invasion"
        self.screen_width = 1050
        self.screen_height = 690
        self.bg_color = (230, 230, 230)  # create a tuple containing the RGB background color

        # ship settings
        self.ship_speed_factor = 3  # step size of ship movement between each screen drawing
        self.ship_speed_acceleration_ratio = 10  # maximum acceleration ratio (times of ship_speed_factor)

        # welcome menu settings
        self.font = "img/INVASION2000.TTF"
  
