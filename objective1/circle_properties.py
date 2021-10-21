""""
Write a subroutine that outputs the following properties of a circle
from the diameter and arc angle:
The radius of the circle (diameter divided by 2).
The area of the circle (3.14 multiplied by the radius squared).
The circumference of the circle (3.14 multiplied by the diameter).
The arc length (circumference multiplied by the arc angle), divided by 360.
"""

diameter=float(input("please enter the diameter"))
radius=diameter/2
area=radius*radius*3.14
circumference=3.14*diameter
print(radius)
print(area)
print(circumference)