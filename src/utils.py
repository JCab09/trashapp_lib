# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 19:31:19 2022

@author: jason
"""
import importlib

import apps


def get_games():
    games = {}
    games_dict = apps.games_dict
    for game in games_dict:
        module = importlib.import_module(
            'apps.games.' + game + '.' + games_dict[game]['name'])
        class_ = getattr(module, games_dict[game]['name'])
        games[game] = {'name': games_dict[game]['name'],
                       'description': games_dict[game]['description'],
                       'class': class_}
    return games
      
