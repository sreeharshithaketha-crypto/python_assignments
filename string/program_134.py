# Program 134: Find shortest word

sentence = input("Enter sentence: ")
words = sentence.split()
shortest = min(words, key=len)

print(f"Sentence: {sentence}")
print(f"Shortest Word: {shortest}")
