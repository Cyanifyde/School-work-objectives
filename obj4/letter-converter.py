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
