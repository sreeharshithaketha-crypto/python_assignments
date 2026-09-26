correct_username = "admin"
correct_password = "python123"
try:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username != correct_username:
        raise ValueError("Invalid username.")
    if password != correct_password:
        raise ValueError("Invalid password.")
except ValueError as error:
    print("Login failed:", error)
else:
    print("Login successful.")
