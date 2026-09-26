# Program 138: Password validation extended

password = input("Enter password: ")

# Check length
if len(password) < 8:
    print("Password must have at least 8 characters")
else:
    # Check for uppercase
    has_upper = any(c.isupper() for c in password)
    # Check for lowercase
    has_lower = any(c.islower() for c in password)
    # Check for digit
    has_digit = any(c.isdigit() for c in password)
    # Check for special
    has_special = any(not c.isalnum() for c in password)
    
    if has_upper and has_lower and has_digit and has_special:
        print("Strong Password")
    else:
        print("Weak Password")
