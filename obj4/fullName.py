def name_sep(name):
    name_split=name.split()
    return name_split
name=name_sep(input("please input your full name"))
print("your fist name is", name[0])
print("your second name is", name[1])