try:
    num1 = int(input("Enter first number: "))
    num2= int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Enter integers only.")
except ZeroDivisionError:
    print("The second number cannot be zero.")