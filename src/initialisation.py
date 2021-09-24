#!/usr/bin/python3


import gi
import subprocess
import os
import locale
import gettext
import webbrowser

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')

from gi.repository import Gtk, Granite, Gdk

import constants as cn

class Initialisation(Gtk.Box):

    '''Getting system default settings'''
    settings = Gtk.Settings.get_default()

    def __init__(self, parent):
        '''Our class will be a Gtk.Box and will contain our 
        new Welcome Widget.'''
        Gtk.Box.__init__(self, False, 0)
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

        self.set_border_width(80)
        self.set_orientation(Gtk.Orientation.VERTICAL)

        grid = Gtk.Grid.new()
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)
        grid.set_row_spacing(35)
        grid.set_column_spacing(35)
        
        # Widgets creation
        validate_button = Gtk.Button.new_with_label(_("Validate"))
        validate_button.get_style_context().add_class('suggested-action')
        validate_button.connect("clicked", self.on_validate_clicked)
        nb_team_button = Gtk.SpinButton.new_with_range(2,8,1)
        random_team_attributes = Gtk.Button.new_with_label(_("Random team names and colors"))
        scroll_w = Gtk.ScrolledWindow.new(None, None)
        listbox = Gtk.ListBox.new()
        listbox.get_style_context().add_class('config-list-box')
        scroll_w.add(listbox)
        
        row_1 = Gtk.ListBoxRow()
        box_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        box_1.set_border_width(10)
        entry = Gtk.Entry()
        entry.set_placeholder_text("Team name")
        color = Gtk.ColorButton.new_with_rgba(Gdk.RGBA(222, 222, 222, 255))
        color.connect("color_set", self.on_color_color_set)
        box_1.pack_start(entry, True, True, 0)
        box_1.pack_end(color, False, False, 0)
        row_1.add(box_1)
        listbox.add(row_1)
        
        row_2 = Gtk.ListBoxRow()
        box_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        box_2.set_border_width(10)
        entry = Gtk.Entry()
        entry.set_placeholder_text("Team name")
        color = Gtk.ColorButton.new_with_rgba(Gdk.RGBA(222, 0, 222, 255))
        color.connect("color_set", self.on_color_color_set)
        box_2.pack_start(entry, True, True, 0)
        box_2.pack_end(color, False, False, 0)
        row_2.add(box_2)
        listbox.add(row_2)
        
        # Attach widgets to the grid
        grid.attach(nb_team_button, 0, 0, 1, 1)
        grid.attach(random_team_attributes, 1, 0, 1, 1)
        grid.attach(scroll_w, 0, 1, 2, 4)
        grid.attach(validate_button, 1, 5, 1, 1)
        
        self.pack_start(grid, True, False, 0)
        
    # def on_spin_button():
    #     get_value_as_int()
    
    def on_color_color_set(self, widget):
        print("Hi")
        # cn.Colors.primary_color = widget.get_rgba().to_string()

        # stylesheet = f"""
        #     @define-color colorPrimary {cn.Colors.primary_color};
        #     @define-color textColorPrimary {cn.Colors.primary_text_color};
        #     @define-color textColorPrimaryShadow {cn.Colors.primary_text_shadow_color};
        # """

        # style_provider = Gtk.CssProvider()
        # style_provider.load_from_data(bytes(stylesheet.encode()))
        # Gtk.StyleContext.add_provider_for_screen(
        #     Gdk.Screen.get_default(), 
        #     style_provider,
        #     Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        # )
    
    def on_validate_clicked(self, widget):
        self.parent.stack.set_visible_child_name("brackets")
