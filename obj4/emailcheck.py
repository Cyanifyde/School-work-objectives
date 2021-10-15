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