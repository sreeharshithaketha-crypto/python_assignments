# Program 128: Extract numbers from string

text = "Order123Amount5000"
numbers = ""

for character in text:
    if character.isdigit():
        numbers += character

print(f"String: {text}")
print(f"Numbers: {numbers}")
