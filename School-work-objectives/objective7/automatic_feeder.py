"""
An automatic animal feeder dispenses different types of food and different quantities. “Breakfast” outputs hopper 1, “Lunch” outputs hopper 2, “Dinner” outputs hopper 1 and hopper 2. The user can enter one of the three options and how much to dispense. E.g.
Breakfast
2
Would result in the output:
Hopper 1
Hopper 1
Write a program to simulate the automatic feeder.
"""


def hopper(arg):
    arg = arg.lower()
    if arg == "breakfast":
        return 1
    if arg == "lunch":
        return 2
    if arg == "dinner":
        return 3


def send(arg, ammount):
    for x in range(ammount):
        if arg == 1:
            print("hopper 1")
        elif arg == 2:
            print("hopper 2")
        else:
            print("both hoppers")


try:
    send(hopper(input("please input the time ie 'lunch'\n")),
         int(input("please input the amount\n")))
except:
    print("error")
