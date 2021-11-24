"""
Write a program that repeatedly asks a user for a positive number until no number is entered. The program outputs the highest number, the total and the average of the numbers entered.
"""

lists = []
g = True


def save(x):
    lists.append(x)
    return lists


def decision(lists):
    top = 0
    tot = 0
    av = 0
    for x in lists:
        tot += x
        if x > top:
            top = x
    av = tot / len(lists)
    return tot, top, av


while g == True:
    try:
        v = int(
            input(
                "please input a number to add to the list or press enter to run all calculations\n"
            ))
        save(v)
    except ValueError:
        g = False
ran = decision(lists)
print("the numbers inputed are are")
for x in range(len(lists)):
    print(lists[x])
print()
print("the total is {}\nthe largest number is {}\nth average is {}".format(
    ran[0], ran[1], ran[2]))
