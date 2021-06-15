import subprocess
import os
from multiprocessing import Pool

f = "C:/Users/XiMTa/Dropbox/Writings/GitHub/tan19.github.io/Quant/InterviewQuestionBank/source/genTeXJemdoc.py"
subprocess.run(["python", f], shell = True, cwd=os.path.dirname(f))

files = []
for root, subdirs, f in os.walk("./"):
    if f:              
        files += [root + "\\" + x for x in f if ".jemdoc" in x]

def gen(f):
    subprocess.run(["python", 
                    "C:/Users/XiMTa/Dropbox/Writings/GitHub/tan19.github.io/bin/jemdoc", 
                    "-c", "C:/Users/XiMTa/Dropbox/Writings/GitHub/tan19.github.io/bin/mysite.conf", 
                    os.path.basename(f)], shell = True, cwd=os.path.dirname(f))           

if __name__ == '__main__':
    with Pool(16) as p:
        p.map(gen, files)