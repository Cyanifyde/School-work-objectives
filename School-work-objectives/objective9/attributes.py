"""
Write two subroutines. One that allows the user to enter the attributes for a character in an RPG game.  This includes their name, attack and defence capability between 0 and 100.  A second subroutine should write the data to a file.
"""
from _runhelp import file
v=file("attributes.json").get(0)[0]

import json


def _save():
    with open(v, 'w') as f:
        json.dump(notes, f)


def _open():
    global notes
    try:
        with open(v) as f:
            notes = json.load(f)
    except FileNotFoundError:
        print("Could not load vend.json")
        notes = {}
        
_open()