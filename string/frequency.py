# Count the frequency of each character.
text = "banana"
for char in sorted(set(text)):
    print(char, text.count(char))