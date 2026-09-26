# Find all duplicate characters.
text = "programming"
for char in sorted(set(text)):
    if text.count(char) > 1:
        print(char, end=" ")