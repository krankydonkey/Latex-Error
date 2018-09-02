from rpn import rpn
from reader import *
import os

"""
formula_file = open(input("Enter formula file name: "), 'r')
variable_file = open(input("Enter variable file name: "), 'r')
"""
formula_file = open("formulas.txt", 'r')
variable_file = open("variables.csv", 'r')
output_file = open("output.tex", 'w')
output_csv = open("output.csv", 'w')
output_file.write("\\documentclass[a4paper]{article}\n")
output_file.write("\\usepackage{amsmath}\n")
output_file.write("\\usepackage{amssymb}\n")
output_file.write("\\begin{document}\n")
equations = read_formula(formula_file)
structure = read_structure(variable_file)
variables = {}
samples = True

string = ""
for equation in equations:
    string += equation[0] + ",Error,"
string = string[:-1] + "\n"
output_csv.write(string)
string = ""
while read_vars(variable_file, structure, variables):
    output_csv.write(string)
    string = ""
    for equation in equations:
        answer = rpn(equation[1], variables, output_file, samples)
        answer.string = equation[0]
        answer.string_nums = ""
        variables[equation[0]] = answer
        string += str(answer.value) + "," + str(answer.error) + ","
    samples = False
    string = string[:-1] + "\n"
output_csv.write(string[:-1])
output_file.write("\\end{document}")
output_file.close()
formula_file.close()
variable_file.close()
output_csv.close()
os.system("pdflatex output.tex")