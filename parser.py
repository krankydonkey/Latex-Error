import math

class Operator:
    def __init__(self, function, associativity, priority):
        self.function = function
        self.associativity = associativity
        self.priority = priority

LEFT = 0
RIGHT = 1

OPERATORS = {
    '+' : Operator(0, LEFT, 1),
    '-' : Operator(0, LEFT, 1),
    '*' : Operator(0, LEFT, 2),
    '/' : Operator(0, LEFT, 2),
    '^' : Operator(0, RIGHT, 3)
}

FUNCTIONS = {
    "exp" : math.exp,
    "sin" : math.sin
}