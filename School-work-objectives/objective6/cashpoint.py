"""
An automated teller machine (ATM) or cashpoint allows customers to withdraw money in £20, £10 and £5 notes. The machine always dispenses the minimum number of notes. Write a program that would control the actuators dispensing notes from a withdrawal request. The necessary function takes the amount to withdraw as a parameter. A typical output is:
Withdraw: £115.
Dispense £20.
Dispense £20.
Dispense £20.
Dispense £20.
Dispense £20.
Dispense £10.
Dispense £5.
"""


def dispence_ammount(arg):
    lists = []
    currency = [20, 10, 5]
    list_ammount = len(lists)
    ammout = 0
    count = 20
    v = False
    while v == False:
        if ammout < arg:
            ammout += count
            lists.append(count)
        elif ammout > arg:
            ammout -= count
            list_ammount += 1
            count = currency[list_ammount]
            lists.pop()
        else:
            return lists


lists = dispence_ammount(int(input("please input the ammount to withdraw\n")))
for x in lists:
    print("dispence {}".format(x))
