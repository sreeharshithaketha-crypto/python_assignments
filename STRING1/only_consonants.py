# Print only the consonants from a string.
text = "Hello Python"
for char in text:
    if char.isalpha() and char.lower() not in "aeiou":
        print(char, end=" ")