# 6. Create a dictionary of words and their meanings. Ask the user for a word and display its meaning.
meanings = {"happy": "feeling good", "quick": "fast", "large": "big"}
word = input("Enter a word: ")
print(meanings.get(word, "Word not found"))
