# Count every word in a paragraph.
text = input("Enter a paragraph: ").lower()
words = text.split()
for word in sorted(set(words)):
    print(word, words.count(word))