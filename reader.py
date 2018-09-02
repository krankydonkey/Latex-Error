from number import Number
from shunt import Shunt

def read_structure(line):
    structure = []
    line = line.replace(" ", "")
    line = line.split(",")
    count = 0
    while count < len(line):
        var = line[count]
        count += 1
        if count < len(line):
            if line[count] == "Error":
                structure.append((var, True))
                count += 1
        else:
            structure.append((var, False))   
    return structure

def read_vars(line, structure, variables):
    line = line.replace(" ", "")
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
        equation = line.strip()
        equation = equation.replace(" ", "")
        equation = equation.split("=")
        shunt = Shunt()
        shunted = shunt.convert(equation[1])
        equations.append((equation[0], shunted))
    return equations