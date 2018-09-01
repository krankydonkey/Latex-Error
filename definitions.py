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
    def __init__(self, string, function):
        self.string = string
        self.function = function
    
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
    "-" : Function("-", negative),
    "sqrt" : Function("sqrt", sqrt),
    "exp" : Function("exp", exp),
    "sin" : Function("sin", sin),
    "cos" : Function("cos", cos),
    "tan" : Function("tan", tan),
    "sinh" : Function("sinh", sinh),
    "cosh" : Function("cosh", cosh),
    "tanh" : Function("tanh", tanh),
    "asin" : Function("asin", asin),
    "acos" : Function("acos", acos),
    "atan" : Function("atan", atan),
    "asinh" : Function("asinh", asinh),
    "acosh" : Function("acosh", acosh),
    "atanh" : Function("atanh", atanh),
    "ln" : Function("ln", ln),
    "log" : Function("log", None),
    "!" : Function("!", None)
}

CONSTANTS = {
    'g' : Number(9.81, "g"),
    'c' : Number(299792458, "c"),
    'e' : Number(2.718281828459, "e")
}