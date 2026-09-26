# Program 97: Docstring example

def add(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b

print(f"Result: {add(5, 3)}")
print(f"Docstring: {add.__doc__}")
