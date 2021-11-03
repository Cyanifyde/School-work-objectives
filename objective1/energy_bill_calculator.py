""""
Write a subroutine that will output the raw cost of energy usage by taking three parameters: previous meter reading, current reading and calorific value.
The units used equals the current reading minus the previous reading.
kWh = units used * 1.022 * calorific value divided by 3.6.
The calorific value varies a little by each supplier, are governed by legislation and provided by the National Grid. Assume a value of 39.3.
Energy is charged at 2.84p per kWh.
You do not need to format the output because the result is the input to further calculations.
"""

import math
def return_cost(pre,cur,cal):
    unit=cur-pre
    kWh=unit*1.022*(cal/3.6)
    cost=math.floor(((math.floor(kWh))*2.84))
    return cost
previous=float(input("please input the previous value"))
current=float(input("please input the current value"))
calorific_value=float(input("please input the chlorific value"))
cost=return_cost(previous,current,calorific_value)
print("the cost was",cost,"p")