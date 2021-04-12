import re
import subprocess
from collections import defaultdict
import os

from .CProblem import *

def Read_Problems(rootdir = "./Problems") -> list():
    files = []
    for root, subdirs, f in os.walk(rootdir):
        if f:
            files += [root + "\\" + x for x in f]

    pList = []
    for i, filename in enumerate(files):
        Metadata, Question, Answer = re.split('# \w+\n', open(filename, "r").read())[1:]        

        # Metadata pre-processing
        Title, Difficulty, Category, Tags, Source = re.split('> .+: ', Metadata)[1:]
        Metadata = dict(zip(["FileName", "Title", "Difficulty", "Category", "Tags", "Source"], 
                            [os.path.basename(filename), Title.strip(), Difficulty.strip(), Category.strip(), Tags.strip(), Source.strip()]))

        # Question pre-processing
        Question = re.sub(r"\*\*([\w+ ]+)\*\*", r"{\\bf{\1}}", Question) # bold font        
        Question = re.sub(r"```([^`]+)```", r"\\begin{verbatim}\1\\end{verbatim}\n", Question) # code
        
        # Answer pre-processing
        Answer = re.sub(r"\*\*([\w+ ]+)\*\*", r"{\\bf{\1}}", Answer) # bold font
        Answer = re.sub(r"```([^`]+)```", r"\\begin{verbatim}\1\\end{verbatim}\n", Answer) # code

        pList.append(Problem(Metadata, Question, Answer))

    return pList

def Generate_TeX_Source_File(pList) -> str():
    Q = defaultdict(lambda: defaultdict(lambda: defaultdict(str)))
    A = defaultdict(lambda: defaultdict(str))

    for i, problem in enumerate(pList):
        FileName, Title, Difficulty, Category, Tags, Source = problem.Metadata.values()
        Question = problem.Question
        Answer = problem.Answer

        Part, Chapter, Section = Category.split("/")

        Q[Part][Chapter][Section] += "\\begin{question}{" + Title + "}{" + Difficulty + "}{\#" + FileName + "; " + Tags + "; " + Source + "}\n"
        Q[Part][Chapter][Section] += Question
        Q[Part][Chapter][Section] += "\\end{question}\n\n"

        # answers are chapter-wise
        A[Part][Chapter] += "\\begin{answer}{" + Title + "}\n"
        A[Part][Chapter] += Answer
        A[Part][Chapter] += "\\end{answer}\n"

    body = ""
    for Part in Q:
        body += "\\part{" + Part + "}\n"
        for Chapter in Q[Part]:
            body += "\\chapter{" + Chapter + "}\n"
            body += "\\minitoc\n"
            for Section in Q[Part][Chapter]:
                body += "\section{" + Section + "}\n"
                body += Q[Part][Chapter][Section]
            body += "\\newpage\section{Chapter Answers}"
            body += A[Part][Chapter]
    
    pre  = open("LaTex/pre.txt", "r").read()
    post = open("LaTex/post.txt", "r").read()    
    tex  = pre + body + post

    return tex

def Write_pdf_File(tex):
    f = open("LaTeX/InterviewQuestionBank.tex", "w")
    f.write(tex)
    f.close()
    
    subprocess.run(["pdflatex", "-output-directory=_build", "LaTeX/InterviewQuestionBank.tex"], shell = True)