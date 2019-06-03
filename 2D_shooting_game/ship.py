import pygame


class Ship:
    def __init__(self, screen):  # screen is need to put Ship class into the game window
        """initialize the ship and set its starting position"""
        self.screen = screen

        # load ship image and get its rect
        self.image = pygame.image.load('img/0.jpg')  # this function returns a surface, which is represented by the image it loads
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()  # we are trying to put the ship_rect into screen_rect

        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
