# Program 123: Best practices - join for multiple strings

words = ["Python", "is", "easy"]

# Recommended
sentence = " ".join(words)
print(f"Using join: {sentence}")

# Not recommended (in loops)
result = ""
for word in words:
    result += " " + word
print(f"Using concatenation: {result}")
