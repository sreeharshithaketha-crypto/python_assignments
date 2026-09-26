# Find the largest word in a sentence.
words = "Python is very useful".split()
print(max(words, key=len))