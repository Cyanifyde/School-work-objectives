import os
import time


def find_files(filename, search_path):
    result = []
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result

def go_main():
    os.system("python main.py reset")

def ff(x, num):
    _ = find_files(x, "/home/runner/all")
    try:
        return _[num]
    except IndexError:
        if _ == []:
            os.system("python errors.py 2")
            go_main()
        else:
            os.system("python errors.py 1-2")
    else:
        os.system("python errors.py 0")
    go_main()


class file():
    def __init__(self, *loc):
        self.loc: int = loc

    def get(self, *at):
        v=[]
        for x in at:
            try:
                v.append(ff(self.loc, x))
            except TypeError:
                if at[0].isnumeric():
                    os.system("python errors.py 2")
                else:
                    os.system("python errors.py 3")
                go_main()
            except IndexError:
                os.system("python errors.py 1")
                go_main()
        return v