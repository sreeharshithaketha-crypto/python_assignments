# 8. Create a dictionary and count the frequency of each character in a given string.
text = "hello"
frequency = {}
for character in text:
    frequency[character] = frequency.get(character, 0) + 1
print(frequency)
