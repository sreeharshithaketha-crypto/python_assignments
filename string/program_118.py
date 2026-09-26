# Program 118: Difference between lower and casefold

text1 = "PYTHON"
text2 = "python"

# Using lower
print(f"Using lower: {text1.lower() == text2.lower()}")

# Using casefold
print(f"Using casefold: {text1.casefold() == text2.casefold()}")
