#this page is not meant to be readable however please ask me for a description if you want
import os;clear=lambda:os.system("clear");un=[".upm","extra",".git"]
def go_somewhere(_,_1):clear();os.system("python "+_1+"/"+os.listdir(_1)[_-2]);input("\npress enter to go to main menu\n")
def output(list1):
    for f in range (len(os.listdir(list1))):print(f+1,"--",os.listdir(list1)[f-1])
    x=int(input("input the number of the project you want to run\nnote all programms wth 'extra' in their names is just that... they are not to be used for marking\n"));return x;clear()
def main():
    __=([(i)for i in list(filter(os.path.isdir,os.listdir("/home/runner/obs-all")))if i not in un])
    for x in range(len(__)):print(x+1,"--",__[x])
    _=int(input("what objective do you want to run?, enter then number next to the objective\n"));clear();go_somewhere(output(__[_-1]),(__[_-1]))
if __name__=="__main__":
    clear()
    try:main()
    except:pass
os.system("python main.py")