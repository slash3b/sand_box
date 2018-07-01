import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events(settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

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

def update_screen(settings, screen, ship, aliens, bullets):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

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

def update_aliens(settings, aliens):
    check_fleet_edges(settings, aliens)
    aliens.update()

def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1
