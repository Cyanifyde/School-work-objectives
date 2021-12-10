"""
Write a program that will hold the inventory a player has in an RPG game. The player has the following actions: pick (adds an item to the inventory), drop (removes an item from the inventory), pull (outputs a random item from the inventory) and search (outputs all the items in the inventory).
"""

import random


class action():
    def __init__(self, *items):
        self.items = [x for x in items]

    def pick(self, item):
        self.items.append(item)

    def drop(self, item):
        self.items.remove(item)

    def pull(self):
        _ = random.randint(0, (len(self.items)) - 1)
        print(self.items[_])

    def search(self):
        print("you have {} items, they are:".format(len(self.items)))
        for x in self.items:
            print(x)


inv = action("sword", "bow")
run = True
while run == True:
    _ = input("please input an action 'pick','drop','pull','search'\n")
    if _ == "pick":
        _1 = input("what tem do you want to add?\n")
        inv.pick(_1)
    elif _ == "drop":
        _1 = input("what item do you want to remove?\n")
        inv.drop(_1)
    elif _ == "pull":
        inv.pull()
    elif _ == "search":
        inv.search()
    else:
        run = False
