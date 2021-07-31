import math


# Static Methods:
def n_sigfig(a, n):
    sigfig = math.floor(math.log(a, 10)) + 1  # number of significant digits in value
    return round(a, n - sigfig + 1)  # returns value to "n" significant figures


def addition(a, b):
    return int(a) + int(b)


def division(a, b):
    return float(b) / float(a)


def multiplication(a, b):
    return int(a) * int(b)


def square(a):
    return int(a) ** 2


def square_root(a):
    return math.sqrt(int(a))


def subtraction(a, b):
    return int(b) - int(a)


class Calculator:
    # Initialization:
    def __init__(self, sigfig=9):
        self.result = 0
        self.sigfig = sigfig  # modify significant figures, or assume 9 digits

    # Object Methods:
    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def divide(self, a, b):
        self.result = round(division(a, b), self.sigfig)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = n_sigfig(square_root(a), self.sigfig)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result
