try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    print("Result:", a / b)
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Division by zero.")
