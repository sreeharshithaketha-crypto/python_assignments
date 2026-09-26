# Program 105: Login system

saved_username = "admin"
saved_password = "Python@123"

username = input("Enter username: ").strip()
password = input("Enter password: ")

if username == saved_username and password == saved_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")
