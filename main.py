from rpn import rpn
from reader import *
from preamble import preamble
import os

"""
formula_file = open(input("Enter formula file name: "), 'r')
variable_file = open(input("Enter variable file name: "), 'r')
"""
formula_file = open("formulas.txt", 'r')
variable_file = open("variables.csv", 'r')
output_file = open("output.tex", 'w')
output_csv = open("output.csv", 'w')
preamble(output_file)
equations = read_formula(formula_file)
top = (variable_file.readline()).strip()
structure = read_structure(top)
variables = {}
samples = True

for equation in equations:
    top += "," + equation[0] + ",Error"
top += "\n"
output_csv.write(top)
string = ""
line = variable_file.readline()
while line:
    line = line.strip()
    string += line
    read_vars(line, structure, variables)
    output_csv.write(string)
    for equation in equations:
        answer = rpn(equation[1], variables, output_file, samples)
        answer.string = equation[0]
        answer.string_nums = ""
        variables[equation[0]] = answer
        string += "," + str(answer.value) + "," + str(answer.error)
    samples = False
    string += "\n"
    line = variable_file.readline()

output_csv.write(string[:-1])
output_file.write("\\end{document}")
output_file.close()
formula_file.close()
variable_file.close()
output_csv.close()
os.system("pdflatex output.tex")