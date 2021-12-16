"""
Write a program that stores a shopping list for a user in a text file. The user can create a new shopping list (with a new filename), add items to an existing shopping list, remove items from the shopping list or output a shopping list.
"""

######################json
def _save(file):
    with open(loc+file+jso, 'w') as f:
        json.dump(notes, f)


def _open(file):
    global notes
    try:
        with open(loc+file+jso) as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = {}
        
def timesused(item, quantity):
    quantity=int(quantity)
    if item in notes:
        notes[item] = notes[item]+quantity
    else:
        notes[item] = quantity

def timesused_delete(item, quantity):
    quantity=int(quantity)
    if item in notes:
        notes[item] = notes[item]-quantity
        if notes[item]<=0:
            notes.pop(item)
    else:
        pass
    
####################

loc="School-work-objectives/objective9/shopping_lists/"
jso=".json"
def paths(x):  
    #returns all directories /files along a path
    return sorted([
        (i) for i in list(os.listdir(x)) 
    ])


def add():
    v=input("please input the item and then the amount you want to add separated by a space and beginning with an x\nif multiple items need to be added please follow that layout by putting a space between each item ie 'peanuts x10 apples x2 pears bananas'\n")
    v=v.split()
    for x in range (len(v)):
        try:
            p=v[x+1]
            if p =="":
                p="v"
        except:
            p="v"
        if p.startswith("x"):
            vm=p[1:]
        else:
            vm=1
        if not v[x].startswith("x"):
            timesused(v[x],vm)
            _save(i)

def delete():
    v=input("please input the item and then the amount you want to delete separated by a space and beginning with an x\nif multiple items need to be added please follow that layout by putting a space between each item ie 'peanuts x10 apples x2 pears bananas'\n")
    v=v.split()
    for x in range (len(v)):
        try:
            p=v[x+1]
            if p =="":
                p="v"
        except:
            p="v"
        if p.startswith("x"):
            vm=p[1:]
        else:
            vm=1
        if not v[x].startswith("x"):
            timesused_delete(v[x],vm)
            _save(i)
    
import os,json
run=True
while run==True:
    fun=True
    print("files:")
    for x in paths(loc):
        print(os.path.splitext(x)[0])
    
    i=input("would you like to make a new file?\n")
    if i == "yes":
        i=input("please name the file\n")
        _open(i)
        _save(i)
    else:
        i=input("what file do you want to open?\n")
        if i in (os.path.splitext(str(paths(loc)))[0]):
            _open(i)
        else:
            fun=False
    if fun ==True:
        print("in your item list there is")
        for x in notes:
            print("there is {} many items of {}".format(notes[x],x))
        ip=input("would you like to:\n1 --- add new items to list\n2 --- remove an item from list\n")
        if ip =="1":
            add()
        if ip=="2":
            delete()
    else:
        pass