""""
A popular function in games design used in acceleration algorithms is to clamp a value. A value cannot exceed a maximum limit. E.g. Clamp(6,50) means return the number 6 or the number 50, whichever is the lowest. 6 would be returned. Clamp(56,50) would return 50 because 56 is greater than 50. Write a function that clamps a variable, always returning an integer.
"""
import os
def a():
    def math(x,y):
        if x>y:
            return y
        else:
            return x
    print("please input the first number")
    x=input()
    print("please input the second number")
    y=input()
    print("returned",math(x,y))
def b():
    class math():
        def __init__(self, no1: float, no2: float):
            self.no1: float= no1
            self.no2: float= no2
        def clamp(self):
            if self.no1<self.no2:return self.no1
            elif self.no1>self.no2:return self.no2
            else:return self.no1
    decision=math(int(input("please input the first number")),int(input("please input the second number")))
    math=decision.clamp()
    print("returned",math)
print("what versin would you like to run? the harder version or the easier version\n1 -- easier\n2 -- harder")
try:
    _=int(input())
except:
    os.system("python obj3/clamp.py")
if _==1:
    a()
else: 
    b()