# Program 121: Best practices - F-strings

name = "Ravi"
age = 25

# Recommended
print(f"Welcome {name}, age {age}")

# Not recommended
print("Welcome " + name + ", age " + str(age))
