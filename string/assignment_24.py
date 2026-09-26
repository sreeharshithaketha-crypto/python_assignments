# Assignment 24: Raw strings

print("=" * 50)
print("ASSIGNMENT 24: Raw strings")
print("=" * 50)

# Normal string
normal = "C:\\newfolder\\file.txt"
print(f"Normal: {normal}")

# Raw string
raw = r"C:\newfolder\file.txt"
print(f"Raw: {raw}")

# Useful for regex
pattern = r"\d+\w+"
print(f"\nRegex pattern: {pattern}")

# Raw strings treat backslash as literal character
