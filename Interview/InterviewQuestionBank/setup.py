import subprocess
from source.compile import *

Write_pdf_File(Generate_TeX_Source_File(Read_Problems("Problems/")))

subprocess.run(["start", "_build/InterviewQuestionBank.pdf"], shell = True)