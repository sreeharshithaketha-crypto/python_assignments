# Program 126: Character frequency using dictionary

text = "python programming"
frequency = {}

for character in text:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

print(f"String: {text}")
print(f"Frequency: {frequency}")
