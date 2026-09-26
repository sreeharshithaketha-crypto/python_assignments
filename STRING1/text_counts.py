# Count words, characters, digits, vowels, and spaces.
text = "I have 2 pens"
vowels = 0
digits = 0
spaces = 0
for char in text.lower():
    if char in "aeiou":
        vowels += 1
    if char.isdigit():
        digits += 1
    if char == " ":
        spaces += 1
print("Words:", len(text.split()))
print("Characters:", len(text))
print("Digits:", digits)
print("Vowels:", vowels)
print("Spaces:", spaces)