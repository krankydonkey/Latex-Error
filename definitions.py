from number import *
from functools import partial

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
    def __init__(self, string, function, numArgs):
        self.string = string
        self.function = function
        self.args = numArgs
    
    def __str__(self):
        return self.string
        
    def __repr__(self):
        return self.string
        

OPERATORS = {
    '+' : Operator("+", add, "Left", 1),
    '-' : Operator("-", subtract, "Left", 1),
    '*' : Operator("*", multiply, "Left", 2),
    '/' : Operator("/", divide, "Left", 2),
    '^' : Operator("^", power, "Right", 3)
}

FUNCTIONS = {
    "-" : Function("-", negative, 1),
    "sqrt" : Function("sqrt", sqrt, 1),
    "exp" : Function("exp", exp, 1),
    "sin" : Function("sin", sin, 1),
    "cos" : Function("cos", cos, 1),
    "tan" : Function("tan", tan, 1),
    "sinh" : Function("sinh", sinh, 1),
    "cosh" : Function("cosh", cosh, 1),
    "tanh" : Function("tanh", tanh, 1),
    "asin" : Function("asin", asin, 1),
    "acos" : Function("acos", acos, 1),
    "atan" : Function("atan", atan, 1),
    "asinh" : Function("asinh", asinh, 1),
    "acosh" : Function("acosh", acosh, 1),
    "atanh" : Function("atanh", atanh, 1),
    "ln" : Function("ln", ln, 1),
    "log" : Function("log", log, 2)
}

CONSTANTS = {
    'g' : Number(9.81, "g"),
    'c' : Number(299792458, "c"),
    'e' : Number(2.718281828459, "e")
}