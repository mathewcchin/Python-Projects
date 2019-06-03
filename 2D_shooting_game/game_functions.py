import sys
import pygame


def check_events():
    """response to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(game_settings, screen, ship):
    """Update items on the screen and draw new screen"""
    # screen.fill(game_settings.bg_color)
    bg = pygame.image.load('img/bg.jpg')
    screen.blit(bg, (0, 0))
    ship.blitme()

    # draw the updated screen
    pygame.display.flip()
