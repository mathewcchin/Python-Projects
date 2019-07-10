import pygame, sys
from setting import Settings
import game_functions as gf
from ship import Ship

pygame.init()  # initialize the background things needed by pygame
game_settings = Settings()  # create an object of Setting class, and access the attributes

screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))  # create a game window
pygame.display.set_caption(game_settings.caption)  # set the caption of the game window


def welcome_screen():
    # Game sounds:
    # Main Menu (Royalty Free Soundtrack):
    # Power Bots Loop
    # by DL-Sounds
    # https://www.dl-sounds.com/royalty-free/power-bots-loop/
    pygame.mixer.music.load("img/Power Bots Loop.wav")
    pygame.mixer.music.play(-1)

    # key click noise:
    # Menu_Navigate_03.wav
    # by LittleRobotSoundFactory
    # https://freesound.org/people/LittleRobotSoundFactory/sounds/270315/
    key_sound = pygame.mixer.Sound("img/key_sound.wav")

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    grey = (192,192,192)

    # Game Fonts
    font = game_settings.font

    # Game FPS
    clock = pygame.time.Clock()
    FPS = 30

    # Main Menu Loop
    selected = "start"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if selected == "settings" and event.key == pygame.K_UP:
                    key_sound.play()
                    selected = "start"

                elif selected == "quit" and event.key == pygame.K_UP:
                    key_sound.play()
                    selected = "settings"

                elif selected == "start" and event.key == pygame.K_DOWN:
                    key_sound.play()
                    selected = "settings"

                elif selected == "settings" and event.key == pygame.K_DOWN:
                    key_sound.play()
                    selected = "quit"

                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        run_game()
                    if selected == "settings":
                        user_settings()
                    if selected == "quit":
                        sys.exit()

        # Main Menu UI
        menu = pygame.image.load('img/bg.jpg')
        screen.blit(menu, (0, 0))

        title = text_format("Alien Invasion", font, 90, black)
        if selected == "start":
            text_start = text_format("START", font, 75, white)
        else:
            text_start = text_format("START", font, 75, black)

        if selected == "settings":
            text_settings = text_format("SETTINGS", font, 75, white)
        else:
             text_settings = text_format("SETTINGS", font, 75, black)

        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, black)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        settings_rect = text_settings.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (game_settings.screen_width / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_start, (game_settings.screen_width / 2 - (start_rect[2] / 2), 300))
        screen.blit(text_settings, (game_settings.screen_width / 2 - (settings_rect[2] / 2), 350))
        screen.blit(text_quit, (game_settings.screen_width / 2 - (quit_rect[2] / 2), 400))
        pygame.display.update()
        clock.tick(FPS)


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText

def user_settings():
    print("its working")
    #pygame.draw.rect(screen, (200, 150, 100, 50))




def run_game():
    """ Initialize game and create a screen object"""

    # make a ship, pass:
    #   -the surface on which pygame draws the ship
    #   -game_settings (which contains settings for the ship)
    ship = Ship(screen, game_settings)


    # start the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        # using a function in game_functions
        gf.check_events(ship)
        ship.update()

        # update screen and draw it
        gf.update_screen(game_settings, screen, ship)


welcome_screen()
