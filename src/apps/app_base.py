# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:18:42 2022

@author: jason
"""

from abc import ABC, abstractmethod
import logging
import pygame

from .cevent import CEvent
from .key_utils import get_key_dict

class AppBase(ABC, CEvent):
    def __init__(self, name, width, height, fps=60, display_surface=None):
        super().__init__()
        self.exit_code = 0
        self._name = name
        self._running = False
        self._size = self._width, self._height = width, height
        self._fps = fps
        self._keys = get_key_dict()
        
        if display_surface is None:
            self._disp_surf = pygame.display.set_mode(self._size, pygame.HWSURFACE)
        else:
            self._disp_surf = display_surface
            
        pygame.display.set_caption(self._name)
        self._clock = pygame.time.Clock()
        self._logger = logging.getLogger(self._name)
        self._logger.debug(f"{self._name} Base is initialized")
        
    
    @abstractmethod
    def _on_init(self) -> bool:
        pass
    
    
    @abstractmethod
    def _on_loop(self):
        pass
    
    
    @abstractmethod
    def _on_render(self):
        pass
        
    
    @abstractmethod
    def _on_cleanup(self):
        pass
    

    def on_execute(self):        
        self._running = self._on_init()
        if not self._running:
            self._logger.warn(f"{self._name} did not initialize... "
                              "the game will not run!")
        else:
            self._logger.debug(f"{self._name} has fully initialized!")
        while self._running:
            for event in pygame.event.get():
                try:
                    self._on_event(event)
                except NotImplementedError as err:
                    self._logger.debug(f"NotImplementedError: {err}")
            self._on_loop()
            self._on_render()
            self._clock.tick(self._fps)
            
        self._logger.debug("Cleaning up...")
        self._on_cleanup()
        self._logger.debug(f"Returning with exit_code = {self.exit_code}")
        return self.exit_code