"""
ROT13 ("rotate by 13") is a simple letter substitution cipher that replaces a letter with the 13th letter after it, in the alphabet. E.g. HELLO would become URYYB. Spaces and punctuation are ignored.
ROT13 was once a popular method of obscuring answers to puzzles or to hide spoilers.
Write a subroutine that takes two filenames as parameters. The subroutine applies the ROT13 algorithm to each letter in the original file and outputs the result to a new file. You can make this easier by only handling capital letters if you need to.
"""
import string
from _runhelp import file

print("please input new things to 'ROT13.txt'")
x = input("press enter when you have added new stuff")
v = file("rot13.txt").get(0)[0]
end = file("rot13_end.txt").get(0)[0]
alphabet = string.ascii_lowercase


def rotate(letter, times):
    try:
        if letter.isupper():
            found = alphabet.index(letter.lower())
            loc = found + times
            try:
                newlett = alphabet[loc].upper()
            except:
                newlett = alphabet[found - len(alphabet) + times].upper()
        elif not letter.isupper():
            found = alphabet.index(letter)
            loc = found + times
            try:
                newlett = alphabet[loc]
            except:
                newlett = alphabet[found - len(alphabet) + times]
    except:
        newlett = letter
    return newlett


def words(word, times):
    g = ""
    p = []
    for x in word:
        g = ""
        for letter in x:
            g += rotate(letter, times)
        p.append(g)
    return p


def reinput(list):
    return ' '.join(list).replace('\n ', '\n')


def partition(para):
    return words(para.splitlines(True), 13)


g = open(v, "r").read()
lel = partition(g)
g = open(end, "w")
g.write(reinput(lel))
g.close()
print("output saved to 'ROT13_END.txt'")
