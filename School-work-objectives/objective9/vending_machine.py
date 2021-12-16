"""
A vending machine dispenses items to customers when they choose a number between 1 and 25. When an item is dispensed the quantity for the item is reduced by 1. The data about the status of the vending machine is stored in a file called, “vend.dat” on flash memory inside the machine. This allows the status of the machine to be accessed remotely.
Write a program that stores the name of the item so it can be displayed on an LCD screen and the quantity of the item. When an item is sold, the quantity in the file is updated.
"""
# the items arent stored on a dat file but a json file as there is practically no documentation of this

import json,difflib
def _save():
    with open('School-work-objectives/objective9/vend.json', 'w') as f:
        json.dump(notes, f)

def _open():
    global notes
    try:
        with open('School-work-objectives/objective9/vend.json') as f:
            notes = json.load(f)
    except FileNotFoundError:
        print("Could not load vend.json")
        notes = {}


_open()
def find_similar(x):
    return difflib.get_close_matches(x, notes, cutoff=0.10, n=1)[0]

def timesused(item, quantity):
    notes[item] = quantity
    _save()

def _reset():
    timesused("apple",100)
    timesused("pear",100)
    timesused("fruit",100)
    timesused("fanta",100)
    timesused("snack",100)
    timesused("pepsi",100)
    _save()
v=True
while v==True:
    _open()
    for x in notes:
        print("there is {} many items of {}s".format(notes[x],x))
    i=input("please input what item you want\n")
    if i == "restock":
        _reset()
    else:
        try:
            p=find_similar(i)
        except:
            p=None
        print(p,"selected\n")
        timesused(p, notes[p]-1)
        

