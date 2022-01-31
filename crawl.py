import os, time, urllib.request

clear = lambda: os.system("clear")


def crawl():
    path = '/home/runner/all/School-work-objectives'
    list_dir = []
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            if files != (".git"):
                if name not in (
                        ".upm.gitextrasmain.py.breakpointsREADME.mdpoetry.lockpyproject.toml."
                ):
                    list_dir.append(os.path.join(root, name))
    f = open("_crawled.txt", "w")
    f = open("_crawled.txt", "a")
    for x in list_dir:
        f.write(x + "\n")
    f.close()


def update(loc, no):
    time.sleep(0.3)
    if no == 1:
        print("downloading", loc)
    elif no == 2:
        clear()
        print("making directory", loc)
        time.sleep(1)
        clear()
    elif no == 3:
        print("finished writing to", loc)
        time.sleep(0.5)
        clear()
    else:
        print("missing file", loc)
        time.sleep(0.3)


def download_list():
    response = urllib.request.urlopen(
        'https://raw.githubusercontent.com/pravda-cancri/School-work-objectives/master/_crawled.txt'
    )
    data = response.read()
    f = open("crawl.txt", "wb")
    f.write(data)
    f.close()


def make_dir(item):
    os.system("mkdir " + item)


def write_to_file(data, at):
    update(''.join(at.split('/')[-1]), 1)
    f = open(at, "wb")
    f.write(data)
    f.close()
    update(''.join(at.split('/')[-1]), 3)


def check_dir(item):
    var = len(item.split('/')) - 1
    gr = ""
    for x in range(var):
        gr += "/" + ''.join(item.split('/')[x])
        if not os.path.isdir(gr):
            update(''.join(gr.split('/')[-1]), 2)
            make_dir(gr)


def download(_, item):
    response = urllib.request.urlopen(
        "https://raw.githubusercontent.com/pravda-cancri/School-work-objectives/master/School-work-objectives/"
        + _)
    data = response.read()
    check_dir(item)
    write_to_file(data, item)


def download_item(item):
    num = 2
    running = True
    while running:
        try:
            _ = '/'.join(item.split('/')[-num:])
            download(_, item)
            running = False
        except:
            num += 1


def check_different():
    f = open("crawl.txt", "r")
    f = f.read().splitlines()
    g = open("_crawled.txt", "r")
    g = g.read().splitlines()
    for x in f:
        if x not in g:
            update(''.join(x.split('/')[-1]), 4)
            download_item(x)


crawl()
#download_list()
#check_different()
glf = False
if glf == True:
    os.remove("_crawled.txt")
    os.remove("crawl.txt")
