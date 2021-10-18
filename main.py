#
#this page is not meant to be readable however please ask me for a description if you want
#
import os,time; clear=lambda: os.system("clear")
def go_somewhere(_,_1): clear();os.system("python "+_1+"/"+os.listdir(_1)[_-2]);time.sleep(4)
def output(list1):
    clear()
    for f in range (len(os.listdir(list1))):print(f+1,"--",os.listdir(list1)[f-1])
    x=int(input("input the number of the project you want to run\n"));return x;clear()
def main():
    clear();__=([(i) for i in list(filter(os.path.isdir, os.listdir("/home/runner/obs-all"))) if i!=".upm" and i!="extra" and i!=".git"])
    for x in range (len(__)):print(x+1,"--",__[x])
    _=int(input("what objective do you want to run?, enter then number next to the objective\n"));go_somewhere(output(__[_-1]),(__[_-1]))
if __name__=="__main__":
    clear()
    try:main()
    except:pass
os.system("python main.py")
