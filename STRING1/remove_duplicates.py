# Remove duplicate characters from a string.
text = "banana"
answer = ""
for char in text:
    if char not in answer:
        answer += char
print(answer)