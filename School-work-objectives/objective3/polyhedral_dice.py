""""
1, please do not change this line
In role playing and board games it is common to have dice with more or less than six sides. D2, D4, D8, D10, D12, D20 are often used. 
Write a function that takes one parameter: the number of faces on a dice. The function should return a random roll of the dice.
"""

import random
def faces(x):
    x=random.randint(1,x)
    return x
print("how many faces are on the die?")
print("you roled a",faces(int(input())))