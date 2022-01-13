"""
ROT13 ("rotate by 13") is a simple letter substitution cipher that replaces a letter with the 13th letter after it, in the alphabet. E.g. HELLO would become URYYB. Spaces and punctuation are ignored.
ROT13 was once a popular method of obscuring answers to puzzles or to hide spoilers.
Write a subroutine that takes two filenames as parameters. The subroutine applies the ROT13 algorithm to each letter in the original file and outputs the result to a new file. You can make this easier by only handling capital letters if you need to.
"""
import string
alphabet=string.ascii_lowercase
def rotate(letter,times):
    if letter.isupper():
        found=alphabet.index(letter.lower())
        loc=found+times
        try:
            newlett=alphabet[loc]
        except:
            newlett=alphabet[loc - len(alphabet) + len(alphabet)]
        return newlett
    else:
        found=alphabet.index(letter
        loc=found+times
        try:
            newlett=alphabet[loc]
        except:
            newlett=alphabet[loc - len(alphabet) + len(alphabet)].upper()

def words(word,times):
    g=""
    for y in x:
        g+=rotate(y,times)
    return g

def partition(para):
    x=split(para)

        