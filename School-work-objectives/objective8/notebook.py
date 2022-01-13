"""
Write a program that allows the user to store up to 10 notes.  The program should have this functionality on an infinite loop:
Output all the notes stored, numbered 0-9.
Ask the user to enter a number for a note to change.
Ask the user to enter the new note.
Over-write any existing note stored at that position.
"""

import json
import os
import random
import time

clear = lambda: os.system("clear")

from _runhelp import file
v=file("amino.txt").get(0)[0]

def _save():
    with open(v, 'w') as f:
        json.dump(notes, f)


def _open():
    global notes
    try:
        with open(v) as f:
            notes = json.load(f)
    except FileNotFoundError:
        print("Could not load usagecount.json")
        notes = {}


def timesused(note, loc):
    notes[str(loc)] = note
    _save()


def list_all():
    dictionary_items = notes.items()
    sorted_items = sorted(dictionary_items)
    for x in range(len(sorted_items)):
        print(sorted_items[x][0], " --- ", sorted_items[x][1])


_open()
while True:
    cont = True
    list_all()
    try:
        _ = input(
            "please input the number location you want to write at ie '2' from 0-9\n"
        )
        if _ not in [
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "delete_all"
        ]:
            raise ValueError
            raise Exception
    except ValueError:
        print("incorrect number")
        cont = False

    if cont == True:
        if _ == "delete_all":
            notes = {}
            _save()
        else:
            __ = input(
                "please input what you would like to enter to this location\n")
            timesused(__, _)
        animation = "|/-\\"
        [
            exec(
                'print("saving",__,"to loc "+_,"  ",( animation[i % len(animation)]));time.sleep(random.uniform(0.1,0.4));clear()'
            ) for i in range(random.randint(10, 20))
        ]

    else:
        time.sleep(1)
    clear()
