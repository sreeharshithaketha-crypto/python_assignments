# Program 127: Remove extra spaces

text = "Python    is    easy   to learn"
result = " ".join(text.split())

print(f"Original: '{text}'")
print(f"After cleanup: '{result}'")
