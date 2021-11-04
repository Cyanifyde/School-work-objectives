"""
The top prize in a lottery is won by matching three numbers between 1 and 30 to three random numbers drawn in the same order. When a ball is drawn it is put back into the machine before another ball is drawn. There are always 30 balls in the machine before a ball is drawn and a player may choose the same ball more than once. A draw takes place once a week. Write a function that takes three numbers as parameters, draws three random numbers between 1 and 30 and returns the number of weeks it took to win the jackpot. E.g.
Numbers chosen: 17, 12, 25 must match: ball one is 17, ball two is 12, ball three is 25.
"""

import random
def choose(*arg):
    ount=0
    for x in arg:
        y=random.randint(1,30)
        print("the nuber",y,"was drawn")
        if x==y:
            ount+=1
    if ount==3:
        return True
f=open("objective6/week.txt","r")
v=f.read()
if choose(*((int(input("please input the "+str(x+1)+" number\n"))) for x in range (3))) :
    print("you won in",int(v)+1,"weeks")
else:
    print("\nyou lost")
    f=open("objective6/week.txt","w")
    v=int(v)+1
    f.write(str(v))
    f.close()