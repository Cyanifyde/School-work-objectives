""""
Write a function that takes the names of two cities as parameters and returns a string that is the first four characters of each city separated with a dash. For example: London, Madrid would return LOND-MADR
"""
def cities(city1,city2):
    cyty=city1[:4].upper()+"-"+city2[:4].upper()
    return cyty
print(cities(input("please input the first city "),input("please input the second city ")))