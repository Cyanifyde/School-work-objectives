""""
A valid email address must contain an @ symbol and at least one dot. Write a function that provides basic validation of an email address, returning True if the address is valid and False if the address is invalid.
"""
import re 
import dns.resolver 
email=input("please input your email\n")
try:
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        domain = email.rsplit('@', 1)[-1]
        if bool(dns.resolver.resolve(domain,'MX')):
            print("valid email")
        else: print("non-existant email")
    else:
        print("invalid email")
except:
    print("invalid email")