import math

ADD = " + "
PRODUCT = " \\times "
DECIMALS = 5

class Number:
    def __init__(self, value, error, string="", string_nums="", error_vars="", error_nums=""):
        self.value = value
        self.error = error
        self.string = string
        self.string_nums = string_nums
        self.error_vars = error_vars
        self.error_nums = error_nums

    def __str__(self):
        return rstr(self.value) + " +- " + rstr(self.error)
    
    def __repr__(self):
        return rstr(self.value) + " +- " + rstr(self.error)
    
    def isConstant(self):
        return self.error == 0

    def getError(self):
        string = "\\begin{align*}\n" \
                + self.string + " &= " + self.string_nums + " \\\\\n" \
                + "&= " + rstr(self.value) + " \\\\[4mm]\n" \
                + diff(enclose(self.string)) + " &= " + self.error_vars \
                + " \\\\\n" + "&= " + self.error_nums + " \\\\\n" \
                + "&= " + rstr(self.error) + "\\\\[4mm]\n" \
                + "\\therefore " + self.string + " &= " + rstr(self.value) \
                + " \\pm " + rstr(self.error) + "\n" \
                + "\\end{align*}"
        return string

def rstr(number):
    return str(round(number, DECIMALS))

# Encloses the given string in latex brackets.
def enclose(string):
    return "\\left( " + string + " \\right)"

# Encloses the given string in a square root symbol.
def root(string):
    return "\\sqrt{ " + string + "}"

# Encloses the given string in absolute value brackets.
def mag(string):
    return "\\left| " + string + " \\right|"

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
def addsub(num1, num2, value, string, string_nums):
    error = math.sqrt(num1.error**2 + num2.error**2)
    error_vars = root(square(diff(num1.string)) + ADD \
            + square(diff(num2.string)))
    error_nums = root(square(rstr(num1.error)) + ADD \
            + square(rstr(num2.error)))
    return Number(value, error, string, string_nums, error_vars, error_nums)

def add(num1, num2):
    value = num1.value + num2.value
    string = num1.string + " + " + num2.string
    string_nums = rstr(num1.value) + " + " + rstr(num2.value)
    return addsub(num1, num2, value, string, string_nums)

def subtract(num1, num2):
    value = num1.value - num2.value
    string = num1.string + " - " + num2.string
    string_nums = rstr(num1.value) + " - " + rstr(num2.value)
    return addsub(num1, num2, value, string, string_nums)

def negative(num):
    value = -num.value
    string = "- " + num.string
    string_nums = "- " + str(num.value)
    error = num.error
    error_vars = num.error_vars
    error_nums = num.error_nums
    return Number(value, error, string, string_nums, error_vars, error_nums)

# Handles the error and associated string calculations for multiplication
# and division.
def muldiv(num1, num2, value, string, string_nums):
    error = abs(value*math.sqrt(percent(num1)**2 + percent(num2)**2))
    error_vars = mag(string) + root(square(enclose(percent_var(num1))) \
            + ADD + square(enclose(percent_var(num2))))
    error_nums = mag(rstr(value)) + root(square(rstr(percent(num1))) + ADD \
            + square(rstr(percent(num2))))
    return Number(value, error, string, string_nums, error_vars, error_nums)

def multiply(num1, num2):
    value = num1.value * num2.value
    string = num1.string + PRODUCT + num2.string
    string_nums = rstr(num1.value) + PRODUCT + rstr(num2.value)
    return muldiv(num1, num2, value, string, string_nums)

def divide(num1, num2):
    value = num1.value / num2.value
    string = fraction(num1.string, num2.string)
    string_nums = fraction(rstr(num1.value), rstr(num2.value))
    return muldiv(num1, num2, value, string, string_nums)

def power(num1, num2):
    value = num1.value**num2.value
    string = order(num1.string, num2.string)
    string_nums = order(rstr(num1.value), rstr(num2.value))
    error = abs(value * num2.value * percent(num1))
    error_vars = mag(string + PRODUCT + num2.string + PRODUCT \
            + percent_var(num1))
    error_nums = mag(rstr(value) + PRODUCT + rstr(num2.value) + PRODUCT \
            + rstr(percent(num1)))
    return Number(value, error, string, string_nums, error_vars, error_nums)

