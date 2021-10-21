"""
When keeping fish, one of the goals to reduce algae is to keep nitrates to a minimum. One way of doing this is to dose a carbon source which nitrifying bacteria within an aquarium consume together with nitrates. The carbon source must be dosed very precisely.
Write this function to determine and return the dose.
The program should output:
“For x nitrate dose y ml”
Where x is the parameter and y is the returned value.
"""
def choice(a):
    if a>=10:
        return 3
    elif a>=2.5:
        return 2
    elif a>=1:
        return 1
    else: 
        return 0.5
x1=int(input("please input ammount of nitrogen"))
x=choice(x1)
print("For",x1,"nitrate dose",x,"ml")