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
        
        dict_to_return = {}
        for i in self.list_of_teams:
            picked_team = random.choice(self.list_of_teams)
            if i % 2 == 0:
                None
            elif i % 2 == 1:
                None
                
        
    def get_nb_of_teams():
        return len(self.list_of_teams)
