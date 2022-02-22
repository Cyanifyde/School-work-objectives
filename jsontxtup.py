import json
import requests 
import time
from _runhelp import file
def lol():

    url = 'https://www.w3schools.com/python/demopage.php'
    myobj = {'somekey': 'somevalue'}
    
    x = requests.post(url, data = myobj)
    
    print(x.text)
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
            elif eval(response.text) != notes:
                print("file {} has data not synced with server".format(v))
                requests.post( "https://api.ent1ty.space/data/drop/{}".format(x), json = notes)
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
                requests.post("https://api.ent1ty.space/data/drop/{}".format(x), data = notes)
                print("syncing")
                time.sleep(0.5)
                