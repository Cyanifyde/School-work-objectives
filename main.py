"""
look at change_logs.txt to see if the wanted program is finished
DO NOT CHANGE main.py or any file in /change
"""
x=True #change this to  False to run change log updater

import os;clear=lambda:os.system("clear")
un=[".upm","extra",".git","change","extras","main.py","update.txt",".breakpoints","change_logs.txt","README.md","poetry.lock","pyproject.toml"];exec("if x==False:change.changelog.a()")
def paths(x):return sorted([(i)for i in list (os.listdir(x))if i not in un])
def send(x):clear();os.system("python "+x);_=("" if input("\npress enter to go to rerun\nor input anything else to return\n")!="" else x) ;f=open("update.txt","w");f.write(_);f.close()
def recursion(x):v=paths(x);[print(str(x)+" --- "+v[x]) for x in range (len(v))];_=int(input("what file do you want to open / run?\n"));pathn=x+"/"+str(v[_]);clear();return pathn
def main():
    po=True;path="/home/runner/all"
    while po==True:
        try:path=recursion(path)
        except NotADirectoryError:send(path);po=False;clear()
f=open("update.txt","r");f=f.read()
try:clear();send(f) if f!="" else main()
except:f=open("update.txt","w");f.write("");f.close()
os.system("python main.py")