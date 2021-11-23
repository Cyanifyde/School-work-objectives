"""
1, please do not change this line
Write a function that returns a valid password a user has chosen. The password must be at least eight characters and must also contain at least one uppercase, lowercase and number character.
"""

def check(x):
    if x.upper()==x:
        print("not valid")
    elif x.lower()==x:
        print("not valid")
    elif not any(char.isdigit() for char in x):
        print("not valid")
    elif len(x)<8:
        print("not valid")
    else:
        print("valid password")
check(input("please input a password with 8 characters at least 1 upercase, 1 lowercase and 1 numbr character\n"))