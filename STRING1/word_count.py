# Count words without using split().
text = "Python is very useful"
count = 0
inside_word = False
for char in text:
    if char != " " and not inside_word:
        count += 1
        inside_word = True
    elif char == " ":
        inside_word = False
print(count)