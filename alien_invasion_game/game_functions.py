import sys
import pygame
from bullet import Bullet
from alien import Alien

from time import sleep

def check_events(settings, screen, ship, bullets, stats, sb, play_button, aliens):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_keydown_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)
    if event.key == pygame.K_q:
        sys.exit()

def update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

def update_bullets(settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collision(settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(settings, screen, ship, aliens)
    if collisions:
        for aliens in collisions.values():
            stats.score += settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bullet_amount:
        bullet = Bullet(settings, screen, ship)
        bullets.add(bullet)

def create_fleet(settings, screen, ship, aliens):
    alien = Alien(settings, screen)
    aliens_number_x = get_number_aliens_x(settings, alien.rect.width)
    rows_number = get_number_rows(settings, ship.rect.height, alien.rect.height)
    for rows_number in range(rows_number):
        for alien_number in range(aliens_number_x):
            create_alien(settings, screen, aliens, alien_number, rows_number)

# define number of aliens that fit in a row
def get_number_aliens_x(settings, alien_width):
    alien_fleet_space_x = settings.screen_height - 1 * alien_width
    return int(alien_fleet_space_x / alien_width) - 3

# return number of alien rows
def get_number_rows(settings, ship_height, alien_height):
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    return int(available_space_y / (2 * alien_height))

def create_alien(settings, screen, aliens, alien_number, row_number):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def update_aliens(settings, stats, sb, screen, ship, aliens, bullets):
    check_fleet_edges(settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, sb, screen, ship, aliens, bullets)
    check_aliens_bottom(settings, stats, sb, screen, ship, aliens, bullets)

def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1

def ship_hit(settings, stats, sb, screen, ship, aliens, bullets):
    if (stats.ships_left > 0):
        stats.ships_left -= 1

        sb.prep_ships()

        aliens.empty()
        bullets.empty()
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(settings, stats, sb, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, sb, screen, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()