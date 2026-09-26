try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("Age must be 18 or above.")
except ValueError as error:
    print("Error:", error)
else:
    print("You are eligible to register.")
