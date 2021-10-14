def chars():
    #cant start a int with 0 so currently stored as a string
    numbers="0123456789"
    #list of some commonly used characters
    characters="abcdABCD@#!£"
    #alphanumerics is a group of characters from both nubers and characters
    alphanumerics=numbers+characters
    print("the digits are:",numbers)
    print("The characters are:",characters)
    print("the alphanumerics are:", alphanumerics)
chars()