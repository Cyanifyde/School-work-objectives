""""
At a charging point in a supermarket, customers can charge their electric vehicle while they shop. They also gain points to redeem against the cost of their shopping. Customers are charged £1 per session and 20p per minute. There is a minimum 15-minute charge time. The customer is still charged that minimum even if they disconnect before 15 minutes are used. They also gain the minimum number of points though at 22.
Customers gain 1.5 points per minute, rounded down.
Write a function that takes the number of minutes charged and returns two values: the total cost and the points gained.
The program should output the result with the currency formatted with a pound sign and two decimal places.
"""

import math


def cal(time1):
    if time1 <= 15:
        return 400, 22
    else:
        price = time1 * 20 + 100
        points = time1 * 1.5
        x = math.floor(points)
        return price, x


x = cal(int(input("please input the time charged\n")))
print("total cost=£", "{:.2f}".format(x[0] / 100),
      "and the total pionts gained are", x[1])
