# Remove duplicate words from a sentence.
words = "red blue red green blue".split()
answer = []
for word in words:
    if word not in answer:
        answer.append(word)
print(" ".join(answer))