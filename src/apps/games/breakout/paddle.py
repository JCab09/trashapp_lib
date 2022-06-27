# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:58:02 2022

@author: jason
"""

import pygame
from pygame.locals import *

from ...colors import *

class Paddle(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height, x_bounds=(None, None)):
        super().__init__()
        
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        self.rect = pygame.draw.rect(self.image, color, (0, 0, width, height))
        
        self.x_min, self.x_max = x_bounds
        if self.x_max is not None:
            self.x_max -= width
        
        
    def move_left(self, pixels):
        self.rect.x -= pixels
        if self.x_min is not None:
            if self.rect.x < self.x_min:
                self.rect.x = self.x_min
        
    
    def move_right(self, pixels):
        self.rect.x += pixels
        if self.x_max is not None:
            if self.rect.x > self.x_max:
                self.rect.x = self.x_max