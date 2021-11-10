"""
1, please do not change this line
Write a program that illustrates the depreciation of the value of a car. The program takes three parameters, the year, the value of the car and the minimum resale value. The car depreciates by 30% in the first and second year, and 20% in each subsequent year. The program should output the values from the model until the resale value is reached. E.g.
Car is bought for £12500. Minimum resale value is £6000.
2020: £12500
2021: £8750
2022: £6125
Part exchange in 2022.
"""

def depreciates(year,value,minimum):
    years=0
    reached=False
    while reached==False:
        print(year," : £{0:.2f}".format(value))
        if value>minimum and years ==0 or 1:
            value-=(0.3*value)
        else:
            value-=(0.2*value)
        if value<minimum:
            return year
        year+=1
        years+=1
x=depreciates(int(input("please input the year\n")),int(input("please input the currnt value\n")),int(input("pease input the minimun value\n")))
print("part exchange in {}".format(x))

