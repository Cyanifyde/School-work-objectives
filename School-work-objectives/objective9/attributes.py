"""
Write two subroutines. One that allows the user to enter the attributes for a character in an RPG game.  This includes their name, attack and defence capability between 0 and 100.  A second subroutine should write the data to a file.
"""

from _runhelp import file

__ = file("attributes.txt").get(0)[0]

g = open(__, "r").read()
g = g.splitlines()

names = []
stats = []
for p in range(len(g)):
    f = g[p]
    x = f.startswith("CharacterName://")
    if x:
        pg = f.replace("CharacterName://", "")
        names.append(pg)
        for k in range(2):
            stats.append(g[p + k + 1])
for x in range(len(names)):
    print("{} has the attributes : attack = {} , defence = {}".format(
        names[x], stats[x * 2], stats[x * 2 - 1]))
stat = []
running = True
while running == True:
    try:
        name = input("please input a name\n")
        stat.append(int(input("please input the attack\n")))
        stat.append(int(input("please input the defence\n")))
        running = False
    except ValueError:
        print("number was not input")
print(
    "you want to give '{}' the attributes : attack = {} , defence = {}\ninput anything to continue or input 'v' to stop"
    .format(name, stat[0], stat[1]))
v = input()
if v != "v":
    g = open(__, "a")
    g.write("\nCharacterName://{}\n{}\n{}".format(name, str(stat[0]),
                                                  str(stat[1])))
    g.close()
