# Validate a username using string methods.
username = input("Enter username: ")
if username.isalnum() and len(username) >= 4:
    print("Valid username")
else:
    print("Invalid username")