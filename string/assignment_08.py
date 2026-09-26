# Assignment 8: Why are strings called immutable?

# Strings are immutable because they cannot be modified after creation
# Any operation on a string creates a new string

text = "Python"
print(f"Original string: {text}")

# Trying to modify directly will cause an error
# text[0] = "J"  # This will raise TypeError

# Correct approach - create a new string
text = "J" + text[1:]
print(f"New string: {text}")
