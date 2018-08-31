from definitions import OPERATORS, FUNCTIONS, Function, CONSTANTS
output = []
operators = []

def process(string):
    return 0

# Looks at operators on the top of the stack and transfers them to the output
# stack if their priority is greater than the given operator, or is equal to
# and has left associativity. It then appends the given operator to the
# operators stack.
def consume(operator):
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
    output.append(operator)

# Pops operators from the operators stack and appends them to the output until
# a left bracket ')' is found. If no bracket is found, a SyntaxError is raised.
# If the operator before the bracket is a function, it is also appended.
def match_bracket():
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
    current = ""
    for char in string:
        if char in OPERATORS:
            process(current)
            consume(char)
            current = ""
        elif char == '(':
            operators.append('(')
        elif char == ')':
            match_bracket()