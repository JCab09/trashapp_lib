# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 14:19:46 2022

@author: jason
"""

import argparse
import logging
import pygame
from pygame.locals import *

from apps.app_base import AppBase
from apps.colors import *
import utils

argparser = argparse.ArgumentParser()

log_lvl = argparser.add_mutually_exclusive_group()

log_lvl.add_argument(
    '-d', '--debug',
    help="Print lots of debugging statements",
    action='store_const', dest='loglevel', const=logging.DEBUG,
    default=logging.WARNING)

log_lvl.add_argument(
    '-v', '--verbose',
    help="Be verbose",
    action='store_const', dest='loglevel', const=logging.INFO)


class App(AppBase):
    def __init__(self, args):
        f = logging.Formatter(
            '%(asctime)s - [%(processName)-10s] [%(name)s] '
            '[%(levelname)-8s] - %(message)s')
        ch = logging.StreamHandler()
        ch.setFormatter(f)
        handlers = [ch]
        logging.basicConfig(level=args.loglevel, handlers=handlers, force=True)
        super(App, self).__init__("JC's TrashGame Lib", 700, 500)
    
    
    def _on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self._size, pygame.HWSURFACE)
        self._fpsclock = pygame.time.Clock()
        
        self._header_font = pygame.font.Font(None, 50)
        self._menu_font = pygame.font.Font(None, 35)
        
        self._menu_texts = ['1: Pong', '2: Breakout', '0: Gimmick', 'ESC: Exit']
        self._text_renders = [self._header_font.render("JC's TrashGame Lib", 1, BLUE)]
        self._menu_renders = [self._menu_font.render(text, 1, GRAY) for text in self._menu_texts]
        
        self._mouse = None
        self._games = utils.get_games()
        return True
        
        
    def _on_exit(self):
        self._logger.debug("_on_exit event triggered, setting exit_code = 1")
        self.exit_code = 1
        self._running = False
          
    
    def _on_loop(self):
        self._mouse = pygame.mouse.get_pos()
        
        app = self._parse_input()
        if app is not None:
            self._logger.info(f"Starting {app._name}...")
            exit_code = app.on_execute()
            self._logger.debug(
                f"{app._name} returned with exit_code = {app.exit_code}")
            if exit_code == 1:
                self._logger.debug("Setting self._running to False")
                self._running = False
            
            self._display_surf = pygame.display.set_mode(self._size, pygame.HWSURFACE)
    
    
    def _on_render(self):
        self._display_surf.fill(BLACK)
        
        for text in self._text_renders:
            self._display_surf.blit(text, (40, 40))
        
        for i, menu in enumerate(self._menu_renders):
            self._display_surf.blit(menu, (55, 100 + i*30))
        pygame.display.update()
        self._fpsclock.tick(self._fps)
    
    
    def _on_cleanup(self):
        pygame.quit()
        self._logger.info("Good Bye =)")
    
    
    def _on_key_down(self, event):
        if event.key == K_ESCAPE:
            self._running = False
    
    
    def _parse_input(self):
        keys = pygame.key.get_pressed()
        if keys[K_1] or keys[K_KP1]:
            return self._games['pong']['class']('PongGame', 700, 500)
        if keys[K_2] or keys[K_KP2]:
            return self._games['breakout']['class']('BreakoutGame',400, 700)
        if keys[K_0] or keys[K_KP0]:
            return self._games['gimmick']['class']('Dafuq?!', 700, 700)
        return None
  
    
if __name__ == '__main__':
    args = argparser.parse_args()
    theApp = App(args)
    attr_err_count = 0
    while attr_err_count <= 1:
        try:
            print("STARTING APP")
            theApp.on_execute()
            break
        except KeyboardInterrupt:
            theApp._on_cleanup()
            break
        except AttributeError as err:
            attr_err_count += 1
            if attr_err_count > 0:
                raise err