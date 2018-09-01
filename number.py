import math

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

def diff(string):
    return "\\delta " + string

# Raises string2 as the power of string1.
def order(string1, string2):
    return string1 + " ^{ " + string2 + " }"

# Returns the given string squared
def square(string):
    return order(string, "2")

# Converts the two strings into a fraction.
def fraction(string1, string2):
    return "\\dfrac{ " + string1 + " }{ " + string2 + " }"




# Returns the error of the number as a percentage of its value.
def percent(num):
    return num.error/num.value

# Returns a latex fraction representing the percentage error.
def percent_var(num):
    return fraction(diff(num.string), num.string)

# Handles the error and associated string calculations for addition
# and subtraction.
def addsub(num1, num2, value, string):
    error = math.sqrt(num1.error**2 + num2.error**2)
    error_vars = root(square(diff(num1.string)) + " " \
            + square(diff(num2.string)))
    error_nums = root(square(diff(str(num1.error))) + " " \
            + square(diff(str(num2.error))))
    return Number(value, error, string, error_vars, error_nums)

def add(num1, num2):
    value = num1.value + num2.value
    string = num1.string + "+" + num2.string
    return addsub(num1, num2, value, string)

def subtract(num1, num2):
    value = num1.value - num2.value
    string = num1.string + "-" + num2.string
    return addsub(num1, num2, value, string)

# Handles the error and associated string calculations for multiplication
# and division.
def muldiv(num1, num2, value, string):
    delta1 = num1.error/num1.value
    delta2 = num2.error/num2.value
    error = value*math.sqrt(delta1**2 + delta2**2)
    error_vars = string + " \\sqrt{ " + enclose(percent_var(num1)) \
            + "^{2} + " + enclose(percent_var(num2)) + "^{2} }"
    error_nums = str(value) + " \\sqrt{ " + str(percent(num1)) \
            + "^{2} + " + str(percent(num2)) + "^{2} }"
    return Number(value, error, string, error_vars, error_nums)

def multiply(num1, num2):
    value = num1.value * num2.value
    string = num1.string + PRODUCT + num2.string
    return muldiv(num1, num2, value, string)

def divide(num1, num2):
    value = num1.value / num2.value
    string = "\\dfrac{ " + num1.string + " }{ " + num2.string + " }"
    return muldiv(num1, num2, value, string)

def power(num1, num2):
    value = num1.value**num2.value
    string = num1.string + "^{" + num2.string + "}"
    error = abs(value * num2.value * percent(num1))
    error_vars = "|" + string + PRODUCT + num2.string + PRODUCT \
            + percent_var(num1) + "|"
    error_nums = "|" + str(value) + PRODUCT + str(num2.value) + PRODUCT \
            + str(percent(num1)) + "|"
    return Number(value, error, string, error_vars, error_nums)


num1 = Number(2, 0.5, "a")
num2 = Number(4, 0.25, "b")
num3 = power(num1, num2)
print(num3.error_vars)





