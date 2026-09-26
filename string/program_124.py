# Program 124: Best practices - validation

age_input = input("Enter age: ")

if age_input.isdigit():
    age = int(age_input)
    print(f"Valid age: {age}")
else:
    print("Invalid input. Please enter a number.")
