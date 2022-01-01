def writes(x):
    f = open("loc.txt", "w")
    f.write(x)
    f.close()


def paths(x):
    return sorted([
        (i) for i in list(os.listdir(x)) if i not in
        ".upm.gitextrasmain.py.breakpointsREADME.mdpoetry.lockpyproject.toml"
        if not i.endswith((".json", ".txt"))
    ])


def send(x):
    writes(x)
    os.system("python " + x)
    _ = ("" if input(
        "\npress enter to go to rerun\nor input anything else to return\n") !=
         "" else x)
    writes(_)


def recursion(x):
    v = paths(x)
    [print(str(x) + " --- " + v[x]) for x in range(len(v))]
    _ = int(input("what file do you want to open / run?\n"))
    clear()
    return x + "/" + str(v[_])


def main():
    exec(
        'p=True;path="/home/runner/all"\nwhile p==True:\n\ttry:path=recursion(path)\n\texcept NotADirectoryError:send(path);p=False;clear()'
    )


exec(
    'import os;clear=lambda:os.system("clear");f=open("loc.txt","r");f=f.read()\ntry:clear();send(f)if f!=""else main()\nexcept:writes("")\nos.system("python main.py")'
)
