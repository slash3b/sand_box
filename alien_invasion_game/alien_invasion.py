#!/usr/bin/env python3

import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    pygame.init()
    # pygame.mixer.music.load('music/space_police.mp3')
    # pygame.mixer.music.play(0)

    settings = Settings()

    resolution = (settings.screen_height, settings.screen_width)
    screen = pygame.display.set_mode(resolution)
    ship = Ship(screen, settings)
    aliens = Group()
    bullets = Group()
    gf.create_fleet(settings, screen, aliens)

    pygame.display.set_caption(settings.caption)

    while True:
        gf.check_events(settings, screen, ship, bullets)
        gf.update_bullets(bullets)
        ship.update()
        gf.update_screen(settings, screen, ship, aliens, bullets)

run_game()
