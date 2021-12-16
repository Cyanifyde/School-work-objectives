"""
Write a program that asks the user for their email address and a Gamertag to be used in an online game. These are stored in a text file. Two players cannot share the same email address or Gamertag. This should be checked before writing the data to the file.
"""
import json
def _save():
    with open('School-work-objectives/objective9/gamertag.json', 'w') as f:
        json.dump(notes, f)

def _open():
    global notes
    try:
        with open('School-work-objectives/objective9/gamertag.json') as f:
            notes = json.load(f)
    except FileNotFoundError:
        print("Could not load vend.json")
        notes = {}

_open()
def save(email, gamertag):
    if email not in notes:
        fals=True
        for x in notes:
            if notes[x] ==gamertag:
                fals=False
        if fals==True:
            notes[email]=gamertag
            _save()
        else:
            print("gamertag in use")
    else:
        print("email in use")
while True:
    _open()
    save(input("please enter your email\n"),input("please enter your gamertag\n"))