def sin(num):
    value = math.sin(num.value)
    string = "sin " + enclose(num.string)
    string_nums = "sin " + enclose(rstr(num.value))
    error = abs(math.cos(num.value)*num.error)
    error_vars = mag("cos " + enclose(num.string) + PRODUCT + diff(num.string))
    error_nums = mag(rstr(math.cos(num.value)) + PRODUCT + rstr(num.error))
    return Number(value, error, string, string_nums, error_vars, error_nums)

def cos(num):
    value = math.cos(num.value)
    string = "cos " + enclose(num.string)
    string_nums = "cos " + enclose(rstr(num.value))
    error = abs(math.sin(num.value)*num.error)
    error_vars = mag("sin " + enclose(num.string) + PRODUCT + diff(num.string))
    error_nums = mag(rstr(math.sin(num.value)) + PRODUCT + rstr(num.error))
    return Number(value, error, string, string_nums, error_vars, error_nums)

def tan(num):
    sinNum = sin(num)
    cosNum = cos(num)
    value = sinNum.value/cosNum.value
    string = "tan " + enclose(num.string)
    string_nums = "tan " + enclose(rstr(num.value))
    return muldiv(sinNum, cosNum, value, string, string_nums)

def sinh(num):
    value = math.sinh(num.value)
    string = "sinh " + enclose(num.string)
    string_nums = "sinh " + enclose(rstr(num.value))
    error = abs(math.cosh(num.value)*num.error)
    error_vars = mag("cosh " + enclose(num.string) + PRODUCT + diff(num.string))
    error_nums = mag(rstr(math.cosh(num.value)) + PRODUCT + rstr(num.error))
    return Number(value, error, string, string_nums, error_vars, error_nums)

def cosh(num):
    value = math.cosh(num.value)
    string = "cosh " + enclose(num.string)
    string_nums = "cosh " + enclose(rstr(num.value))
    error = abs(math.sinh(num.value)*num.error)
    error_vars = mag("sinh " + enclose(num.string) + PRODUCT + diff(num.string))
    error_nums = mag(rstr(math.sinh(num.value)) + PRODUCT + rstr(num.error))
    return Number(value, error, string, string_nums, error_vars, error_nums)

def tanh(num):
    sinhNum = sinh(num)
    coshNum = cosh(num)
    value = sinhNum.value/coshNum.value
    string = "tanh " + enclose(num.string)
    string_nums = "tanh " + enclose(rstr(num.value))
    return muldiv(sinhNum, coshNum, value, string, string_nums)

def exp(num):
    value = math.exp(num.value)
    string = order("e", num.string)
    string_nums = order("e", rstr(num.value))
    error = abs(num.value*num.error)
    error_vars = mag(num.string + PRODUCT + diff(num.string))
    error_nums = mag(rstr(num.value) + PRODUCT + rstr(num.error))
    return Number(value, error, string, string_nums, error_vars, error_nums)

def ln(num):
    value = math.log(num.value)
    string = natlog(num.string)
    string_nums = natlog(rstr(num.value))
    error = percent(num)
    error_vars = mag(fraction(diff(num.string), num.string))
    error_nums = mag(fraction(rstr(num.error), rstr(num.value)))
    return Number(value, error, string, string_nums, error_vars, error_nums)

def log(base, num):
    value = math.log(num.value, base)
    string = little("log", rstr(base)) + enclose(num.string)
    string_nums = little("log", rstr(base)) + enclose(rstr(num.value))
    error = abs(percent(num)/math.log(base))
    error_vars = mag(fraction(diff(num.string), num.string + PRODUCT \
            + natlog(rstr(base))))
    error_nums = mag(fraction(rstr(num.error), rstr(num.value) + PRODUCT \
            + rstr(math.log(base))))
    return Number(value, error, string, string_nums, error_vars, error_nums)





