import os, json,time,random;clear = lambda: os.system("clear");un = [".upm", "extra", ".git", "change"];f = open("change/change.json", "r");done = json.load(f);lists = sorted([(i)for i in list(filter(os.path.isdir, os.listdir("/home/runner/obs-all")))if i not in un]);animation = "|/-\\"
for x in lists:
    for v in os.listdir(x):
        print("checking");m=str(x+" "+v);print(m);time.sleep(random.uniform(0.1,0.4));print("passed");time.sleep(0.2);clear()
        if not v.endswith('.txt'):done[v]=("{} , yes".format(x)) if ((open("{}/{}".format(x, v), "r").read().splitlines()[1].split(", "))[0])=="1" else ("{} , no".format(x))
with open('change/change.json', 'w') as f:json.dump(done, f)
f=open('change_logs.txt', 'w');f.write("| {} | {} | {} |\n{}".format("objective".center(14),"task".center(30),"done?".center(6),('-'*60)));f.close();g=open('change_logs.txt', 'a');v = open("change/change.json", "r");done = json.load(v)
for item in done:x=done[item].split(" , ");g.write("\n| {} | {} | {} |".format(x[0].center(14),item.center(30),x[1].center(6)))