# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 18:10:19 2022

@author: jason
"""
import pygame
from pygame.locals import *

from ...colors import *
from ...app_base import AppBase

from .ball import Ball
from .paddle import Paddle


class PongGame(AppBase):
    
    def _on_init(self):
        self._paddle_A = Paddle(WHITE, 10, 100)
        self._paddle_A.rect.x = 20
        self._paddle_A.rect.y = 200
        
        self._paddle_B = Paddle(WHITE, 10, 100)
        self._paddle_B.rect.x = 670
        self._paddle_B.rect.y = 200
        
        self._ball = Ball(WHITE, 10, 10)
        self._ball.rect.x = 345
        self._ball.rect.y = 245
        
        self._all_sprites = pygame.sprite.Group()
        self._all_sprites.add(self._paddle_A)
        self._all_sprites.add(self._paddle_B)
        self._all_sprites.add(self._ball)
        
        self._score_A = 0
        self._score_B = 0
        return True
    
    
    def _on_loop(self):
        self._parse_input()
        self._all_sprites.update()
        
        if self._ball.rect.x >= 690:
            self._score_A += 1
            self._ball.velocity[0] = -self._ball.velocity[0]
        if  self._ball.rect.x <= 0:
            self._score_B += 1
            self._ball.velocity[0] = -self._ball.velocity[0]
        if self._ball.rect.y >= 490 or self._ball.rect.y <= 0:
            self._ball.velocity[1] = -self._ball.velocity[1]
            
        if pygame.sprite.collide_mask(self._ball, self._paddle_A) \
            or pygame.sprite.collide_mask(self._ball, self._paddle_B):
                self._ball.bounce()
    
    
    def _on_render(self):
        self._disp_surf.fill(BLACK)
        pygame.draw.line(self._disp_surf, WHITE, (349, 0), (349, 500), 2)
        self._all_sprites.draw(self._disp_surf)
        
        font = pygame.font.Font(None, 74)
        text = font.render(str(self._score_A), 1, WHITE)
        self._disp_surf.blit(text, (250, 10))
        text = font.render(str(self._score_B), 1, WHITE)
        self._disp_surf.blit(text, (420, 10))
        
        pygame.display.flip()
    
    
    def _on_cleanup(self):
        pass
        
    
    def _on_exit(self):
        self._logger.debug("_on_exit event triggered, setting exit_code = 1")
        self._running = False
        self.exit_code = 1
        
        
    def _parse_input(self):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self._paddle_A.move_up(5)
        if keys[K_s]:
            self._paddle_A.move_down(5)
        if keys[K_UP]:
            self._paddle_B.move_up(5)
        if keys[K_DOWN]:
            self._paddle_B.move_down(5)
        if keys[K_ESCAPE]:
            self._running = False