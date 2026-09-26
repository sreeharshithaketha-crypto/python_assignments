# Program 130: Extract special characters

text = "Python@123#Programming!"
special = ""

for character in text:
    if not character.isalnum() and not character.isspace():
        special += character

print(f"String: {text}")
print(f"Special characters: {special}")
