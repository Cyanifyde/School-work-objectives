inventory=["sword", "shield", "potion", "amulet"]
def exists(item):
    if item in inventory:
        return True
    else:
        return False
print(exists(input("please input the searched item ").lower()))
