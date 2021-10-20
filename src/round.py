#!/usr/bin/python3


import gi
import subprocess
import os
import locale
import gettext
import webbrowser
import random

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')

from gi.repository import Gtk, Granite

try:
    import constants as cn
except ImportError:
    import tournoi.constants as cn


class Round:
    def __init__(self, parent, list_of_teams):
        
        self.list_of_teams = list_of_teams
        self.parent = parent
        
        ########### TRANSLATION ##############
        try:
           current_locale, encoding = locale.getdefaultlocale()
           locale_path = os.path.join(
               os.path.abspath(
                   os.path.dirname(__file__)
               ), 
               'locale'
           )
           translate = gettext.translation(
               cn.App.application_shortname, 
               locale_path, 
               [current_locale] 
           )
           _ = translate.gettext
        except FileNotFoundError:
           _ = str
        self._ = _
        ######################################
        
        list_to_return = []
        list_len = self.next_power_of_2(self.get_nb_of_teams)
        nb_of_ghosts = list_len - self.get_nb_of_teams
        
        for i in range(list_len):
            if i < nb_of_ghosts:
                team = Team("Ghost "+str(i))
                list_to_return.append(team)
            else:
                team = Team(list_of_teams[i - nb_of_ghosts].get('name'))
                list_to_return.append(team)
                
        
    def get_nb_of_teams():
        return len(self.list_of_teams)
    
    def next_power_of_2(x):  
        return 1 if x == 0 else 2**(x - 1).bit_length()


        
class Team:
    def __init__(self, name):
        self.name = name
        self.coordinate
        
        
class NotATeam:
    def __init__(self):
        self.coordinate
