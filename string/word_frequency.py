# Count the frequency of each word.
words = "red blue red green blue red".split()
for word in sorted(set(words)):
    print(word, words.count(word))