"""
Write a program that allows the user to store up to 10 notes.  The program should have this functionality on an infinite loop:
Output all the notes stored, numbered 0-9.
Ask the user to enter a number for a note to change.
Ask the user to enter the new note.
Over-write any existing note stored at that position.
"""
import json;import os;clear=lambda:os.system("clear");import time
def _save():
    with open('School-work-objectives/objective8/notes.json', 'w') as f:
        json.dump(notes, f)
def _open():
    global notes
    try:
        with open('School-work-objectives/objective8/notes.json') as f:
            notes = json.load(f)
    except FileNotFoundError:
        print("Could not load usagecount.json")
        notes = {}
def timesused(note,loc):
    notes[str(loc)] = note
    _save()
def delete():
    for x in list(notes):
        if x not in ["0","1","2","3","4","5","6","7","8","9"]:
            print("invalid note location,deleting")
            del notes[x]
            _save()
def list_all():
    dictionary_items = notes.items()
    sorted_items = sorted(dictionary_items)
    for x in range(len(sorted_items)):
        print(sorted_items[x][0]," --- ",sorted_items[x][1])
_open()
while True:
    cont=True
    list_all()
    try:
        _=int(input("please input the number location you want to write at ie '2' from 0-9\n"))
        if _ not in ["0","1","2","3","4","5","6","7","8","9"]:
            raise ValueError
            raise Exception("incorrect number")
    except ValueError:print("incorrect number");cont=False
    if cont==True:
        __=input("please input what you would like to enter to this location\n")
        timesused(__,_)
    #delete()
    time.sleep(1)
    clear()


    