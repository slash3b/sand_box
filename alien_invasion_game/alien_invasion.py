#!/usr/bin/env python3

import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    pygame.init()
    settings = Settings()
    pygame.display.set_caption(settings.caption)
    resolution = (settings.screen_width, settings.screen_height)
    screen = pygame.display.set_mode(resolution)

    ship = Ship(screen, settings)
    aliens = Group()
    bullets = Group()
    gf.create_fleet(settings, screen, ship, aliens)

    while True:
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(settings, aliens)
        gf.update_screen(settings, screen, ship, aliens, bullets)

run_game()
