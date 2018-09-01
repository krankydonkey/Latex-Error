from definitions import Operator, Function, CONSTANTS
from number import Number
from shunt import Shunt

def rpn(output, variables, file):
    stack = []
    for element in output:
        if type(element) is Operator:
            num2 = stack.pop()
            num1 = stack.pop()
            evaluated = element.function(num1, num2)
            file.write(evaluated.getError() + "\n")
            stack.append(evaluated)
        elif type(element) is Function:
            num = stack.pop()
            evaluated = element.function(num)
            file.write(evaluated.getError() + "\n")
            stack.append(evaluated)
        else:
            if element in variables:
                stack.append(variables.get(element))
            elif element in CONSTANTS:
                stack.append(CONSTANTS.get(element))
            else:
                number = Number(float(element), element)
                stack.append(number)
    return stack.pop()