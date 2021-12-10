"""
Tanks is a game for one player.  At the start of the game, the computer places 10 tanks on an 8x8 board but does not reveal their locations to the player.  Each tank occupies one square on the board.  The player enters a grid reference, e.g. 1,5 on each turn.  The player destroys the tank if the square is occupied by a tank.  The player wins if they destroy all the tanks within 50 turns.
A visualisation of the tanks on the board for one player:
Write a program to play the game.
"""
import random


def variables():
    global rows
    global cols
    global ammount_of_tanks
    global ammount_of_tries

    rows = 8
    cols = 8
    ammount_of_tanks = 10
    ammount_of_tries = 30


def layout():
    global arr
    arr = [[0 for i in range(cols)] for j in range(rows)]
    random_place()


def random_place():
    run = True
    parse = 0
    while run == True:
        parse += 1
        x = random.randint(0, rows - 1)
        y = random.randint(0, cols - 1)
        if arr[x][y] != 1:
            arr[x][y] = 1
        else:
            parse -= 1
        if parse >= ammount_of_tanks:
            run = False


def search(arg, arg1):
    if arr[arg][arg1] == 1:
        arr[arg][arg1] = 0
        return True
    else:
        return False


def check():
    g = False
    for x in arr:
        for v in x:
            if v == 1:
                g = True
    return g


def show():
    for row in arr:
        print(row)


variables()
layout()
run = True
num = 0
while run == True:
    print("try:", num)
    num += 1

    try:
        x = int(input("please input the x value 0-7\n"))
        y = int(input("please input the y value 0-7\n"))
        if search(x, y):
            print("found")
    except:
        pass
    if not check():
        run = False
        print("you have found all of them")
    if num >= ammount_of_tries:
        print("you have not found all of them, here is where they were")
        show()
        run = False
