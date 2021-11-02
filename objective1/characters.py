""""
Write a program to produce the following output:
The digits are: 0123456789
The characters are: abcdABCD@#!£
The alphanumerics are: 0123456789 abcdABCD@#!£
"""

def chars():
    numbers="0123456789"
    characters="abcdABCD@#!£"
    alphanumerics=numbers+characters
    print("the digits are:",numbers)
    print("The characters are:",characters)
    print("the alphanumerics are:", alphanumerics)
chars()