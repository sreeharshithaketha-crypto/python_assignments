# Program 12: Remove duplicate characters

text = "programming"
result = ""

for character in text:
    if character not in result:
        result += character

print(f"Original: {text}")
print(f"Without duplicates: {result}")
