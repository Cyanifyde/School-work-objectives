def cities(city1,city2):
    cyty=city1[:4].upper()+"-"+city2[:4].upper()
    return cyty
print(cities(input("please input the first city "),input("please input the second city ")))