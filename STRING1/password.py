# Check whether a password has at least one digit.
password = input("Enter password: ")
has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True
print(has_digit)