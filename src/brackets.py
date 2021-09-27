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

try:
    import constants as cn
    import teams as tm
except ImportError:
    import tournoi.constants as cn
    import tournoi.teams as tm

class Brackets(Gtk.Box):

    '''Getting system default settings'''
    settings = Gtk.Settings.get_default()

    def __init__(self, parent):
        '''Our class will be a Gtk.Box and will contain our 
        new Welcome Widget.'''
        Gtk.Box.__init__(self, False, 0)
        self.parent = parent
        icon_size = Gtk.IconSize.MENU

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
        
        self.set_border_width(80)
        self.set_orientation(Gtk.Orientation.VERTICAL)
        
        brackets = Gtk.Grid.new()
        brackets.set_column_homogeneous(True)
        brackets.set_row_homogeneous(True)
        brackets.set_row_spacing(35)
        brackets.set_column_spacing(35)
        
        liste = [(0,0,{'name':"Bob",'color':"Blue",'points':0}),
                (0,2,{'name':"Alice",'color':"Red",'points':0}),
                (1,1,{'name':"Fred",'color':"Green",'points':0})]
        
        bbox = {}
        buttons = {}
        COL = 0
        ROW = 1
        DICT = 2
        WIDTH = 1
        HEIGHT = 1
        for i in range(len(liste)):
            bbox[i] = Gtk.Box()
            team_name_label = Gtk.Label(liste[i][DICT].get('name'))
            bbox[i].pack_start(team_name_label, True, True, 0)
            edit_button = Gtk.Button.new_from_icon_name("accessories-text-editor-symbolic", icon_size)
            edit_button.connect('clicked', self.on_edit_button_clicked)
            bbox[i].pack_end(edit_button, False, False, 6)
            delete_button = Gtk.Button.new_from_icon_name("edit-delete-symbolic", icon_size)
            delete_button.get_style_context().add_class('destructive-action')
            delete_button.valign = Gtk.Align.CENTER
            delete_button.connect('clicked', self.on_delete_button_clicked)
            bbox[i].pack_end(delete_button, False, False, 6)
            brackets.attach(bbox[i],
                        liste[i][COL],
                        liste[i][ROW],
                        WIDTH,
                        HEIGHT)
            
            # buttons[i] = Gtk.Button.new_with_label(liste[i][DICT].get('name'))
            # brackets.attach(buttons[i],
            #             liste[i][COL],
            #             liste[i][ROW],
            #             WIDTH,
            #             HEIGHT)
        # self.teams = tm.Teams(3)
        self.pack_start(brackets, True, True, 0)
        
        
    def on_edit_button_clicked (self, widget):
        print("edit")
    
    def on_delete_button_clicked (self, widget):
        print("delete")
