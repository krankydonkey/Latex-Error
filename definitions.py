class Operator:
    def __init__(self, string, function, associativity, priority):
        self.string = string
        self.function = function
        self.associativity = associativity
        self.priority = priority

    def __str__(self):
        return self.string
        
    def __repr__(self):
        return self.string
        

class Function:
    def __init__(self, string, function):
        self.string = string
        self.function = function
    
    def __str__(self):
        return self.string
        
    def __repr__(self):
        return self.string

OPERATORS = {
    '+' : Operator("+", None, "Left", 1),
    '-' : Operator("-", None, "Left", 1),
    '*' : Operator("*", None, "Left", 2),
    '/' : Operator("/", None, "Left", 2),
    '^' : Operator("^", None, "Right", 3)
}

FUNCTIONS = {
    "sqrt" : Function("sqrt", None),
    "exp" : Function("exp", None),
    "sin" : Function("sin", None),
    "cos" : Function("cos", None),
    "tan" : Function("tan", None),
    "sinh" : Function("sinh", None),
    "cosh" : Function("cosh", None),
    "tanh" : Function("tanh", None),
    "arcsin" : Function("arcsin", None),
    "arccos" : Function("arccos", None),
    "arctan" : Function("arctan", None),
    "arcsinh" : Function("arcsinh", None),
    "arccosh" : Function("arccosh", None),
    "arctanh" : Function("arctanh", None),
    "ln" : Function("ln", None),
    "log" : Function("log", None),
    "!" : Function("!", None)
}

CONSTANTS = {
    'g' : 9.81,
    'c' : 299792458,
    'e' : 2.718281828459
}