# Program 104: Student registration validation

name = input("Enter student name: ").strip().title()
course = input("Enter course: ").strip().title()
mobile = input("Enter mobile number: ").strip()

if not name.replace(" ", "").isalpha():
    print("Invalid student name")
elif not mobile.isdigit() or len(mobile) != 10:
    print("Invalid mobile number")
else:
    print("\nRegistration Successful")
    print(f"Name   : {name}")
    print(f"Course : {course}")
    print(f"Mobile : {mobile}")
