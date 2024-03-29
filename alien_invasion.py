# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:04:09 2019

@author: F70574
"""

import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    """Initialize one screen"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings,screen)
    
    # Create a group for bullet storage
    bullets = Group()
    # Creat an group of aliens
    aliens = Group()
    
    gf.create_fleet(ai_settings, screen, aliens)
    
    # Start the main loop of the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # Re-draw the screen
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        
run_game()