"""
Procedural generation is a popular technique in games design made famous by the 1984 game Elite, where planets in a galaxy and creatures inhabiting those planets were generated using a deterministic algorithm.
Write a function that outputs a description of fictional animals that live on a planet. The function takes the number of the planet as an integer parameter and uses this as a seed for a random number generator so that the same creatures always live on the same planet!
Data might include, but is not limited to:
Creatures: lizards, humanoids, insects
Colours: red, green, blue
Characteristics: shy, angry, docile
An example of an output for a planet might be: “Angry blue humanoids”.
It is important that the outcome is not truly random so that if planet 1652 contains angry blue humanoids, next time it is checked they are still living there and haven’t been replaced by docile red lizards!
"""

creatures = ["lizards", "humanoids", "insects"]
colours = ["red", "green", "blue"]
characteristics = ["shy", "angry", "blue"]
import random

po = []


def seed(x):
    random.seed(x)
    for x in range(3):
        p1 = [1, 2, 3]
        g = p1[(random.randint(1, 3)) - 1]
        print(g)
        po.append(g)

    print("this planet has {} {} {}".format(characteristics[po[0] - 1],
                                            colours[po[1] - 1],
                                            creatures[po[2] - 1]))


seed(int(input("please input any number for a seed\n")))
