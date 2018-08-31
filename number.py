class Number:
    def __init__(self, value, error, string="", error_vars="", error_nums=""):
        self.value = value
        self.error = error
        self.string = string
        self.error_vars = error_vars
        self.error_nums = error_nums
    
hi = Number(1, 0, "woot")
print(hi.string)