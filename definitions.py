class Operator:
    def __init__(self, function, associativity, priority):
        self.function = function
        self.associativity = associativity
        self.priority = priority

class Function:
    def __init__(self, function):
        self.function = function

OPERATORS = {
    '+' : Operator(None, "Left", 1),
    '-' : Operator(None, "Left", 1),
    '*' : Operator(None, "Left", 2),
    '/' : Operator(None, "Left", 2),
    '^' : Operator(None, "Right", 3)
}

FUNCTIONS = {
    "sqrt" : Function(None),
    "exp" : Function(None),
    "sin" : Function(None),
    "cos" : Function(None),
    "tan" : Function(None),
    "sinh" : Function(None),
    "cosh" : Function(None),
    "tanh" : Function(None),
    "arcsin" : Function(None),
    "arccos" : Function(None),
    "arctan" : Function(None),
    "arcsinh" : Function(None),
    "arccosh" : Function(None),
    "arctanh" : Function(None),
    "ln" : Function(None),
    "log" : Function(None),
    "!" : Function(None)
}

CONSTANTS = {
    'g' : 9.81,
    'c' : 299792458,
    'e' : 2.718281828459
}