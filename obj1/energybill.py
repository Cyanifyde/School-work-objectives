import math
def return_cost(pre,cur,cal):
    unit=cur-pre
    kWh=unit*1.022*(cal/3.6)
    cost=math.floor(((math.floor(kWh))*2.84))
    return cost
previous=float(input())
current=float(input())
calorific_value=float(input())
cost=return_cost(previous,current,calorific_value)
print("the cost was",cost,"p")