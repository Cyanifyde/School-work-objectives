""""
Write two subroutines that convert between centigrade and Fahrenheit using the formula: F = (C * 1.8) + 32
One subroutine takes the temperature in degrees centigrade as a parameter and returns Fahrenheit.
The second subroutine takes the temperature in degrees Fahrenheit as a parameter and returns centigrade.
E.g. 30°C = 86°F
(30°C * 1.8) + 32 = 86°F
"""

def FtoC(F):
    return (F-32)/1.8
def CtoF(C):
    return (C*1.8)+32
C=30
F=CtoF(C)
print(C,"degrees C is",F,"degrees F")