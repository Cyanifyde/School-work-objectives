""""
1, please do not change this line
The actual size of a cell viewed under a light microscope is 80μm (micrometres). It measures 4cm on the slide. Calculate the magnification.
The size on the slide multiplied by 10,000 converts the measurement to μm. Divide this by the actual size to determine the magnification.
"""

def calculate(x,y):
    return y/(x*10000)
x=float(input("please input the actual size in micrometers"))
y=float(input("please input the viewed size in cm"))
print(calculate(x,y))