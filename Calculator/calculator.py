from MathOperations.Addition import Addition
from MathOperations.Subtraction import Subtraction
from MathOperations.Multiplication import Multiplication
from MathOperations.Division import Division
from MathOperations.SquareRoot import SquareRoot
from MathOperations.Square import Square

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = Addition.sum(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = Subtraction.subtract(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = Multiplication.multiply(a, b)
        return self.result

    def divide(self, a, b):
        self.result = Division.divide(a, b)
        return self.result

    def sqroot(self, a):
        self.result = SquareRoot.sqroot(a)
        return self.result

    def square(self, a):
        self.result = Square.square(a)
        return self.result