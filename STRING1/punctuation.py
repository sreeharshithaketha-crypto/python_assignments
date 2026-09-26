# Remove punctuation marks from a string.
text = "Hello, Python!"
answer = ""
for char in text:
    if char.isalnum() or char == " ":
        answer += char
print(answer)