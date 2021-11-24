"""
Write a function called SqRoot that calculates the square root of a number, X using Newton’s method.
Root = X at the start of the algorithm.
Root is repeatedly recalculated as 0.5*(Root+(X/Root) until the value of Root does not change. E.g. the square root of 64 can be calculated in the sequence of steps:
64
32.5
17.234615384615385
10.474036101145005
8.292191785986859
8.005147977880979
8.000001655289593
8.00000000000017
8.0
8.0 – This value equals the previous value of Root.
"""


def SqRoot(x):
    root = x
    v = False
    while v == False:
        last = root
        root = 0.5 * (root + (x / root))
        if last == root:
            return root


inp = int(input("please input a number\n"))
print("the square root of {} is  {}".format(inp, SqRoot(inp)))
