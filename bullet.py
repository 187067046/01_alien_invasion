# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 10:56:17 2019

@author: F70574
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage the bullet"""
    
    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object"""
        #super(Bullet, self).__init__()
        super().__init__()
        self.screen = screen
        
        # Create a rec stands for the bullet
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store position(float)
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """Move the bullet upwards"""
        self.y -= self.speed_factor
        self.rect.centery = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)