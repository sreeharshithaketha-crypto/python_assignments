# Count the spaces in a string.
text = "Hello my friend"
count = 0
for char in text:
    if char == " ":
        count += 1
print(count)