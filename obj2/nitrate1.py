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