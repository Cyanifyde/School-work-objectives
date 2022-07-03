import json
import requests
import time
from _runhelp import file


def filecheckup():
    #a function that checks for updates of specific files from the server
    files = [
        "vend.json", "cookie.json", "gamertag.json", "notes.json",
        "attributes.txt"
    ]
    for x in files:
        #itterates over the files
        if x.endswith(".json"):
            #checks if the files end with .txt or .json as different reponse queries need to be used for each type
            
            v = file(x).get(0)[0]
            response = requests.get(
                "https://api.ent1ty.space/api/data/file?get=true&file={}".format(
                    x))
            #gets a response from the server
            try:
                #opens the file with exception handling
                with open(v) as f:
                    notes = json.load(f)
            except:
                notes = {}
            if notes == {}:
                #if the file is empty the file is downloaded
                print("file {} has data not synced with server".format(v))
                g = open(v, "w")
                g.write(response.text)
                print("syncing")
                g.close()
                time.sleep(0.5)
            elif eval(response.text) != notes:
                #if file isnt empty but is different the file is sent to the server for the server to hold data
                print("file {} has data not synced with server".format(v))
                requests.post(
                    "https://api.ent1ty.space/api/data/files?file={}".format(x),
                    json=notes)
                print("syncing")
                time.sleep(0.5)
        elif x.endswith("txt"):
            v = file(x).get(0)[0]
            response = requests.get(
                "https://api.ent1ty.space/data/file?get=true&file={}".format(
                    x))
            notes = open(v, "r")
            notes = notes.read()
            if notes == "":
                print("file {} has data not synced with server".format(v))
                g = open(v, "w")
                g.write(response.text)
                print("syncing")
                g.close()
                time.sleep(0.5)
            elif response.text != notes:
                print("file {} has data not synced with server".format(v))
                requests.post(
                    "https://api.ent1ty.space/api/data/files?file={}".format(x),
                    data=notes)
                print("syncing")
                time.sleep(0.5)
