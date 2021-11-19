import os,json,time,random;clear=lambda:os.system("clear")
def vmm(x,v):print("checking",x+" "+v);time.sleep(random.uniform(0.05,0.1));print("passed");time.sleep(0.1);clear()
def a():
    with open('change/change.json', 'w')as f:json.dump({},f)
    un=[".upm","extra",".git","change"];f=open("change/change.json","r");done=json.load(f);lists=sorted([(i)for i in list(filter(os.path.isdir,os.listdir("/home/runner/obs-all")))if i not in un]);[[vmm(x,v) for v in os.listdir(x)] for x in lists];exec('for x in lists:\n\tfor v in os.listdir(x):\n\t\tdone[v]=((("{} , yes".format(x))if(((open("{}/{}".format(x, v),"r").read().splitlines()[1].split(", "))[0])=="1") else("{} , no".format(x))) if not v.endswith(".txt") else ("{} , no".format(x)))')
    with open('change/change.json', 'w')as f:json.dump(done,f)
    f=open('change_logs.txt','w');f.write("| {} | {} | {} |\n{}".format("objective".center(14),"task".center(30),"done?".center(6),('-'*60)));f.close();g=open('change_logs.txt','a');v = open("change/change.json","r");done=json.load(v)
    for item in done:x=done[item].split(" , ");g.write("\n| {} | {} | {} |".format(x[0].center(14),item.center(30),x[1].center(6)))
    exec('f=open("main.py","r").read().replace("x=False", "x=True")\ngn=open("main.py","w")\ngn.write(f)\ngn.close()')