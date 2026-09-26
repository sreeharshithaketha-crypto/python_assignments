# Capitalize each word without using title().
words = "python string methods".split()
answer = []
for word in words:
    answer.append(word[0].upper() + word[1:])
print(" ".join(answer))