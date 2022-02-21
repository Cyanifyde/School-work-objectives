import json
import requests 
import time
from _runhelp import file
def filecheckup():
    files=["vend.json","cookie.json","gamertag.json","notes.json","attributes.txt"]
    for x in files:
        if x.endswith(".json"):
            v = file(x).get(0)[0]
            response=requests.get("https://api.ent1ty.space/data/{}?get=true".format(x))
            global notes
            try:
                with open(v) as f:
                    notes = json.load(f)
            except:
                notes = {}
            if notes=={}:
                print("file {} has data not synced with server".format(v))
                g = open(v, "w")
                g.write(response.text)
                print("syncing")
                g.close()
                time.sleep(0.5)
            elif response.json() != notes:
                print("file {} has data not synced with server".format(v))
                response=requests.get("https://api.ent1ty.space/data/{}?get=false&update={}".format(x,notes))
                print("syncing")
                time.sleep(0.5)
        elif x.endswith("txt"):
            v = file(x).get(0)[0]
            response=requests.get("https://api.ent1ty.space/data/{}?get=true".format(x))
            notes = open(v, "r")
            notes=notes.read()
            if notes=="":
                print("file {} has data not synced with server".format(v))
                g = open(v, "w")
                g.write(response.text)
                print("syncing")
                g.close()
                time.sleep(0.5)
            elif response.text != notes:
                print("file {} has data not synced with server".format(v))
                response=requests.get("https://api.ent1ty.space/data/{}?get=false&update={}".format(x,notes))
                print("syncing")
                time.sleep(0.5)
                