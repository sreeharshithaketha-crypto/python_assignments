# Extract all numbers from a string.
text = "I have 2 pens and 10 books"
numbers = ""
for char in text:
    if char.isdigit():
        numbers += char
print(numbers)