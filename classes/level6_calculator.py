# Q1: Create Calculator methods with parameters and return values.
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

calculator = Calculator()
print(calculator.add(5, 3))
print(calculator.subtract(5, 3))
