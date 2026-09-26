numbers = [10, 20, 30]
try:
    print(numbers[5])
except IndexError:
    print("The specified index does not exist.")