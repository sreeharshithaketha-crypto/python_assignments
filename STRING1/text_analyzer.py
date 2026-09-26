# Display different counts in a text.
text = input("Enter text: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0
for char in text.lower():
    if char in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1
    else:
        special += 1
print("Characters:", len(text))
print("Words:", len(text.split()))
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special:", special)