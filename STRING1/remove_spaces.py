# Remove spaces without using replace().
text = "I like Python"
answer = ""
for char in text:
    if char != " ":
        answer += char
print(answer)