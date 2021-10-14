import random
def faces(x):
    x=random.randint(1,x)
    return x
print("how many faces are on the die?")
print("you roled a",faces(int(input())))