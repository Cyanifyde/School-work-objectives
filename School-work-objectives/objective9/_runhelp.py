import os


def find_files(filename, search_path):
    result = []
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result


def ff(x, num):
    _ = find_files(x, "/home/runner/all")
    try:
        return _[num]
    except IndexError:
        if _ == []:
            exit("error code x00000001")
        else:
            exit("error code x00000001-2")
    else:
        exit("error code x00000000")


class file():
    def __init__(self, loc):
        self.loc: int = loc

    def get(self, *at):
        v=[]
        for x in at:
            try:
                v.append(ff(self.loc, x))
            except TypeError:
                if at[0].isnumeric():
                    exit("error code x00000002")
                else:
                    exit("error code x00000003")
            except IndexError:
                exit("error code x00000001")
        return v