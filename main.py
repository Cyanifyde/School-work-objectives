"""
this page has now been made to be readable
feel lucky you didnt have to read the compressed versions that came before
please see School-work-objectives/old_programs/
"""


def writes(x):
    f = open("loc.txt", "w")
    f.write(x)
    f.close()


def reads():
    f = open("loc.txt", "r")
    f = f.read()
    if f != "":
        _ = f
    else:
        _ = "/home/runner/all"
    return _


def pick_dir():
    time.sleep(1)
    y = reads()
    y = y.split("/")
    for x in range(4):
        del y[0]
    print(
        "\n\nwhat folder/script do you want to return to?\nplease either input a number or enter anything else to return to main folder\n"
    )
    y.reverse()
    for x in range(len(y)):
        print(x, "----", y[x])
    try:
        str = ""
        y.reverse()
        p = int(input())
        for x in range(p):
            del y[-1]
        for x in y:
            str += "/" + x
        str = "/home/runner/all" + str
    except:
        str = "/home/runner/all"
    writes(str)
    clear()
    os.system("python main.py")


def paths(x):
    return sorted([
        (i) for i in list(os.listdir(x)) if i not in
        ".upm.gitextrasmain.py.breakpointsREADME.mdpoetry.lockpyproject.toml"
        if not i.endswith((".json", ".txt"))
    ])


def send(x):
    writes(x)
    os.system("python " + x)
    pick_dir()


def recursion(x):
    v = paths(x)
    writes(x)
    [print(str(x) + " --- " + v[x]) for x in range(len(v))]
    _ = int(input("what file do you want to open / run?\n"))
    return x + "/" + str(v[_])


def main():
    p = True
    path = reads()
    while p == True:
        try:
            clear()
            path = recursion(path)
        except NotADirectoryError:
            send(path)
            p = False


import os
import time

clear = lambda: os.system("clear")
f = reads()
if os.path.isdir(f):
    main()
else:
    try:
        send(f)
    except:
        writes("/home/runner/all")
os.system("python main.py")
