import os


def find_files(filename, search_path):
    result = []
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result


def go_main():
    os.system("python main.py reset")

def goerrors(errorcode):
    os.system("python errors.py {}".format(errorcode))


def ff(x, num):
    _ = find_files(x, "/home/runner/all")
    try:
        return _[num]
    except IndexError:
        if _ == []:
            goerrors("2")
            go_main()
        else:
            goerrors("1-2")
    else:
        goerrors("0")
    go_main()


class file():
    def __init__(self, *loc):
        self.loc: int = loc

    def get(self, *at):
        v = []
        for x in at:
            try:
                v.append(ff(self.loc[0], x))
            except TypeError:
                if at[0].isnumeric():
                    goerrors("2")
                else:
                    goerrors("2")
                go_main()
            except IndexError:
                goerrors("1")
                go_main()
        return v