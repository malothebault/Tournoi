#!/usr/bin/python3


import gi
import subprocess
import os
import locale
import gettext
import webbrowser

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')

from gi.repository import Gtk, Granite

import constants as cn

class Brackets(Gtk.Box):

    '''Getting system default settings'''
    settings = Gtk.Settings.get_default()

    def __init__(self, parent):
        '''Our class will be a Gtk.Box and will contain our 
        new Welcome Widget.'''
        Gtk.Box.__init__(self, False, 0)

        '''Your app needs translations, right?
        Here we are trying to set the locale_path to the system one, assuming 
        the app is installed.'''
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
        ''''The self._ can be used for defining a new translation string.
        Note: that if the translation is not loaded (the check above), 
              self._ will be the same as str, so you won't get any errors.'''
        self._ = _

