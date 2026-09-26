# Find the smallest word in a sentence.
words = "Python is very useful".split()
print(min(words, key=len))