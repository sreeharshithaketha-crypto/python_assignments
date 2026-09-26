# Reverse a string without slicing or reversed().
text = "Python"
answer = ""
for char in text:
    answer = char + answer
print(answer)