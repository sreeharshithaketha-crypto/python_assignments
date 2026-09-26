try:
    num = int(input("Enter a number: "))
    print(100 / num)
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Zero is not allowed.")
finally:
    print("Program execution completed.")