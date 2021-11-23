""""
1, please do not change this line
A popular function in games design used in acceleration algorithms is to clamp a value. A value cannot exceed a maximum limit. E.g. Clamp(6,50) means return the number 6 or the number 50, whichever is the lowest. 6 would be returned. Clamp(56,50) would return 50 because 56 is greater than 50. Write a function that clamps a variable, always returning an integer.
"""

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