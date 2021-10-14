print()
import math
def cal(time1):
    if  time1<= 15:
        return 400,22
    else:
        price=time1*20+100
        points=time1*1.5
        x=math.floor(points)
        return price,x
x=cal(int(input()))
print("total cost=£","{:.2f}".format(x[0]/100),"and the total pionts gained are",x[1])