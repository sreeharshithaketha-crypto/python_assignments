try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except ValueError:
    print("Please enter numbers only.")
except ZeroDivisionError:
    print("The second number cannot be zero.")
else:
    print("result:", result)
finally:
    print("Thank you for using the calculator.")