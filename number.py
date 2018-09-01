import math

ADD = " + "
PRODUCT = " \\times "

class Number:
    def __init__(self, value, error, string="", error_vars="", error_nums=""):
        self.value = value
        self.error = error
        self.string = string
        self.error_vars = error_vars
        self.error_nums = error_nums
    
    def isConstant(self):
        return self.error == 0


# Encloses the given string in latex brackets.
def enclose(string):
    return "\\left( " + string + " \\right)"

# Encloses the given string in a square root symbol.
def root(string):
    return "\\sqrt{ " + string + "}"

# Encloses the given string in absolute value brackets.
def mag(string):
    return "| " + string + " |"

# Appends the delta symbol to the start of the given string.
def diff(string):
    return "\\Delta " + string

# Returns the given string squared
def square(string):
    return order(string, "2")

# Raises string2 as the power of string1.
def order(string1, string2):
    return string1 + " ^ { " + string2 + " }"

# Lowers string2 as the subscript of string1.
def little(string1, string2):
    return string1 + "_{ " + string2 + " }"

# Converts the two strings into a fraction.
def fraction(string1, string2):
    return "\\dfrac{ " + string1 + " }{ " + string2 + " }"

# Returns the string natural log of the given string.
def natlog(string):
    return "ln " + enclose(string)



# Returns the error of the number as a percentage of its value.
def percent(num):
    return abs(num.error/num.value)

# Returns a latex fraction representing the percentage error.
def percent_var(num):
    return fraction(diff(num.string), num.string)

# Handles the error and associated string calculations for addition
# and subtraction.
def addsub(num1, num2, value, string):
    error = math.sqrt(num1.error**2 + num2.error**2)
    error_vars = root(square(diff(num1.string)) + ADD \
            + square(diff(num2.string)))
    error_nums = root(square(diff(str(num1.error))) + ADD \
            + square(diff(str(num2.error))))
    return Number(value, error, string, error_vars, error_nums)

def add(num1, num2):
    value = num1.value + num2.value
    string = num1.string + " + " + num2.string
    return addsub(num1, num2, value, string)

def subtract(num1, num2):
    value = num1.value - num2.value
    string = num1.string + " - " + num2.string
    return addsub(num1, num2, value, string)

# Handles the error and associated string calculations for multiplication
# and division.
def muldiv(num1, num2, value, string):
    delta1 = num1.error/num1.value
    delta2 = num2.error/num2.value
    error = value*math.sqrt(delta1**2 + delta2**2)
    error_vars = string + root(square(enclose(percent_var(num1))) \
            + ADD + square(enclose(percent_var(num2))))
    error_nums = str(value) + root(square(str(percent(num1))) + ADD \
            + square(str(percent(num2))))
    return Number(value, error, string, error_vars, error_nums)

def multiply(num1, num2):
    value = num1.value * num2.value
    string = num1.string + PRODUCT + num2.string
    return muldiv(num1, num2, value, string)

def divide(num1, num2):
    value = num1.value / num2.value
    string = fraction(num1.string, num2.string)
    return muldiv(num1, num2, value, string)

def power(num1, num2):
    value = num1.value**num2.value
    string = order(num1.string, num2.string)
    error = abs(value * num2.value * percent(num1))
    error_vars = mag(string + PRODUCT + num2.string + PRODUCT \
            + percent_var(num1))
    error_nums = mag(str(value) + PRODUCT + str(num2.value) + PRODUCT \
            + str(percent(num1)))
    return Number(value, error, string, error_vars, error_nums)

def sin(num):
    value = math.sin(num.value)
    string = "sin " + enclose(num.string)
    error = abs(math.cos(num.value)*num.error)
    error_vars = mag("cos " + enclose(num.string) + PRODUCT + diff(num.string))
    error_nums = mag(str(math.cos(num.value)) + PRODUCT + str(num.error))
    return Number(value, error, string, error_vars, error_nums)

def cos(num):
    value = math.cos(num.value)
    string = "cos " + enclose(num.string)
    error = abs(math.sin(num.value)*num.error)
    error_vars = mag("sin " + enclose(num.string) + PRODUCT + diff(num.string))
    error_nums = mag(str(math.sin(num.value)) + PRODUCT + str(num.error))
    return Number(value, error, string, error_vars, error_nums)

def tan(num):
    return divide(sin(num), cos(num))

def sinh(num):
    value = math.sinh(num.value)
    string = "sinh " + enclose(num.string)
    error = abs(math.cosh(num.value)*num.error)
    error_vars = mag("cosh " + enclose(num.string) + PRODUCT + diff(num.string))
    error_nums = mag(str(math.cosh(num.value)) + PRODUCT + str(num.error))
    return Number(value, error, string, error_vars, error_nums)

def cosh(num):
    value = math.cosh(num.value)
    string = "cosh " + enclose(num.string)
    error = abs(math.sinh(num.value)*num.error)
    error_vars = mag("sinh " + enclose(num.string) + PRODUCT + diff(num.string))
    error_nums = mag(str(math.sinh(num.value)) + PRODUCT + str(num.error))
    return Number(value, error, string, error_vars, error_nums)

def tanh(num):
    return divide(sinh(num), cosh(num))

def exp(num):
    value = math.exp(num)
    string = order("e", num.string)
    error = abs(num.value*num.error)
    error_vars = mag(num.string + PRODUCT + diff(num.string))
    error_nums = mag(str(num.value) + PRODUCT + str(num.error))
    return Number(value, error, string, error_vars, error_nums)

def ln(num):
    value = math.log(num.value)
    string = natlog(num.string)
    error = percent(num)
    error_vars = mag(fraction(diff(num.string), num.string))
    error_nums = mag(fraction(str(num.error), str(num.value)))
    return Number(value, error, string, error_vars, error_nums)

def log(base, num):
    value = math.log(num.value, base)
    string = little("log", str(base)) + enclose(num.string)
    error = abs(percent(num)/math.log(num.value))
    error_vars = mag(fraction(diff(num.string), num.string + PRODUCT \
            + natlog(num.string)))
    error_nums = mag(fraction(str(num.error), str(num.value) + PRODUCT \
            + str(math.log(num.value))))
    return Number(value, error, string, error_vars, error_nums)


num1 = Number(2, 0.5, "a")
num2 = Number(4, 0.25, "b")
num3 = sin(num1)
print(num3.error_vars)





