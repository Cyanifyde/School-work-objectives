x=int(input("please input length"))
y=int(input("please input width"))
z=int(input("please input cost per m^2"))
def calculate(x,y,z):
    under=z*3
    greppers=(x*2+y*2)
    carpet=x*y*z
    return (under+greppers+carpet+50)

print("£",calculate(x,y,z))