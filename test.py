from number import *
import os
from shunt import Shunt
from rpn import rpn


num1 = Number(5, "a", 0.25)
num2 = Number(2, "b", 0.5)
num3 = Number(3, "c", 0.125)
num4 = Number(4, "d", 0.7)
variables = {
    "a" : num1,
    "b" : num2,
    "c" : num3,
    "d" : num4
}
expression = "a*b+c*sin(d)"
shunter = Shunt()
output = shunter.convert(expression)
print(output)


file = open("testout.tex", 'w')
file.write("\\documentclass[a4paper]{article}\n")
file.write("\\usepackage{amsmath}\n")
file.write("\\usepackage{amssymb}\n")
file.write("\\begin{document}\n")

number = rpn(output, variables, file)
print(number)
file.write(number.getError()+"\n")


file.write("\\end{document}")
file.close()
os.system("pdflatex testout.tex")