try:
    age = int(input("Enter age: "))
    if age < 0 or age > 100:
        raise ValueError("Age must be between 0 and 100.")
    print("Age:", age)
except ValueError as e:
    print("Invalid age:", e)
