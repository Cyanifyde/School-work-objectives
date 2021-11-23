"""
1, please do not change this line
The computer and player choose one of rock, paper, or scissors.  The output of the encounter is then displayed with rock beating scissors, scissors beating paper, and paper beating rock.  The winner scores 1 point for a win.  The score for both players should be output.  The game is won when one player reaches 10 points.
"""

from random import randint as random 
classes=["rock","paper","scissors"]
def point(*arg):
    p1=classes.index(arg[0])
    p2=arg[1]
    if p1 == 0 and p2 ==1:
        return "player"
    elif p1 ==1 and p2 ==2:
        return "player"
    elif p1 ==2 and p2 ==0:
        return "player"
    elif p1 == p2:
        return None
    else:
        return "computer"
def game():
    count=[0,0]
    finished =False
    while not finished:
        p1=input("input rock paper or scissors")
        computer=random(0,3)
        x=point(p1,computer)
        if  x=="player":
            print("player wins")
            count[0]+=1
        elif x =="computer":
            print("computer wins")
            count[1]+=1
        else:
            print("draw")
        if count[0] ==10 or count[1]==10:
            finished=True
game()