# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 13:29:02 2022

@author: jason
"""

import pygame

from ...colors import *


class Paddle(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height, y_bounds=(0, 400)):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        pygame.draw.rect(self.image, color, (0, 0, width, height))
        self.rect = self.image.get_rect()
        
        self._y_bounds = y_bounds
        
        
    def move_up(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < self._y_bounds[0]:
            self.rect.y = self._y_bounds[0]
        
        
    def move_down(self, pixels):
        self.rect.y += pixels
        if self.rect.y > self._y_bounds[1]:
            self.rect.y = self._y_bounds[1]