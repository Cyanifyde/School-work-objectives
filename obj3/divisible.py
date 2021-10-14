num1=int(input("please input the first number\n"));num2=int(input("please input the second number\n"))
def can(num1,num2):
    try:dnum=num1/num2
    except ZeroDivisionError:return False
    if dnum - int(dnum) == 0:return True
    else:return False
print(can(num1,num2))