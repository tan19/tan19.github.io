import pandas as pd

import re
import subprocess
from collections import defaultdict
import os

def Read_Problems(rootdir = "../Problems"):
    files = [root + "\\" + x for root, _, f in os.walk(rootdir) for x in f if f]
    
    ProblemSet = [[] for _ in range(len(files))]
    for i, filename in enumerate(files):
        FileName = os.path.basename(filename)

        Metadata, Question, Answer = re.split('# \w+\n', open(filename, "r").read())[1:]                

        # Metadata pre-processing        
        Title, Difficulty, Category, Tags, Source = [s.strip() for s in re.split('> .+: ', Metadata)[1:]] 

        try:
            Part, Chapter, Section = Category.split("; ")
        except:
            Part, Chapter, Section = Category.split("/")

        ProblemSet[i] = [FileName, Title, Difficulty, Part, Chapter, Section, Tags, Source, Question, Answer]

    df = pd.DataFrame(ProblemSet, columns=["FileName", "Title", "Difficulty", "Part", "Chapter", "Section", "Tags", "Source", "Question", "Answer"])

    return df

def Generate_Jemdoc_Source_file(df):
    for Part in set(df.Part):        
        for Chapter in sorted(set(df[df.Part == Part].Chapter)):            
            page = f"= {Chapter} ({len(df[(df.Part == Part) & (df.Chapter == Chapter)])} Problems)\n\n"

            sorted_Sections = sorted(set(df[(df.Part == Part) & (df.Chapter == Chapter)].Section))
            for Section in sorted_Sections:
                S = Section.replace("C++", "C\+\+")
                page += f"- {S} ({len(df[(df.Part == Part) & (df.Chapter == Chapter) & (df.Section == Section)])} Problems)\n"                

            probID = 0            
            for Section in sorted_Sections:
                page += "== " + Section.replace("C++", "C\+\+") + "\n\n"                
                for i, p in df[(df.Part == Part) & (df.Chapter == Chapter) & (df.Section == Section)].iterrows():
                    probID += 1
                    page += f"~~~\n*Question \#{probID}: *\n"
                    page += p.Question.replace("\\begin{align}", "\\(").replace("\\end{align}", "\\)").replace("C++", "C\+\+")
                    page += "\\n\\n"                    
                    page += "*Title: *" + p.Title + "\\n"
                    page += "*FileName: *" + p.FileName + "\\n"
                    page += "*Difficulty: *" + p.Difficulty + "\\n"
                    page += "*Category: *" + p.Part + "\/" + p.Chapter + "\/" + p.Section.replace("C++", "C\+\+") + "\\n"
                    page += "*Tags: *" + p.Tags + "\\n"
                    page += "*Source: *" + p.Source + "\\n"
                    page += "\n"
                    page += "~~~\n\n"

                    page += "*Answer: *\n"
                    page += p.Answer.replace("\\begin{align}", "\\(\n\\begin{align}").replace("\\end{align}", "\\end{align}\n\\)\n").replace("```", "~~~\n").replace("C++", "C\+\+")
                    page += "\n\n"

            fname = Part.replace(" ", "_") + "_" + Chapter.replace(" ", "_")
            page = "# jemdoc: menu{MENU_Interview}{" + fname + ".html}\n" + page            

            f = open("../Jemdoc/" + fname + ".jemdoc", "w")            
            f.write(page)
            f.close()
    
def Generate_TeX_Source_File(pList) -> str():
    Q = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    A = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    for i, problem in enumerate(pList):
        FileName, Title, Difficulty, Category, Tags, Source = problem.Metadata.values()

        # Question pre-processing
        Question = re.sub(r"\*\*([\w+ ]+)\*\*", r"{\\bf{\1}}", problem.Question) # bold font        
        Question = re.sub(r"```([^`]+)```", r"\\begin{verbatim}\1\\end{verbatim}\n", Question) # code
        
        # Answer pre-processing
        Answer = re.sub(r"\*\*([\w+ ]+)\*\*", r"{\\bf{\1}}", problem.Answer) # bold font
        Answer = re.sub(r"```([^`]+)```", r"\\begin{verbatim}\1\\end{verbatim}\n", Answer) # code
        
        Question = "\\begin{question}{" + Title + "}{" + Difficulty + "}{\#" + FileName + "; " + Tags + "; " + Source + "}\n"
        Question += problem.Question
        Question += "\\end{question}\n\n"

        Answer = "\\begin{answer}{" + Title + "}\n"
        Answer += problem.Answer
        Answer += "\\end{answer}\n"

        Part, Chapter, Section = Category.split(";")

        Q[Part][Chapter][Section].append(Question)        
        A[Part][Chapter][Section].append(Answer)

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
            body += "".join([v for k, v in A[Part][Chapter].items()])
    
    pre  = open("../LaTex/pre.txt", "r").read()
    post = open("../LaTex/post.txt", "r").read()    
    tex  = pre + body + post

    return tex

def Write_pdf_File(tex):
    f = open("../LaTeX/InterviewQuestionBank.tex", "w")
    f.write(tex)
    f.close()
    
    subprocess.run(["pdflatex", "-output-directory=_build", "../LaTeX/InterviewQuestionBank.tex"], shell = True)

Generate_Jemdoc_Source_file(Read_Problems())
