import subprocess
from source.genTeXJemdoc import *

pList = Read_Problems("Problems/")

# Write_pdf_File(Generate_TeX_Source_File(pList))
# subprocess.run(["start", "_build/InterviewQuestionBank.pdf"], shell = True)
 
Generate_Jemdoc_Source_file(pList)