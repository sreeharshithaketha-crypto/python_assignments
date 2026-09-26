# Program 120: Common string errors

# Error 1: Invalid index
try:
    text = "Python"
    print(text[20])
except IndexError as e:
    print(f"Error 1 - IndexError: {e}")

# Error 2: Modifying string directly
try:
    text[0] = "J"
except TypeError as e:
    print(f"Error 2 - TypeError: {e}")

# Error 3: Concatenating string and integer
try:
    age = 22
    print("Age: " + age)
except TypeError as e:
    print(f"Error 3 - TypeError: {e}")

# Correct way
age = 22
print(f"Age: {age}")
