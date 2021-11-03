"""
Write a function that returns the basic points value of a word in the game scrabble.
1 point: E, A, I, O, N, R, T, L, S, U.
2 points: D, G.
3 points: B, C, M, P.
4 points: F, H, V, W, Y.
5 points: K.
8 points: J, X.
10 points: Q, Z.
"""

a="EAIONRTLSU";b="DG";c="BCMP";d="FHVWY";e="k";f="JK";g="QZ"
def points(string):
    _=0
    for x in string:
        if x in a:
            _+=1
        elif x in b:
            _+=2
        elif x in c:
            _+=3
        elif x in d:
            _+=4
        elif x in e:
            _+=5
        elif x in f:
            _+=8
        elif x in g:
            _+=10
        else:pass
    return _
print(points(input("please input a word\n").upper()))