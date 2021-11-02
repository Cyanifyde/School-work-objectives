"""
The inventory of a character in a computer game is stored in a single string. Write a function called “Exists” that checks if an item is in the player’s inventory or not.
The inventory could be, “Sword, Shield, Potion, Amulet”.
The items to check could be, “Shield”, “Potion”, “Charm” and “Bow”.
"""

inventory=["sword", "shield", "potion", "amulet"]
def exists(item):
    if item in inventory:
        return True
    else:
        return False
print(exists(input("please input the searched item ").lower()))