# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:03:15 2019

@author: F70574
"""

import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Put each new ship at center bottom
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Set attribute "center" to be float
        self.center = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        
        print("self.screen_rect.right: ",self.screen_rect.right)
        print("self.screen_rect.left: ",self.screen_rect.left)
        print("self.screen_rect.top: ",self.screen_rect.top)
        print("self.screen_rect.bottom: ",self.screen_rect.bottom)
        
        # Moving Flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Adjust the position of the ship according to the moving flag"""
        # Update the value of "center" of the ship, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor
        
        # Update rect object according to self.center
        self.rect.centerx = self.center
        self.rect.centery = self.center_y
    
    def blitme(self):
        
        self.screen.blit(self.image,self.rect)