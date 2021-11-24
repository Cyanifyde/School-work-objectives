""""
Write a subroutine that will output the volume of a fish tank. To calculate volume in litres, multiply length by depth by height and divide by 1000.
"""


def volume(length, depth, height):
    volume = length * depth * height
    volume = volume // 1000
    return volume


length = int(input("please input a length\n"))
depth = int(input("please input a depth\n"))
height = int(input("please input a height\n"))
volume = str(volume(length, depth, height))
print("the volume is " + volume + "l")
