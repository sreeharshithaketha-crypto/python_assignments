import math
try:
    result = math.exp(1000)
    print(result)
except OverflowError:
    print("The result is too large.")
