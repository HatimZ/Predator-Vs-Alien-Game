

import pygame
#importing file
from pygame.sprite import Group
import Gamefunctions as gf
#importing classes
from Settings import settings
from ship import Ship
from alien import Alien

def run_game():
    pygame.init()

    ai_settings = settings()
    #A list of all the sprites
    bullets = Group()

    aliens = Group()
    # Create the fleet of aliens.
   
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #Screen is given in ships parameter, it means we can make multiple screens/windows and work on them
    ship = Ship(ai_settings, screen)
    gf.create_fleet(ai_settings, screen,ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        #Updates all the sprites
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship,aliens, bullets)
        # Updates position of ship by checking the keys pressed




run_game()
