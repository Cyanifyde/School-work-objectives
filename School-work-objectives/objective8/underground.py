"""
Each line on the London underground has several stations. The Victoria line has these stations in the following order: Brixton, Stockwell, Vauxhall, Pimlico, Victoria, Green Park, Oxford Circus, Warren Street, Euston, King's Cross, Highbury & Islington, Finsbury Park, Seven Sisters, Tottenham Hale, Blackhorse Road and Walthamstow Central.
Write a program that allows the user to input two stations. A function should return the number of stops between the two stations. The station names can be input in any order, but you can make the problem easier by only inputting stations in the correct order if you need to.
"""


def find_similar(x):
    return difflib.get_close_matches(x, lists, cutoff=0.10, n=1)[0]


def search():
    v = False
    for x in range(len(lists) - lists.index(name1)):
        if name2 == lists[x + lists.index(name1)]:
            return x - 1
            v = True
    if v == False:
        for x in range(len(lists) - lists.index(name2)):
            if name1 == lists[x + lists.index(name2)]:
                return x - 1
                v = True


import difflib
global name1
global name2
global lists
lists = [
    "Brixton", "Stockwell", "Vauxhall", "Pimlico", "Victoria", "Green Park",
    "Oxford", "Circus", "Warren Street", "Euston", "King's Cross",
    "Highbury & Islington", "Finsbury Park", "Seven Sisters", "Tottenham Hale",
    "Blackhorse Road", "Walthamstow Central"
]

name1 = input()
name2 = input()
name1 = find_similar(name1)
name2 = find_similar(name2)
print("there are {} stops between {} and {}".format(search(), name1, name2))
