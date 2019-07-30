# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 21:26:19 2019

@author: Flora
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Alien class"""
    
    def __init__(self, ai_settings, screen):
        
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)