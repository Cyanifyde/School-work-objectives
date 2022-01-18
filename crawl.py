import os

path = '/home/runner/all/School-work-objectives'
list_dir=[]
for root, directories, files in os.walk(path, topdown=False):
    for name in files:
        if files !=(".git"):
            if name not in (".upm.gitextrasmain.py.breakpointsREADME.mdpoetry.lockpyproject.toml._runhelp.py__pycache__errors.pyfilefiles"):
                print(os.path.join(root, name))
                list_dir.append(os.path.join(root, name))
print(list_dir)