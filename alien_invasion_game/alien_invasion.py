#!/usr/bin/env python3

import pygame
import game_functions as gf

from game_stats import GameStats
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    settings = Settings()
    pygame.display.set_caption(settings.caption)
    resolution = (settings.screen_width, settings.screen_height)
    screen = pygame.display.set_mode(resolution)
    play_button = Button(settings, screen, 'Play')

    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)

    ship = Ship(screen, settings)
    aliens = Group()
    bullets = Group()
    gf.create_fleet(settings, screen, ship, aliens)

    while True:
        gf.check_events(settings, screen, ship, bullets, stats, sb, play_button, aliens)
        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(settings, stats, sb, screen, ship, aliens, bullets)
        gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
