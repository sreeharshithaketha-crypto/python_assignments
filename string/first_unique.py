# Find the first non-repeated character.
text = "swiss"
for char in text:
    if text.count(char) == 1:
        print(char)
        break