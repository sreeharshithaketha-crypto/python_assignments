# Assignment 22: Explain string formatting

# String formatting is used to insert values inside strings
# Python supports: concatenation, % formatting, format(), and f-strings

name = "Ravi"
age = 22

# Concatenation
print("Method 1 - Concatenation:")
print(name + " is " + str(age) + " years old")

# % Formatting
print("\nMethod 2 - % Formatting:")
print("My name is %s and my age is %d" % (name, age))

# format() method
print("\nMethod 3 - format() method:")
print("{} is {} years old".format(name, age))

# f-strings
print("\nMethod 4 - f-strings:")
print(f"{name} is {age} years old")
