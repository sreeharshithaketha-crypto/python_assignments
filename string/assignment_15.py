# Assignment 15: Explain replace()

# replace() method replaces old text with new text
# Syntax: string.replace(old, new, count)

message = "I am learning Java"
result = message.replace("Java", "Python")

print(f"Original: {message}")
print(f"After replace: {result}")

# With count limit
text = "Java Java Java"
result2 = text.replace("Java", "Python", 2)
print(f"\nOriginal: {text}")
print(f"After replace (limit 2): {result2}")
