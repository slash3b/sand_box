import pygame

class Ship():
    def __init__(self, screen, settings):
        # Initialize the ship and set its starting position
        self.screen = screen
        self.settings = settings

        # Load the ship image
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value the ship's center
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    # update ship position baseed on flags
    def update(self):
        # print(self.rect.left < self.screen_rect.left)
        # print(self.rect.right < self.screen_rect.right)
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += self.settings.speed_factor
        if self.moving_up:
            self.rect.bottom -= self.settings.speed_factor

        self.rect.centerx = self.center


    

    def blitme(self):
        self.screen.blit(self.image, self.rect)