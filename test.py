from number import *
import os

num1 = Number(5, 0.25, "a")
num2 = Number(2, 0.5, "b")
num3 = divide(num1, num2)

file = open("testout.tex", 'w')
file.write("\\documentclass[a4paper]{article}\n")
file.write("\\usepackage{amsmath}\n")
file.write("\\usepackage{amssymb}\n")
file.write("\\begin{document}\n")

file.write(num3.getError()+"\n")

file.write("\\end{document}")
file.close()
os.system("pdflatex testout.tex")