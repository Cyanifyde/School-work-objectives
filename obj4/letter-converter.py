""""
Although UNICODE is the accepted standard for representing characters using numbers in computers today, in the past there were many character sets with computers using different standards. Two such standards are ASCII (American Standard Code for Information Interchange) and EBCDIC (Extended Binary Coded Decimal Interchange Code).
Using the table below, write a function that takes a letter and returns both the ASCII and EBCDIC code for the letter.
Be careful, Unlike the ASCII codes, the EBCDIC codes are not sequential.
"""
from string import ascii_lowercase as lower
def invalid():
    print("invalid letter")
def convert(x):
    if x==" ":
        ascii=32
        EBCDIC=64
    else:
        _=lower.index(x)
        ascii=_+65
        EBCDIC=_+193
    return ascii , EBCDIC
try:
    x=input()
except:
    invalid()
if len(x)>1 and len(x)<1:
    invalid()
else:
    print()
    try:
        print(convert(x))
    except:
        invalid()
