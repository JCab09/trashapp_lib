# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:24:20 2022

@author: jason
"""

import pygame
from pygame.locals import *

class CEvent():
    def __init__(self):
        pass
    def _on_input_focus(self):
        raise NotImplementedError(
            "Input Focus event has not been implemented!")
    def _on_input_blur(self):
        raise NotImplementedError(
            "Input Blur event has not been implemented!")
    def _on_key_down(self, event):
        raise NotImplementedError(
            "Key Down event has not been implemented!")
    def _on_key_up(self, event):
        raise NotImplementedError(
            "Key Up event has not been implemented!")
    def _on_mouse_focus(self):
        raise NotImplementedError(
            "Mouse Focus event has not been implemented!")
    def _on_mouse_blur(self):
        raise NotImplementedError(
            "Mouse Blur event has not been implemented!")
    def _on_mouse_move(self, event):
        raise NotImplementedError(
            "Mouse Move event has not been implemented!")
    def _on_mouse_wheel(self, event):
        raise NotImplementedError(
            "Mouse Wheel event has not been implemented!")
    def _on_lbutton_up(self, event):
        raise NotImplementedError(
            "LButton Up event has not been implemented!")
    def _on_lbutton_down(self, event):
        raise NotImplementedError(
            "LButton Down event has not been implemented!")
    def _on_rbutton_up(self, event):
        raise NotImplementedError(
            "RButton Up event has not been implemented!")
    def _on_rbutton_down(self, event):
        raise NotImplementedError(
            "RButton Down event has not been implemented!")
    def _on_mbutton_up(self, event):
        raise NotImplementedError(
            "MButton Up event has not been implemented!")
    def _on_mbutton_down(self, event):
        raise NotImplementedError(
            "MButton Down event has not been implemented!")
    def _on_minimize(self):
        raise NotImplementedError(
            "Minimize event has not been implemented!")
    def _on_restore(self):
        raise NotImplementedError(
            "Restore event has not been implemented!")
    def _on_resize(self, event):
        raise NotImplementedError(
            "Resize event has not been implemented!")
    def _on_expose(self):
        raise NotImplementedError(
            "Expose event has not been implemented!")
    def _on_exit(self):
        raise NotImplementedError(
            "Exit event has not been implemented!")
    def _on_user(self, event):
        raise NotImplementedError(
            "User event has not been implemented!")
    def _on_joy_axis(self, event):
        raise NotImplementedError(
            "Joy Axis event has not been implemented!")
    def _on_joybutton_up(self, event):
        raise NotImplementedError(
            "Joy Button Up event has not been implemented!")
    def _on_joybutton_down(self, event):
        raise NotImplementedError(
            "Joy Button Down event has not been implemented!")
    def _on_joy_hat(self, event):
        raise NotImplementedError(
            "Joy Hat event has not been implemented!")
    def _on_joy_ball(self, event):
        raise NotImplementedError(
            "Joy Ball event has not been implemented!")
        
        
    def _on_event(self, event):
        if event.type == QUIT:
            self._on_exit()
        elif event.type >= USEREVENT:
            self._on_user(event)
        elif event.type == VIDEOEXPOSE:
            self._on_expose()
        elif event.type == VIDEORESIZE:
            self._on_resize(event)
 
        elif event.type == KEYUP:
            self._on_key_up(event)
 
        elif event.type == KEYDOWN:
            self._on_key_down(event)
 
        elif event.type == MOUSEMOTION:
            self._on_mouse_move(event)
 
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                self._on_lbutton_up(event)
            elif event.button == 2:
                self._on_mbutton_up(event)
            elif event.button == 3:
                self._on_rbutton_up(event)
 
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                self._on_lbutton_down(event)
            elif event.button == 2:
                self._on_mbutton_down(event)
            elif event.button == 3:
                self._on_rbutton_down(event)
 
        elif event.type == ACTIVEEVENT:
            if event.state == 1:
                if event.gain:
                    self._on_mouse_focus()
                else:
                    self._on_mouse_blur()
            elif event.state == 2:
                if event.gain:
                    self._on_input_focus()
                else:
                    self._on_input_blur()
            elif event.state == 4:
                if event.gain:
                    self._on_restore()
                else:
                    self._on_minimize()