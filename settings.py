# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 13:46:18 2019

@author: F70574
"""

class Settings():
    """Store all the settings for the game"""
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
    
        # settings of the ship
        self.ship_speed_factor = 1.5
        
        # settings of bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3