# Q3: Create Calculator methods for four basic operations.
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

calculator = Calculator()
print(calculator.add(8, 2))
print(calculator.subtract(8, 2))
print(calculator.multiply(8, 2))
print(calculator.divide(8, 2))
