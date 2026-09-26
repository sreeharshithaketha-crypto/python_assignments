# Program 83: Case-insensitive comparison

text1 = "PYTHON"
text2 = "python"

print(f"Lowercase comparison: {text1.lower() == text2.lower()}")
print(f"Casefold comparison: {text1.casefold() == text2.casefold()}")
