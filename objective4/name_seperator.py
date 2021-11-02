""""
Write a function that takes one parameter called “FullName” and returns two strings. The first is the forename and the second is the surname. Full names will always include a space between the forename and the surname. E.g. “John Smith”.
"""

def name_sep(name):
    name_split=name.split()
    return name_split
name=name_sep(input("please input your full name"))
print("your fist name is", name[0])
print("your second name is", name[1])