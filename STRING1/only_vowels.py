# Print only the vowels from a string.
text = "Hello Python"
for char in text:
    if char.lower() in "aeiou":
        print(char, end=" ")