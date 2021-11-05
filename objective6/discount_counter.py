"""
An electronic advertising board illustrates a sale at 60% off. To make this more eye-catching, the number shown starts at 10 and increases by a random amount until 60 is reached. Write an algorithm that will achieve this. E.g.
10% off.
24% off.
48% off.
60% off.
"""
from random import randint as random 
def pick_random():
    num=random(1,20)
    return num
def check(arg):
    if arg <60:
        num=pick_random()
        if (num+arg)>60:
            return arg+1
        else:
            return arg+num
    else:
        return 60
n=False
arg=0
while n ==False:
    arg=check(arg)
    if arg==60:
        n=True
    print(arg)

