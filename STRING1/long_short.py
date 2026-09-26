# Find the longest and shortest words.
words = "Python is very useful".split()
print("Longest:", max(words, key=len))
print("Shortest:", min(words, key=len))