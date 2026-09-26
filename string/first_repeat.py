# Find the first repeated character.
text = "programming"
seen = ""
for char in text:
    if char in seen:
        print(char)
        break
    seen += char