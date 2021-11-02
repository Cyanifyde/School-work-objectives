"""
Prime numbers are the positive integers greater than 1 that are only divisible by 1 and itself. For example: 2, 3, 5, 7, 11 etc...
Write a function called, “IsPrime” that takes a number as a parameter and returns True if the number is a prime number and False if it is not a prime number.
Starting from two and counting up until the number halved is reached, if the number divided by the counter at any point has no remainder the number is not prime.
This is not a very efficient algorithm, but it works!
"""

true=[]
def IsPrime(param):
    for x in range (param//2-1):
        y=str(param/(x+2)).split(".")
        if y[1]!="0":
            true.append(0)
        else:
            true.append(1)
    return true
print("not a prime" if 1 in IsPrime(int(input("input a number\n"))) else "is a prime")