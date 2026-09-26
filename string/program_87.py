# Program 87: Convert to string

age = 22
text_age = str(age)

print(f"Original: {age}, Type: {type(age)}")
print(f"Converted: {text_age}, Type: {type(text_age)}")

# Using in concatenation
message = "I am " + text_age + " years old"
print(message)
