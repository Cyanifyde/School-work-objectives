""""
A valid email address must contain an @ symbol and at least one dot. Write a function that provides basic validation of an email address, returning True if the address is valid and False if the address is invalid.
"""

import re 
import dns.resolver 
email=input("please input your email\n")
def emailmx(email):
    domain = email.rsplit('@', 1)[-1]
    try:
        if bool(dns.resolver.resolve(domain,'MX')):
            print("valid email")
    except: print("non-existant email")
if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    emailmx(email)
else:
    print("invalid email")