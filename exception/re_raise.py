try:
    number = int(input("Enter a number: "))
    if number < 0:
        raise ValueError("Negative values are not allowed.")
except ValueError as error:
    print("Error detected:", error)
    raise
