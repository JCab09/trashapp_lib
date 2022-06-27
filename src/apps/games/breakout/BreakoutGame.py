# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:51:43 2022

@author: jason
"""
import pygame
from pygame.locals import *


from ...app_base import AppBase
from ...colors import *

from .paddle import Paddle


class BreakoutGame(AppBase):
    
    def _on_init(self):
        self._paddle = Paddle(WHITE, 100, 20, (0, self._width))
        self._paddle.rect.x = self._width // 2 - self._paddle.rect.width // 2
        self._paddle.rect.y = self._height - self._paddle.rect.height - 40
        self._all_sprites = pygame.sprite.Group()
        self._all_sprites.add(self._paddle)
        
        return True
    
    
    def _on_loop(self):
        self._parse_input()
        
        self._all_sprites.update()
    
    
    def _on_render(self):
        self._disp_surf.fill(BLACK)
        self._all_sprites.draw(self._disp_surf)
        
        pygame.display.update()
    
    
    def _on_cleanup(self):
        pass
        
    
    def _on_exit(self):
        self._logger.debug("_on_exit event triggered, setting exit_code = 1")
        self.exit_code = 1
        self._running = False
    
    
    def _parse_input(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] or keys[K_a]:
            self._paddle.move_left(5)
        if keys[K_RIGHT] or keys[K_d]:
            self._paddle.move_right(5)
        if keys[K_ESCAPE]:
            self._running = False