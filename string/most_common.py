# Find the most frequently occurring character.
text = "banana"
print(max(set(text), key=text.count))