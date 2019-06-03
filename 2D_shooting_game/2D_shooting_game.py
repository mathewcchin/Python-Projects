import sys
import pygame
from setting import Settings
from ship import Ship


def run_game():
    """ Initialize game and create a screen object"""

    pygame.init()  # initialize the background things needed by pygame
    game_settings = Settings()  # create an object of Setting class, and access the attributes

    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))  # create a game window
    pygame.display.set_caption(game_settings.caption)  # set the caption of the game window
    screen.fill(game_settings.bg_color)  # .fill() will take a tuple and set background color

    # make a ship
    ship = Ship(screen)

    # start the main loop for the game
    while True:
        # place ship
        ship.blitme()

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # make the most recently drawn screen visible
        pygame.display.flip()


run_game()
