# Make a list of words longer than five characters.
words = "Python makes coding simple".split()
print([word for word in words if len(word) > 5])