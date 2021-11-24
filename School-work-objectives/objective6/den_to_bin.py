"""
Write a function that converts a denary number into a binary number using the repeated division by two algorithm:
The number to be converted is divided by two.
The remainder from the division is the next binary digit. Digits are added to the front of the sequence.
The result is truncated so that the input to the next division by two is always an integer.
The algorithm continues until the result is 0.
E.g.
"""


def pass_list(arg):
    string = ""
    for x in arg:
        string += str(x)
    return string[::-1]


def divide(arg):
    return arg // 2


def check(arg):
    if arg % 2 == 0:
        return True
    else:
        return False


def convert(num):
    lists = []
    done = False
    while done == False:
        x = divide(num)
        x2 = check(num)
        if x2 == True:
            lists.append(0)
        else:
            lists.append(1)
        if x == 0:
            return lists
        else:
            num = x


number = int(input("please input a number\n"))
print("the number {} in binary is {}".format(number,
                                             pass_list(convert(number))))
