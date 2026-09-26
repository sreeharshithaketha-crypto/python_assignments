# Find all unique characters.
text = "programming"
for char in text:
    if text.count(char) == 1:
        print(char, end=" ")