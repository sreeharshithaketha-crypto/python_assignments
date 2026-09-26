# Program 129: Extract letters from string

text = "Python123Programming456"
letters = ""

for character in text:
    if character.isalpha():
        letters += character

print(f"String: {text}")
print(f"Letters: {letters}")
