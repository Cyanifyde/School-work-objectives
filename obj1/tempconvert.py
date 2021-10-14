#temperature converter problem
#subrutine to convert farenheght to centigrade
def FtoC(F):
    return (F-32)/1.8
#subroutine to convert centigrade to farenheight
def CtoF(C):
    return (C*1.8)+32

#main program
C=30
F=CtoF(C)
print(C,"degrees C is",F,"degrees F")