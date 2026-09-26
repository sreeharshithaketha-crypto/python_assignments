# Program 13: Find the first non-repeated character

text = "swiss"
print(f"String: {text}")

for character in text:
    if text.count(character) == 1:
        print("First Non-Repeated Character:", character)
        break
