import dns.resolver 
x=input("please input your email\n")
domain = x.rsplit('@', 1)[-1]
try:
    print("email is valid" if bool(dns.resolver.resolve(domain,'MX'))==True else "false")
except:
    print("email not vaid")