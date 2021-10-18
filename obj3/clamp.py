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