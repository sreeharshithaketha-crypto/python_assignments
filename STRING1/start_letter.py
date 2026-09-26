# Print words beginning with a particular letter.
words = "apple banana avocado orange".split()
for word in words:
    if word.startswith("a"):
        print(word)