#!/usr/bin/python3

from distutils.core import setup

'''Here we are defining where should be placed each file'''
install_data = [
    ('share/applications', ['data/com.github.malothebault.tournoi.desktop']),
    ('share/metainfo', ['data/com.github.malothebault.tournoi.appdata.xml']),
    ('share/icons/hicolor/128x128/apps',['data/com.github.malothebault.tournoi.svg']),
    ('share/glib-2.0/schemas', ["data/com.github.malothebault.tournoi.gschema.xml"]),
    ('bin/tournoi',['src/brackets.py']),
    ('bin/tournoi',['src/constants.py']),
    ('bin/tournoi',['src/handler.py']),
    ('bin/tournoi',['src/headerbar.py']),
    ('bin/tournoi',['src/initialisation.py']),
    ('bin/tournoi',['src/listofname.py']),
    ('bin/tournoi',['src/main.py']),
    ('bin/tournoi',['src/stack.py']),
    ('bin/tournoi',['src/teams.py']),
    ('bin/tournoi',['src/welcome.py']),
    ('bin/tournoi',['src/window.py']),
    ('bin/tournoi',['src/__init__.py']),
]

'''Let's go and infuse our application into the system.'''
setup(  
    name='Tournoi',
    version='0.1',
    author='Malo Thebault',
    description='Create a tournament with ease',
    url='https://github.com/malothebault/Tournoi',
    license='GNU GPL3',
    scripts=['com.github.malothebault.tournoi'],
    packages=['src'],
    data_files=install_data
)
