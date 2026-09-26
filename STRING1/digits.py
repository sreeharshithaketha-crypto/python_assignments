# Count the digits in a string.
text = "abc123xyz45"
count = 0
for char in text:
    if char.isdigit():
        count += 1
print(count)