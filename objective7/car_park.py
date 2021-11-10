"""
A local car park has the following charges:
Up to 1 hour		£1.50
Up to 2 hours	£2.90
Up to 3 hours	£3.90
Up to 4 hours	£4.50
4 hours +		£8.00
Between 8pm and 6am	Free
Disabled users	Free for the first 3 hours
		Additional hours charged
Write a program that allows the user to input the time they arrive, the time they leave and whether they are a disabled blue badge holder. The program outputs the total charge for parking. The times are entered using the 24-hour clock in the format 00:00. E.g. 6pm would be entered as 18:00.
"""

timei = input()
timel = input()
blue = input()
from datetime import datetime


def bluebadge(blue):
    if blue.lower() == "yes":
        return True
    else:
        return False


def format(s, l):
    s1 = datetime.strptime(s, "%H:%M")
    s1 = s1.strftime("%H%M")
    l1 = datetime.strptime(l, "%H:%M")
    l1 = l1.strftime("%H%M")
    return s1, l1


def check_outtime(s1, l1):
    if 1800 < int(s1) < 2400 and 1800 < int(l1) < 2400 or 0 < int(
            s1) < 600 and 0 < int(l1) < 600:
        print("it is free")
        return False
    else:
        return True


def cost_disabled(s, l):
    s1, l1 = format(s, l)
    f = check_outtime(s1, l1)
    if f:
        if int(l1)-int(s1)==3:
            print("it is free")
            return
        else:
            pass
    lists=["£1.50","£2.90","£3.90","£4.50","£8.00"]
    
    d=int(l1)-int(s1)-3

    print(round(d,2))
    try:
        print("it costs",lists[d])
    except:
        print("it costs",lists[4])
    



def cost(s, l):
    lists=["£1.50","£2.90","£3.90","£4.50","£8.00"]
    s1, l1 = format(s, l)
    f = check_outtime(s1, l1)
    if f:
        d=l1-s1
        try:
            print("it costs",lists[d])
        except:
            print("it costs",lists[4])


if bluebadge(blue) == False:
    cost(timei, timel)
else:
    cost_disabled(timei, timel)
