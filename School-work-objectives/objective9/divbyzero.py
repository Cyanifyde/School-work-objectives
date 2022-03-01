"""
Write a function that takes two parameters and returns the division of the two numbers. A division by zero should be handled so the program does not crash, but instead returns, “E”.
"""
def Divide(Number1, Number2):
    try:
        Result = Number1 / Number2
        return Result

    except:
        return "E"


print(Divide(12, 0))
