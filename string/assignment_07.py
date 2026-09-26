# Assignment 7: Explain slicing with step value

# Slicing with step value: string[start:end:step]
# Step defines how many characters to skip

text = "ABCDEFGHIJ"
print(f"String: {text}")
print(f"text[0:10:2] = {text[0:10:2]}")
print(f"text[::2] = {text[::2]}")
print(f"text[1::2] = {text[1::2]}")
print(f"text[::-1] = {text[::-1]}")
