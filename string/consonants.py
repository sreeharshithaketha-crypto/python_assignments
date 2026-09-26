# Count the consonants in a string.
text = "Hello Python"
count = 0
for char in text.lower():
    if char.isalpha() and char not in "aeiou":
        count += 1
print(count)