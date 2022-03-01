"""
A strong number is a number whose sum of the factorial of digits is equal to the original number.
E.g. 145 is strong number because 1! + 4! + 5! = 145. 
That is: (1*1) + (4*3*2*1) + (5*4*3*2*1) = 145
Write a program that allows the user to enter an integer. The program outputs whether the number is strong or not and ensures that an arithmetic overflow cannot crash the program.
"""


def factorial(*arg):
    v = 0
    for x in arg:
        x = int(x)
        fact = 1
        for i in range(1, x + 1):
            fact = fact * i
        v += fact
    return v


def calculate(*arg):
    number = 0
    for x in arg:
        x = int(x)
        number += x * x
    return number


num = str(input("please input a number\n"))
v = str(factorial(*(num[x] for x in range(len(num)))))
if v == num:
    print("it is a strong number")
else:
    print("not a strong number")
