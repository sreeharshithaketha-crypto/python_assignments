# Assignment Question 29: Write a mobile-number validation program

mobile = input("Enter mobile number: ")

if mobile.isdigit() and len(mobile) == 10:
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
