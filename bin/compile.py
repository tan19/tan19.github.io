import subprocess
from os import walk

files = []
for root, subdirs, f in walk("../"):
    if f:        
        files += [root + "\\" + x for x in f if ".jemdoc" in x]

for f in files:    
    subprocess.run(["python", "bin/jemdoc", f], shell = True)