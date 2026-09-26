try:
    num= int(input("Enter a number: "))
    print(100 / num)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Zero is not allowed.")