"""
Write a function to return whether a number is happy or sad.  A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number either equals 1, or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are sad numbers.  When the algorithm ends in a cycle of repeating numbers, this cycle always includes the number 4.
E.g. 19 is a happy number:
"""

def calculate(*arg):
    number=0
    for x in arg:
        x=int(x)
        number+=x*x
    return number
def happy(num):
    halt=False
    while halt==False:
        v=calculate(*(num[x] for x in range (len(num))))
        if v==1:
            return True
        elif v==4:
            return False
        else:
            num=str(v)
print("happy" if happy(str(input("input a number\n"))) else "sad")
