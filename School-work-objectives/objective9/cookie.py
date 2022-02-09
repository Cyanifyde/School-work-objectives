"""
A cookie is a text file a website can use to store small amounts of data on a visitor's computer. They are useful for storing preferences such as colour schemes so that the next time a user visits a website their preferences can be applied.
Write a program that allows a user to choose between dark and light theme. The user preference should be stored in a text file. When the program is run, the user preference is loaded and displayed to the user before presenting the option to change it. If the user chooses to change it, it is changed in the file.
"""

from _runhelp import file

__ = file("cookie.json").get(0)[0]

import json


def _save():
    with open(__, 'w') as f:
        json.dump(cookies, f)


def _open():
    global cookies
    try:
        with open(__) as f:
            cookies = json.load(f)
    except:
        print("Could not load cookie.json")
        cookies = {}


_open()
_save()
view="view_theme"
if view not in cookies:
    cookies[view]="lightmode"
    _save()
else:
    for x in cookies:
        _open()
        print("current setting for {} is {}".format(x,cookies[x]))
        print("would you like to change this?")
        v=input()
        if v=="yes":
            p=input("1 - lightmode\n2 - darkmode\n")
            if p =="1":
                cookies[view]="lightmode"
            else:
                cookies[view]="darkmode"
            _save()

for x in cookies:
    _open()

    print("current setting for {} is {}".format(x,cookies[x]))
                