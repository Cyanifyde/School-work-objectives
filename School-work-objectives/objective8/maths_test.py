"""
Write a program that generates a short test of the addition of two-digit numbers. The test contains five questions. The child taking the test enters their name at the start of the test. The program stores the name of the child and their score out of five. It resets the test at the end, ready for the next child who will see the same questions.
The names and scores are output before the next test starts.
"""

import random
import os

clear = lambda: os.system("clear")


def randoms():
    return random.randint(10, 99)


def test_create():
    global x
    global y
    x = [randoms() for x in range(5)]
    y = [randoms() for x in range(5)]


def gather_name():
    try:
        name = input("please input your name or 'exit' to exit\n")
    except:
        name = None
    return name


def gather_answer():
    try:
        number = int(input("what is the answer to this question?\n"))
    except:
        number = None
    return number


global names
global score
names = []
score = []


def store_name(x):
    names.append(x)


def store_score(x):
    score.append(x)


def display():
    for i in range(len(names)):
        print(names[i], "got", score[i], "points")


def main(name_cur):
    score_cur = 0
    for i in range(5):
        print(x[i], "+", y[i])
        answer = gather_answer()
        if answer == x[i] + y[i]:
            score_cur += 1

    store_name(name_cur)
    store_score(score_cur)
    clear()
    display()


test_create()
running = True
while running == True:
    name_cur = gather_name()
    if name_cur == "exit":
        clear()
        display()
        running = False
    else:
        main(name_cur)
