from definitions import OPERATORS, FUNCTIONS, Function

class Shunt:
    def __init__(self):
        self.output = []
        self.operators = []

    def process(self, string):
        if string == "":
            return
        elif string in FUNCTIONS:
            self.operators.append(FUNCTIONS.get(string))
        else:
            self.output.append(string)
    
    # Looks at operators on the top of the stack and transfers them to the output
    # stack if their priority is greater than the given operator, or is equal to
    # and has left associativity. It then appends the given operator to the
    # operators stack.
    def consume(self, operator):
        priority = operator.priority
        while self.operators:
            prev = self.operators[-1]
            if prev == '(':
                break
            prev_priority = prev.priority
            if prev_priority > priority:
                self.output.append(self.operators.pop())
            elif prev_priority == priority and prev.associativity == "Left":
                self.output.append(self.operators.pop())
            else:
                break
        self.operators.append(operator)

    # Pops operators from the operators stack and appends them to the output until
    # a left bracket ')' is found. If no bracket is found, a SyntaxError is raised.
    # If the operator before the bracket is a function, it is also appended.
    def match_bracket(self):
        while True:
            if self.operators:
                operator = self.operators.pop()
                if operator == '(':
                    break
                else:
                    self.output.append(operator)
            else:
                raise SyntaxError("Incorrect number of brackets")
        if self.operators:
            operator = self.operators[-1]
            if type(operator) is Function:
                self.output.append(self.operators.pop())


    # Takes an infix notation expression and converts it to postfix.
    def convert(self, string):
        current = ""
        for char in string:
            if char in OPERATORS:
                self.process(current)
                current = ""
                self.consume(OPERATORS.get(char))
            elif char == '(':
                self.process(current)
                current = ""
                self.operators.append('(')
            elif char == ')':
                self.process(current)
                current = ""
                self.match_bracket()
            else:
                current = current + char
        self.process(current)
        self.output += self.operators[::-1]
        return self.output        

shunter = Shunt()
print(shunter.convert("a*b+c*sin(d*cos(e))"))