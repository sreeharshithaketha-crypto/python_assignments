# Program 132: Email validation basic

email = input("Enter email address: ")

if "@" in email and "." in email:
    print("Basic email format is valid")
else:
    print("Invalid email format")
