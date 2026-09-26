# Program 28: Strings with duplicate characters

text = "Mississippi"
print(f"String: {text}")
print(f"Length: {len(text)}")

from collections import Counter
char_count = Counter(text)
print(f"Character frequency: {dict(char_count)}")
