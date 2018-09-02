from rpn import rpn
from reader import *
import os

"""
formula_file = open(input("Enter formula file name: "), 'r')
variable_file = open(input("Enter variable file name: "), 'r')
"""
formula_file = open("formulas.txt", 'r')
variable_file = open("variables.csv", 'r')
output_file = open("output.txt", 'w')
output_file.write("\\documentclass[a4paper]{article}\n")
output_file.write("\\usepackage{amsmath}\n")
output_file.write("\\usepackage{amssymb}\n")
output_file.write("\\begin{document}\n")
equations = read_formula(formula_file)
structure = read_structure(variable_file)
variables = {}
while read_vars(variable_file, structure, variables):
    for equation in equations:
        answer = rpn(equation[1], variables, output_file)
        variables[equation[0]] = answer
    output_file.write("\\newpage\n")
output_file.write("\\end{document}")
output_file.close()
os.system("pdflatex output.tex")