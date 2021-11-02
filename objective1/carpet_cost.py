""""
Write a subroutine that outputs the cost of fitting a carpet using 3 parameters:
Width of the room in metres.
Length of the room in metres.
Price of carpet per m2.
Underlay for the carpet will also be required at £3 per m2.
Grippers will be required at £1/m: width * 2 + length * 2
The fitting fee is £50.
Test the program with a 7 x 6m room and a £17m2 carpet.
E.g. 7m x 6m room with a £17 carpet = £714 + £126 + £26 + £50 = £916
"""
x=int(input("please input length"))
y=int(input("please input width"))
z=int(input("please input cost per m^2"))
def calculate(x,y,z):
    under=z*3
    greppers=(x*2+y*2)
    carpet=x*y*z
    return (under+greppers+carpet+50)
print("£",calculate(x,y,z))