# Program 131: Username validation

username = input("Enter username: ")

if username.isalnum():
    print("Valid username")
else:
    print("Username should contain only letters and numbers")
