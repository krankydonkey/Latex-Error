from number import Number
from shunt import Shunt

def read_structure(file):
    structure = []
    line = (file.readline()[:-1]).split(",")
    count = 0
    while count < len(line):
        var = line[count]
        print(var)
        count += 1
        if count < len(line):
            if line[count] == "Error":
                structure.append((var, True))
                count += 1
        else:
            structure.append((var, False))   
    return structure

def read_vars(file, structure, variables):
    line = file.readline()
    if not line:
        return False
    line = (line.strip()).split(",")
    count = 0
    for var, status in structure:
        value = line[count]
        if value != "":
            value = float(value)
        error = 0
        count += 1
        if status:
            error = line[count]
            if error != "":
                error = float(error)
            count += 1
        number = Number(value, var, error)
        if value != "":
            variables[var] = number
    return True

def read_formula(file):
    equations = []
    for line in file:
        equation = (line.strip()).split("=")
        shunt = Shunt()
        shunted = shunt.convert(equation[1])
        equations.append((equation[0], shunted))
    return equations


        
"""
file = open("variables.csv", 'r')
variables = {}
structure = read_structure(file)
read_vars(file, structure, variables)
print(variables)
read_vars(file, structure, variables)
print(variables)
read_vars(file, structure, variables)
print(variables)
"""
file = open("formulas.txt", 'r')
print(read_formula(file))