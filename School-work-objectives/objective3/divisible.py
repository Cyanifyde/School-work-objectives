"""
Write a function that takes two number parameters and divides them by each other. If the division is not possible because the second parameter is zero it should return False. If the second number is exactly divisible by the first number, it returns True. If the second number is not exactly divisible by the first number, it returns False.
"""

num1 = int(input("please input the first number\n"))
num2 = int(input("please input the second number\n"))


def can(num1, num2):
    try:
        dnum = num1 / num2
    except ZeroDivisionError:
        return False
    if dnum - int(dnum) == 0: return True
    else: return False


print(can(num1, num2))
