class Settings:
    """a class to store all settings for the game"""

    def __init__(self):
        """initialize game seeting attributes"""
        # screen settings
        self.caption = "2D Shooting Game"
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # create a tuple containing the RGB background color
