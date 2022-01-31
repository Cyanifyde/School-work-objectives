"""
Write two subroutines. One that allows the user to enter the attributes for a character in an RPG game.  This includes their name, attack and defence capability between 0 and 100.  A second subroutine should write the data to a file.
"""

from _runhelp import file
v=file("attributes.txt").get(0)[0]

g = open(v, "r").read()
g=g.splitlines()

print(g)