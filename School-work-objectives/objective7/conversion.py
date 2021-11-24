"""
A utility program converts metric and imperial measurements. E.g. feet to meters, stones to kilograms. Research the different conversion calculations and create the utility program. The user can select a conversion they require, input the value and the program outputs the conversion.
"""

lists = [
    0.3936, 2.54, 3.2808, 0.3048, 39.37, 0.254, 10.76, 0.0929, 35.314, 0.0283,
    2.205, 0.4536
]
lists2 = ["cm", "in", "m", "in", "m^2", "sq.ft", "m^3", "c.f", "kg", "lb"]


def get_inp(lists, lists2):
    x = len(lists2) // 2
    for y in range(x):
        print(lists2[y * 2], lists2[y * 2 + 1])
    v = input("what conversion unit do you have ie cm\n")
    p = lists2.index(v)
    if p % 2 == 0:
        print("so you would like to convert {} to {}".format(
            lists2[p], lists2[p + 1]))
        g = lists[p]
    else:
        print("so you would like to convert {} to {}".format(
            lists2[p], lists2[p - 1]))
        g = lists[p]
    if input() != "yes":
        return ""
    num = int(input("please input a number\n")) * g
    return num


try:
    print("the original number converted is", get_inp(lists, lists2))
except:
    pass
