try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(result)
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero occurred.")