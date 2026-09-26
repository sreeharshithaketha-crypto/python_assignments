# Program 143: Text processing pipeline

text = input("Enter text: ")

# Clean
cleaned = text.strip().lower()

# Split into words
words = cleaned.split()

# Count words
word_count = len(words)

# Unique words
unique_words = set(words)
unique_count = len(unique_words)

# Find longest word
longest = max(words, key=len) if words else ""

print(f"Original: {text}")
print(f"Total words: {word_count}")
print(f"Unique words: {unique_count}")
print(f"Longest word: {longest}")
