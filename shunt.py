from definitions import OPERATORS, FUNCTIONS, Function, CONSTANTS

def process(string, output, operators):
    output.append(string)

# Looks at operators on the top of the stack and transfers them to the output
# stack if their priority is greater than the given operator, or is equal to
# and has left associativity. It then appends the given operator to the
# operators stack.
def consume(operator, output, operators):
    priority = operator.priority
    while operators:
        prev = operators[-1]
        if prev == '(':
            break
        prev_priority = prev.priority
        if prev_priority > priority:
            output.append(operators.pop())
        elif prev_priority == priority and prev.associativity == "Left":
            output.append(operators.pop())
        else:
            break
    operators.append(operator)

# Pops operators from the operators stack and appends them to the output until
# a left bracket ')' is found. If no bracket is found, a SyntaxError is raised.
# If the operator before the bracket is a function, it is also appended.
def match_bracket(output, operators):
    while True:
        if operators:
            operator = operators.pop()
            if operator == '(':
                break
            else:
                output.append(operator)
        else:
            raise SyntaxError("Incorrect number of brackets")
    if operators:
        operator = operators[-1]
        if type(operator) is Function:
            output.append(operators.pop())
        

def convert(string):
    output = []
    operators = []
    current = ""
    for char in string:
        if char in OPERATORS:
            print(char)
            process(current, output, operators)
            consume(OPERATORS.get(char), output, operators)
            current = ""
        elif char == '(':
            operators.append('(')
        elif char == ')':
            match_bracket(output, operators)
        else:
            current = current + char
    if current != "":
        process(current, output, operators)
        print(operators)
        output += operators[::-1]
    return output
        


print(convert("a*b+c*d^e^f"))