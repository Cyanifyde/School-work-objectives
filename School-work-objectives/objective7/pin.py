"""
A personal identification number (PIN) is four digits. E.g. 2345. Write a function that allows the user to enter a PIN. The program outputs, “Hello” if the user enters the PIN correctly. If the user makes three incorrect attempts the program outputs, “Locked out”.
"""

password = "0123"


def program(count, inp, passw):
    if inp == passw and count <= 3:
        return "hello"
    elif count > 3:
        return "locked out"
    else:
        return "incorrect"


x = "incorrect"
_ = 0
while x != "hello" and x != "locked out":
    _ += 1
    x = program(_, input("please input your password\n"), password)
    print(x)
