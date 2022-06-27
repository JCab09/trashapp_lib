# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 14:50:41 2022

@author: jason
"""

import pygame
from random import randint

from ...colors import *


class Ball(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        pygame.draw.rect(self.image, color, (0, 0, width, height))
        self.rect = self.image.get_rect()
        
        self.velocity = [randint(4, 8), randint(-8, 8)]
        
    
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)