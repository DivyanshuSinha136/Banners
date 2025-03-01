# Banner
# Copyright (C) 2025 Divyanshu Sinha
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from subprocess import run

try:
    import pyfiglet

except:
    run(['pip', 'install', 'pyfiglet'])

import pyfiglet

color = {
    'white': '\033[0m',
    'default': '\033[0m',
    'gray': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'orange': '\033[33m',
    'blue': '\033[34m',
    'volite': '\033[35m',
    'sky-blue': '\033[36m',
}

background_color = {
    'red': '\033[41m',
    'green': '\033[42m',
    'orange': '\033[43m',
    'blue': '\033[44m',
    'volite': '\033[45m',
    'sky-blue': '\033[46m',
    'white':'\033[47m',
    'default': '\033[49m'
}

text_font = {
    'default': '\033[0m',
    'bold': '\033[1m',
    'curl': '\033[3m',
    'underline': '\033[4m',
}

class banner:
    def __init__(self, text: str | None = "Banner", font: str | None = 'Calibri') -> None:
        self.text = text
        self.font = font
        print (self.create)

    def create(self) -> None:
        return pyfiglet.figlet_format(self.text, self.font)

class ColourText:
    '''Change The color of the text in terminal.'''
    '''How to use it:
    from main import ColorText

    ColourText(colour = "default") # text colour should be change on default.
    ColourText(colour = "white") # text colour should be change on white.
    ColourText(colour = "gray") # text colour should be change on gray.
    ColourText(colour = "red") # text colour should be change on red.
    ColourText(colour = "green") # text colour should be change on green.
    ColourText(colour = "orange") # text colour should be change on orange.
    ColourText(colour = "blue") # text colour should be change on blue.
    ColourText(colour = "volite") # text colour should be change on volite.
    ColourText(colour = "sky-blue") # text colour should be change on sky-blue.
    '''
    def __init__(self, colour: str | None = 'default') -> None:
        self.color = colour.lower()
        print(color[self.color])

class TextFunt:
    '''It can change the font boldness, font writing, underline on the terminal'''
    '''How to use it:
    from main import TextFunt
    TextFunt(font = "bold") # change the font into bold.
    TextFunt(font = "underline") # change the font into underline.
    TextFunt(font = "curl") # change the font into curl.
    TextFunt(font = "default") # change the font into default.
    '''
    def __init__(self, font: str | None = 'default') -> None:
        self.font = font.lower()
        print(text_font[self.font])

class BackgroundColour:
    '''It changes the backgrund color of the terminal'''
    '''How to use it:
    from main import BackgroundColour

    BackgroundColour(color = "red") # Background colour should be change on red.
    BackgroundColour(color = "green") # Background colour should be change on green.
    BackgroundColour(color = "orange") # Background colour should be change on orange.
    BackgroundColour(color = "blue") # Background colour should be change on blue.
    BackgroundColour(color = "volite") # Background colour should be change on volite.
    BackgroundColour(color = "sky-blue") # Background colour should be change on sky-blue.
    BackgroundColour(color = "white") # Background colour should be change on white.
    BackgroundColour(color = "default") # Background colour should be change on default.
    '''
    def __init__(self, color: str | None = 'default') -> None:
        self.color = color.lower()
        print(background_color[self.color])